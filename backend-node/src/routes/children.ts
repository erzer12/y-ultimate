import { Router, Response } from 'express';
import multer from 'multer';
import csv from 'csv-parser';
import { Readable } from 'stream';
import prisma from '../utils/prisma';
import { authenticateToken, requireRole, AuthRequest } from '../middleware/auth';

const router = Router();
const upload = multer({ storage: multer.memoryStorage() });

// Get all children
router.get('/', authenticateToken, async (req: AuthRequest, res: Response) => {
  try {
    const children = await prisma.child.findMany({
      include: {
        site: true
      },
      orderBy: {
        lastName: 'asc'
      }
    });
    res.json(children);
  } catch (error) {
    console.error('Error fetching children:', error);
    res.status(500).json({ error: 'Failed to fetch children' });
  }
});

// Create a new child
router.post('/', authenticateToken, requireRole('admin', 'manager'), async (req: AuthRequest, res: Response) => {
  try {
    const { firstName, lastName, dateOfBirth, siteId } = req.body;

    if (!firstName || !lastName || !siteId) {
      return res.status(400).json({ error: 'firstName, lastName, and siteId are required' });
    }

    const child = await prisma.child.create({
      data: {
        firstName,
        lastName,
        dateOfBirth: dateOfBirth ? new Date(dateOfBirth) : null,
        siteId: parseInt(siteId)
      },
      include: {
        site: true
      }
    });

    res.status(201).json(child);
  } catch (error) {
    console.error('Error creating child:', error);
    res.status(500).json({ error: 'Failed to create child' });
  }
});

// Import children from CSV
router.post('/import', authenticateToken, requireRole('admin'), upload.single('file'), async (req: AuthRequest, res: Response) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'CSV file is required' });
    }

    const results: any[] = [];
    const stream = Readable.from(req.file.buffer.toString());

    stream
      .pipe(csv())
      .on('data', (data) => results.push(data))
      .on('end', async () => {
        try {
          const imported = [];
          const errors = [];

          for (const row of results) {
            try {
              if (!row.firstName || !row.lastName || !row.siteId) {
                errors.push({ row, error: 'Missing required fields' });
                continue;
              }

              const child = await prisma.child.create({
                data: {
                  firstName: row.firstName,
                  lastName: row.lastName,
                  dateOfBirth: row.dateOfBirth ? new Date(row.dateOfBirth) : null,
                  siteId: parseInt(row.siteId)
                }
              });
              imported.push(child);
            } catch (error) {
              errors.push({ row, error: String(error) });
            }
          }

          res.json({
            message: 'Import completed',
            imported: imported.length,
            errors: errors.length,
            details: { imported, errors }
          });
        } catch (error) {
          console.error('Error importing children:', error);
          res.status(500).json({ error: 'Failed to import children' });
        }
      });
  } catch (error) {
    console.error('Error processing CSV:', error);
    res.status(500).json({ error: 'Failed to process CSV file' });
  }
});

export default router;
