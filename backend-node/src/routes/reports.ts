import { Router, Response } from 'express';
import prisma from '../utils/prisma';
import { authenticateToken, requireRole, AuthRequest } from '../middleware/auth';

const router = Router();

// Get attendance report with CSV export
router.get('/attendance', authenticateToken, requireRole('admin', 'manager'), async (req: AuthRequest, res: Response) => {
  try {
    const { from, to, site } = req.query;

    if (!from || !to) {
      return res.status(400).json({ error: 'from and to date parameters are required' });
    }

    const whereClause: any = {
      session: {
        date: {
          gte: new Date(from as string),
          lte: new Date(to as string)
        }
      }
    };

    if (site) {
      whereClause.session.siteId = parseInt(site as string);
    }

    const attendanceRecords = await prisma.attendance.findMany({
      where: whereClause,
      include: {
        child: true,
        session: {
          include: {
            site: true
          }
        }
      },
      orderBy: {
        session: {
          date: 'asc'
        }
      }
    });

    // Generate CSV
    const csvHeader = 'Date,Site,Child First Name,Child Last Name,Present,Notes\n';
    const csvRows = attendanceRecords.map(record => {
      const date = new Date(record.session.date).toISOString().split('T')[0];
      const site = record.session.site.name;
      const firstName = record.child.firstName;
      const lastName = record.child.lastName;
      const present = record.present ? 'Yes' : 'No';
      const notes = record.notes || '';
      
      return `${date},${site},"${firstName}","${lastName}",${present},"${notes}"`;
    }).join('\n');

    const csv = csvHeader + csvRows;

    // Set headers for CSV download
    res.setHeader('Content-Type', 'text/csv');
    res.setHeader('Content-Disposition', `attachment; filename=attendance-report-${from}-to-${to}.csv`);
    res.send(csv);
  } catch (error) {
    console.error('Error generating attendance report:', error);
    res.status(500).json({ error: 'Failed to generate attendance report' });
  }
});

export default router;
