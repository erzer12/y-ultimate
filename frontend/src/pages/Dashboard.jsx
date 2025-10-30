/**
 * Dashboard Page Component
 * 
 * This page will be the main dashboard visible after login.
 * It could display:
 *   - Overview statistics
 *   - Recent tournaments
 *   - Upcoming events
 *   - Quick actions
 * 
 * This is a placeholder component. Expand it with actual dashboard content.
 */

import React from 'react';
import { useAuth } from '../context/AuthContext';

function Dashboard() {
  const { user } = useAuth();

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-800 mb-6">
        Dashboard
      </h1>

      {/* Welcome Message */}
      <div className="bg-white rounded-lg shadow p-6 mb-6">
        <h2 className="text-xl font-semibold mb-2">
          Welcome, {user?.full_name || user?.email || 'User'}!
        </h2>
        <p className="text-gray-600">
          This is your Y-Ultimate management dashboard. Use the sidebar to navigate.
        </p>
      </div>

      {/* Dashboard Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        {/* Stat Card 1 */}
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-600 mb-2">
            Active Tournaments
          </h3>
          <p className="text-3xl font-bold text-blue-600">0</p>
        </div>

        {/* Stat Card 2 */}
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-600 mb-2">
            Registered Teams
          </h3>
          <p className="text-3xl font-bold text-green-600">0</p>
        </div>

        {/* Stat Card 3 */}
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-600 mb-2">
            Child Profiles
          </h3>
          <p className="text-3xl font-bold text-purple-600">0</p>
        </div>
      </div>

      {/* Recent Activity */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">Recent Activity</h2>
        <p className="text-gray-600">No recent activity</p>
      </div>
    </div>
  );
}

export default Dashboard;
