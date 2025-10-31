import { Router, Response } from 'express';
import prisma from '../utils/prisma';
import { authenticateToken, requireRole, AuthRequest } from '../middleware/auth';

const router = Router();

// Get sessions (optionally filter by date)
router.get('/', authenticateToken, async (req: AuthRequest, res: Response) => {
  try {
    const { date } = req.query;
    
    const whereClause: any = {};
    if (date) {
      const queryDate = new Date(date as string);
      const startOfDay = new Date(queryDate.setHours(0, 0, 0, 0));
      const endOfDay = new Date(queryDate.setHours(23, 59, 59, 999));
      
      whereClause.date = {
        gte: startOfDay,
        lte: endOfDay
      };
    }

    const sessions = await prisma.session.findMany({
      where: whereClause,
      include: {
        site: true,
        attendance: {
          include: {
            child: true
          }
        }
      },
      orderBy: {
        date: 'desc'
      }
    });

    res.json(sessions);
  } catch (error) {
    console.error('Error fetching sessions:', error);
    res.status(500).json({ error: 'Failed to fetch sessions' });
  }
});

// Create a new session
router.post('/', authenticateToken, requireRole('admin', 'manager'), async (req: AuthRequest, res: Response) => {
  try {
    const { date, siteId, notes } = req.body;

    if (!date || !siteId) {
      return res.status(400).json({ error: 'date and siteId are required' });
    }

    const session = await prisma.session.create({
      data: {
        date: new Date(date),
        siteId: parseInt(siteId, 10),
        notes: notes || null
      },
      include: {
        site: true
      }
    });

    res.status(201).json(session);
  } catch (error) {
    console.error('Error creating session:', error);
    res.status(500).json({ error: 'Failed to create session' });
  }
});

// Bulk save attendance for a session
router.post('/:id/attendance', authenticateToken, requireRole('admin', 'manager', 'coach'), async (req: AuthRequest, res: Response) => {
  try {
    const sessionId = parseInt(req.params.id, 10);
    const { attendance } = req.body;

    if (!Array.isArray(attendance)) {
      return res.status(400).json({ error: 'attendance must be an array' });
    }

    // Verify session exists
    const session = await prisma.session.findUnique({
      where: { id: sessionId }
    });

    if (!session) {
      return res.status(404).json({ error: 'Session not found' });
    }

    // Delete existing attendance records for this session
    await prisma.attendance.deleteMany({
      where: { sessionId }
    });

    // Create new attendance records
    const attendanceRecords = await Promise.all(
      attendance.map((record: any) =>
        prisma.attendance.create({
          data: {
            sessionId,
            childId: parseInt(record.childId, 10),
            present: Boolean(record.present),
            notes: record.notes || null
          },
          include: {
            child: true
          }
        })
      )
    );

    res.json({
      message: 'Attendance saved successfully',
      count: attendanceRecords.length,
      attendance: attendanceRecords
    });
  } catch (error) {
    console.error('Error saving attendance:', error);
    res.status(500).json({ error: 'Failed to save attendance' });
  }
});

export default router;
