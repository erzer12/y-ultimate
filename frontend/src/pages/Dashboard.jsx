import React from 'react';
import { motion } from 'framer-motion';
import HeroSection from '../components/HeroSection';
import { Users, Calendar, Trophy, TrendingUp, Award, Activity, MapPin, Heart, Target } from 'lucide-react';

const StatCard = ({ title, value, subtitle, icon: Icon, color }) => (
  <motion.div
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.5 }}
    className="bg-white rounded-2xl p-6 shadow-soft hover:shadow-lg transition-shadow duration-300"
  >
    <div className="flex items-start justify-between">
      <div>
        <p className="text-gray-500 text-sm font-medium mb-1">{title}</p>
        <h3 className="text-3xl font-headline font-bold text-gray-800 mb-2">{value}</h3>
        <p className="text-sm text-gray-600">{subtitle}</p>
      </div>
      <div className={`p-3 rounded-xl ${color}`}>
        <Icon className="w-6 h-6 text-white" />
      </div>
    </div>
  </motion.div>
);

const ProgrammeCard = ({ title, description, icon: Icon, color, stats }) => (
  <motion.div
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.6 }}
    className="bg-white rounded-2xl p-6 shadow-soft hover:shadow-lg transition-all duration-300"
  >
    <div className={`w-14 h-14 rounded-xl ${color} flex items-center justify-center mb-4`}>
      <Icon className="w-8 h-8 text-white" />
    </div>
    <h3 className="text-2xl font-headline font-bold text-gray-800 mb-3">{title}</h3>
    <p className="text-gray-600 mb-4">{description}</p>
    <div className="space-y-2">
      {stats.map((stat, index) => (
        <div key={index} className="flex items-center justify-between text-sm">
          <span className="text-gray-600">{stat.label}</span>
          <span className="font-semibold text-gray-800">{stat.value}</span>
        </div>
      ))}
    </div>
  </motion.div>
);

const Dashboard = () => {
  // Public statistics (visible to all)
  const publicStats = [
    {
      title: 'Active Children',
      value: '248',
      subtitle: 'Across all programmes',
      icon: Users,
      color: 'bg-primary-500',
    },
    {
      title: 'Weekly Sessions',
      value: '23',
      subtitle: 'This week',
      icon: Calendar,
      color: 'bg-secondary-500',
    },
    {
      title: 'Tournaments',
      value: '8',
      subtitle: '2 upcoming',
      icon: Trophy,
      color: 'bg-accent-500',
    },
    {
      title: 'Communities',
      value: '12',
      subtitle: 'Across Johannesburg',
      icon: MapPin,
      color: 'bg-yellow-500',
    },
  ];

  const programmes = [
    {
      title: 'School Programme',
      description: 'Weekly training sessions at partner schools, building life skills through Ultimate Frisbee',
      icon: Users,
      color: 'bg-primary-500',
      stats: [
        { label: 'Partner Schools', value: '8' },
        { label: 'Active Students', value: '156' },
        { label: 'Sessions per Week', value: '12' },
      ]
    },
    {
      title: 'Community Programme',
      description: 'After-school and weekend sessions in under-resourced communities',
      icon: Heart,
      color: 'bg-secondary-500',
      stats: [
        { label: 'Communities', value: '4' },
        { label: 'Participants', value: '92' },
        { label: 'Sessions per Week', value: '8' },
      ]
    },
    {
      title: 'Tournament Series',
      description: 'Competitive tournaments bringing teams together from across the region',
      icon: Trophy,
      color: 'bg-accent-500',
      stats: [
        { label: 'Annual Tournaments', value: '6' },
        { label: 'Participating Teams', value: '24' },
        { label: 'Total Athletes', value: '300+' },
      ]
    },
  ];

  const upcomingEvents = [
    { 
      type: 'session', 
      title: 'Community Session at Alexandra Park', 
      time: 'Today, 3:00 PM',
      icon: Activity,
      color: 'bg-primary-100 text-primary-600'
    },
    { 
      type: 'tournament', 
      title: 'Spring Ultimate Cup 2024 - Registration Open', 
      time: 'March 15-17',
      icon: Trophy,
      color: 'bg-accent-100 text-accent-600'
    },
    { 
      type: 'assessment', 
      title: 'Mid-Year Skills Assessment Week', 
      time: 'Next Week',
      icon: Award,
      color: 'bg-secondary-100 text-secondary-600'
    },
  ];

  const impactMetrics = [
    { label: 'Life Skills Taught', value: '6 Core Areas' },
    { label: 'Total Programme Hours', value: '1,456' },
    { label: 'Active Coaches', value: '32' },
    { label: 'Attendance Rate', value: '87%' },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section - Public */}
      <HeroSection />

      {/* Public Statistics */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
        >
          <h2 className="text-3xl font-headline font-bold text-gray-800 mb-8 text-center">
            Our Impact Today
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
            {publicStats.map((stat, index) => (
              <StatCard key={index} {...stat} />
            ))}
          </div>
        </motion.div>

        {/* Our Programmes */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5 }}
          className="mb-16"
        >
          <h2 className="text-3xl font-headline font-bold text-gray-800 mb-3 text-center">
            Our Programmes
          </h2>
          <p className="text-gray-600 text-center mb-8 max-w-3xl mx-auto">
            We run three core programmes designed to teach life skills through Ultimate Frisbee,
            reaching children across Johannesburg's under-resourced communities
          </p>
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {programmes.map((programme, index) => (
              <ProgrammeCard key={index} {...programme} />
            ))}
          </div>
        </motion.div>

        {/* Upcoming Events & Activities */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
          {/* Upcoming Events */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            className="bg-white rounded-2xl p-6 shadow-soft"
          >
            <h2 className="text-2xl font-headline font-bold text-gray-800 mb-6">Upcoming Events</h2>
            <div className="space-y-4">
              {upcomingEvents.map((event, index) => {
                const Icon = event.icon;
                return (
                  <div key={index} className="flex items-start space-x-4 p-3 rounded-lg hover:bg-gray-50 transition-colors">
                    <div className={`p-2 rounded-lg ${event.color}`}>
                      <Icon className="w-5 h-5" />
                    </div>
                    <div className="flex-1">
                      <p className="font-medium text-gray-800">{event.title}</p>
                      <p className="text-sm text-gray-500">{event.time}</p>
                    </div>
                  </div>
                );
              })}
            </div>
            <button className="w-full mt-6 bg-primary-50 hover:bg-primary-100 text-primary-700 font-semibold py-3 rounded-xl transition-colors duration-200">
              View All Events
            </button>
          </motion.div>

          {/* What We Teach */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            className="bg-white rounded-2xl p-6 shadow-soft"
          >
            <h2 className="text-2xl font-headline font-bold text-gray-800 mb-6">Life Skills We Develop</h2>
            <div className="space-y-4">
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-lg bg-primary-100 flex items-center justify-center">
                  <Target className="w-5 h-5 text-primary-600" />
                </div>
                <div>
                  <h4 className="font-semibold text-gray-800">Leadership</h4>
                  <p className="text-sm text-gray-600">Taking initiative and guiding others</p>
                </div>
              </div>
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-lg bg-secondary-100 flex items-center justify-center">
                  <Users className="w-5 h-5 text-secondary-600" />
                </div>
                <div>
                  <h4 className="font-semibold text-gray-800">Teamwork</h4>
                  <p className="text-sm text-gray-600">Collaborating effectively with others</p>
                </div>
              </div>
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-lg bg-accent-100 flex items-center justify-center">
                  <Activity className="w-5 h-5 text-accent-600" />
                </div>
                <div>
                  <h4 className="font-semibold text-gray-800">Communication</h4>
                  <p className="text-sm text-gray-600">Expressing ideas clearly and listening</p>
                </div>
              </div>
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-lg bg-yellow-100 flex items-center justify-center">
                  <TrendingUp className="w-5 h-5 text-yellow-600" />
                </div>
                <div>
                  <h4 className="font-semibold text-gray-800">Confidence & Resilience</h4>
                  <p className="text-sm text-gray-600">Building self-belief and bouncing back</p>
                </div>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Impact Dashboard */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="bg-gradient-to-r from-primary-500 to-secondary-500 rounded-2xl p-8 text-white shadow-lg"
        >
          <h2 className="text-3xl font-headline font-bold mb-4">Our Impact This Year</h2>
          <p className="text-lg mb-6 opacity-90">
            Making a difference in the lives of children through Ultimate Frisbee
          </p>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {impactMetrics.map((metric, index) => (
              <div key={index} className="bg-white bg-opacity-20 rounded-xl p-4 backdrop-blur-sm">
                <p className="text-sm opacity-80 mb-1">{metric.label}</p>
                <p className="text-2xl font-bold">{metric.value}</p>
              </div>
            ))}
          </div>
        </motion.div>

        {/* CTA Section */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.8 }}
          className="mt-16 text-center"
        >
          <h2 className="text-3xl font-headline font-bold text-gray-800 mb-4">
            Get Involved
          </h2>
          <p className="text-gray-600 mb-8 max-w-2xl mx-auto">
            Join us in making a difference. Whether you're a parent, volunteer, or supporter,
            there are many ways to contribute to Y-Ultimate's mission.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <button className="bg-primary-500 hover:bg-primary-600 text-white font-semibold px-8 py-4 rounded-xl shadow-lg transition-all duration-300 transform hover:scale-105">
              Register Your Child
            </button>
            <button className="bg-white hover:bg-gray-50 text-primary-600 font-semibold px-8 py-4 rounded-xl shadow-lg border-2 border-primary-500 transition-all duration-300">
              Volunteer With Us
            </button>
            <button className="bg-white hover:bg-gray-50 text-secondary-600 font-semibold px-8 py-4 rounded-xl shadow-lg border-2 border-secondary-500 transition-all duration-300">
              Donate
            </button>
          </div>
        </motion.div>
      </div>
    </div>
  );
};

export default Dashboard;
