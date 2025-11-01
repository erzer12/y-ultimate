import React from 'react';
import { motion } from 'framer-motion';
import HeroSection from '../components/HeroSection';
import { Users, Calendar, Trophy, TrendingUp, Award, Activity } from 'lucide-react';

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

const Dashboard = () => {
  const stats = [
    {
      title: 'Active Children',
      value: '248',
      subtitle: '+12 this month',
      icon: Users,
      color: 'bg-primary-500',
    },
    {
      title: 'Total Sessions',
      value: '156',
      subtitle: '23 this week',
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
      title: 'Attendance Rate',
      value: '87%',
      subtitle: '+5% from last month',
      icon: TrendingUp,
      color: 'bg-yellow-500',
    },
  ];

  const recentActivities = [
    { type: 'session', title: 'Community Session at Hillside', time: '2 hours ago', icon: Activity },
    { type: 'assessment', title: 'New LSAS Assessment Completed', time: '4 hours ago', icon: Award },
    { type: 'tournament', title: 'Spring Tournament Registration Open', time: '1 day ago', icon: Trophy },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <HeroSection />

      {/* Dashboard Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          {stats.map((stat, index) => (
            <StatCard key={index} {...stat} />
          ))}
        </div>

        {/* Quick Actions & Recent Activity */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Quick Actions */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            className="bg-white rounded-2xl p-6 shadow-soft"
          >
            <h2 className="text-2xl font-headline font-bold text-gray-800 mb-6">Quick Actions</h2>
            <div className="space-y-3">
              <button className="w-full flex items-center justify-between p-4 rounded-xl bg-primary-50 hover:bg-primary-100 transition-colors duration-200 group">
                <span className="font-semibold text-primary-700">Mark Attendance</span>
                <Calendar className="w-5 h-5 text-primary-600 group-hover:translate-x-1 transition-transform" />
              </button>
              <button className="w-full flex items-center justify-between p-4 rounded-xl bg-secondary-50 hover:bg-secondary-100 transition-colors duration-200 group">
                <span className="font-semibold text-secondary-700">Add New Child</span>
                <Users className="w-5 h-5 text-secondary-600 group-hover:translate-x-1 transition-transform" />
              </button>
              <button className="w-full flex items-center justify-between p-4 rounded-xl bg-accent-50 hover:bg-accent-100 transition-colors duration-200 group">
                <span className="font-semibold text-accent-700">Create Session</span>
                <Activity className="w-5 h-5 text-accent-600 group-hover:translate-x-1 transition-transform" />
              </button>
            </div>
          </motion.div>

          {/* Recent Activity */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6 }}
            className="bg-white rounded-2xl p-6 shadow-soft"
          >
            <h2 className="text-2xl font-headline font-bold text-gray-800 mb-6">Recent Activity</h2>
            <div className="space-y-4">
              {recentActivities.map((activity, index) => {
                const Icon = activity.icon;
                return (
                  <div key={index} className="flex items-start space-x-4 p-3 rounded-lg hover:bg-gray-50 transition-colors">
                    <div className="p-2 bg-primary-100 rounded-lg">
                      <Icon className="w-5 h-5 text-primary-600" />
                    </div>
                    <div className="flex-1">
                      <p className="font-medium text-gray-800">{activity.title}</p>
                      <p className="text-sm text-gray-500">{activity.time}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </motion.div>
        </div>

        {/* Programme Overview */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="mt-8 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-2xl p-8 text-white shadow-lg"
        >
          <h2 className="text-3xl font-headline font-bold mb-4">Impact Dashboard</h2>
          <p className="text-lg mb-6 opacity-90">
            Track the growth and success of your programmes in real-time
          </p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-white bg-opacity-20 rounded-xl p-4 backdrop-blur-sm">
              <p className="text-sm opacity-80 mb-1">Total Programme Hours</p>
              <p className="text-3xl font-bold">1,456</p>
            </div>
            <div className="bg-white bg-opacity-20 rounded-xl p-4 backdrop-blur-sm">
              <p className="text-sm opacity-80 mb-1">Active Coaches</p>
              <p className="text-3xl font-bold">32</p>
            </div>
            <div className="bg-white bg-opacity-20 rounded-xl p-4 backdrop-blur-sm">
              <p className="text-sm opacity-80 mb-1">Communities Served</p>
              <p className="text-3xl font-bold">12</p>
            </div>
          </div>
        </motion.div>
      </div>
    </div>
  );
};

export default Dashboard;
