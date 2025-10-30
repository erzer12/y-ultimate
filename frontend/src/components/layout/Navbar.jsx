/**
 * Navbar Component
 * 
 * This is a top navigation bar that could display:
 *   - User information
 *   - Notifications
 *   - Quick actions
 *   - Breadcrumbs
 * 
 * This is a placeholder component. Expand it as needed for your application.
 */

import React from 'react';
import { useAuth } from '../../context/AuthContext';

function Navbar() {
  const { user, isAuthenticated } = useAuth();

  return (
    <nav className="bg-white border-b border-gray-200 px-6 py-4">
      <div className="flex items-center justify-between">
        {/* Left side: Could show breadcrumbs or page title */}
        <div>
          <h2 className="text-xl font-semibold text-gray-800">
            {/* Page title could be dynamically set based on current route */}
          </h2>
        </div>

        {/* Right side: User info or actions */}
        <div className="flex items-center space-x-4">
          {isAuthenticated ? (
            <>
              {/* Placeholder for notifications, settings, etc. */}
              <span className="text-sm text-gray-600">
                Welcome, {user?.full_name || user?.email || 'User'}
              </span>
            </>
          ) : (
            <span className="text-sm text-gray-600">Not logged in</span>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
