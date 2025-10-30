/**
 * Sidebar Component
 * 
 * Provides navigation links for the application.
 * Uses React Router's Link component for client-side navigation.
 * 
 * CRITICAL: Why <Link> instead of <a>?
 *   <a href="/dashboard">
 *     - Causes a FULL PAGE RELOAD
 *     - Resets all React state
 *     - Slow (browser re-downloads all JavaScript)
 *   
 *   <Link to="/dashboard">
 *     - Client-side navigation (NO PAGE RELOAD)
 *     - React Router updates the URL and renders the new component
 *     - Fast and preserves application state
 *     - This is the React way of handling navigation
 */

import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

function Sidebar() {
  // Get current location to highlight active link
  const location = useLocation();
  
  // Get auth state to conditionally show/hide links
  const { isAuthenticated, user, logout } = useAuth();

  /**
   * Helper function to determine if a link is active
   * 
   * Returns true if the current URL path matches the link's path.
   * Used to highlight the current page in the navigation.
   */
  const isActive = (path) => {
    return location.pathname === path || location.pathname.startsWith(path + '/');
  };

  /**
   * Navigation Links
   * 
   * Each link is a React Router <Link> component, which:
   *   - Renders as an <a> tag in the HTML
   *   - Intercepts clicks to prevent full page reloads
   *   - Uses React Router for client-side navigation
   */
  const navLinks = [
    { path: '/dashboard', label: 'Dashboard', icon: '📊' },
    { path: '/tournaments', label: 'Tournaments', icon: '🏆' },
    { path: '/profiles', label: 'Child Profiles', icon: '👶' },
    // Add more links as needed
  ];

  return (
    <aside className="bg-gray-800 text-white w-64 flex-shrink-0">
      {/* Logo/Brand */}
      <div className="p-6 border-b border-gray-700">
        <h1 className="text-2xl font-bold">Y-Ultimate</h1>
        <p className="text-sm text-gray-400 mt-1">Management Platform</p>
      </div>

      {/* Navigation Links */}
      <nav className="p-4">
        <ul className="space-y-2">
          {navLinks.map((link) => (
            <li key={link.path}>
              {/*
                Link Component
                
                'to' prop: The destination URL path
                'className': Dynamic classes based on whether the link is active
                
                Why className is a function?
                  - We want different styles for active vs inactive links
                  - Active link: darker background to highlight current page
                  - Inactive link: lighter background, hover effect
              */}
              <Link
                to={link.path}
                className={`
                  flex items-center px-4 py-3 rounded-lg transition-colors
                  ${isActive(link.path)
                    ? 'bg-gray-900 text-white'
                    : 'text-gray-300 hover:bg-gray-700'
                  }
                `}
              >
                <span className="mr-3 text-xl">{link.icon}</span>
                <span>{link.label}</span>
              </Link>
            </li>
          ))}
        </ul>
      </nav>

      {/* User Section (if authenticated) */}
      {isAuthenticated && (
        <div className="absolute bottom-0 w-64 p-4 border-t border-gray-700">
          <div className="mb-3">
            <p className="text-sm font-medium">
              {user?.full_name || user?.email || 'User'}
            </p>
            <p className="text-xs text-gray-400">{user?.email || ''}</p>
          </div>
          <button
            onClick={logout}
            className="w-full px-4 py-2 bg-red-600 hover:bg-red-700 rounded-lg transition-colors"
          >
            Logout
          </button>
        </div>
      )}
    </aside>
  );
}

export default Sidebar;
