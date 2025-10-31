import bcrypt from 'bcryptjs';
import prisma from './utils/prisma';

async function main() {
  console.log('🌱 Seeding database...');

  // Create users
  const hashedPassword = await bcrypt.hash('password123', 10);

  const admin = await prisma.user.upsert({
    where: { email: 'admin@yultimate.com' },
    update: {},
    create: {
      email: 'admin@yultimate.com',
      password: hashedPassword,
      name: 'Admin User',
      role: 'admin'
    }
  });

  const manager = await prisma.user.upsert({
    where: { email: 'manager@yultimate.com' },
    update: {},
    create: {
      email: 'manager@yultimate.com',
      password: hashedPassword,
      name: 'Manager User',
      role: 'manager'
    }
  });

  const coach = await prisma.user.upsert({
    where: { email: 'coach@yultimate.com' },
    update: {},
    create: {
      email: 'coach@yultimate.com',
      password: hashedPassword,
      name: 'Coach User',
      role: 'coach'
    }
  });

  console.log('✅ Created users:', { admin, manager, coach });

  // Create sites
  const site1 = await prisma.site.upsert({
    where: { id: 1 },
    update: {},
    create: {
      name: 'Downtown Community Center',
      location: '123 Main St, Seattle, WA'
    }
  });

  const site2 = await prisma.site.upsert({
    where: { id: 2 },
    update: {},
    create: {
      name: 'Westside Recreation Center',
      location: '456 West Ave, Seattle, WA'
    }
  });

  console.log('✅ Created sites:', { site1, site2 });

  // Create children
  const childrenData = [
    { firstName: 'Emma', lastName: 'Johnson', siteId: site1.id },
    { firstName: 'Liam', lastName: 'Smith', siteId: site1.id },
    { firstName: 'Olivia', lastName: 'Williams', siteId: site1.id },
    { firstName: 'Noah', lastName: 'Brown', siteId: site2.id },
    { firstName: 'Ava', lastName: 'Jones', siteId: site2.id },
    { firstName: 'Ethan', lastName: 'Garcia', siteId: site2.id },
    { firstName: 'Sophia', lastName: 'Martinez', siteId: site1.id },
    { firstName: 'Mason', lastName: 'Davis', siteId: site2.id }
  ];

  const children = await Promise.all(
    childrenData.map((child, index) =>
      prisma.child.upsert({
        where: { id: index + 1 },
        update: {},
        create: child
      })
    )
  );

  console.log(`✅ Created ${children.length} children`);

  // Create sessions
  const today = new Date();
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);

  const session1 = await prisma.session.upsert({
    where: { id: 1 },
    update: {},
    create: {
      date: yesterday,
      siteId: site1.id,
      notes: 'Regular training session'
    }
  });

  const session2 = await prisma.session.upsert({
    where: { id: 2 },
    update: {},
    create: {
      date: today,
      siteId: site2.id,
      notes: 'Practice game day'
    }
  });

  console.log('✅ Created sessions:', { session1, session2 });

  // Create sample attendance records for session1 (only for site1 children)
  const site1Children = children.filter((child) => child.siteId === site1.id);
  const attendanceData = site1Children.slice(0, 3).map((child, index) => ({
    sessionId: session1.id,
    childId: child.id,
    present: index !== 2 // First two present, third absent
  }));

  const attendance = await Promise.all(
    attendanceData.map((att) =>
      prisma.attendance.upsert({
        where: {
          sessionId_childId: {
            sessionId: att.sessionId,
            childId: att.childId
          }
        },
        update: {
          present: att.present
        },
        create: att
      })
    )
  );

  console.log(`✅ Created ${attendance.length} attendance records`);

  console.log('🎉 Seeding completed successfully!');
  console.log('\n📝 Test Credentials:');
  console.log('  Admin:   admin@yultimate.com / password123');
  console.log('  Manager: manager@yultimate.com / password123');
  console.log('  Coach:   coach@yultimate.com / password123');
}

main()
  .catch((e) => {
    console.error('❌ Seeding error:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
