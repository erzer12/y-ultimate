/**
 * Login Page Component
 * 
 * Provides a form for users to log in with email and password.
 * On successful login, redirects to the dashboard.
 * 
 * Key features:
 *   - Form handling with React state
 *   - Integration with AuthContext for login
 *   - Error handling and display
 *   - Redirect after successful login
 */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function LoginPage() {
  // Get the login function from AuthContext
  // This function will send credentials to the backend and store the token
  const { login } = useAuth();
  
  // useNavigate hook allows programmatic navigation
  // After successful login, we'll redirect the user to /dashboard
  const navigate = useNavigate();

  // Form state
  // useState() creates a reactive state variable that triggers re-renders when changed
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  /**
   * Handle Form Submit
   * 
   * Called when the user submits the login form.
   * 
   * Steps:
   *   1. Prevent default form submission (which would reload the page)
   *   2. Clear any previous errors
   *   3. Call the login function from AuthContext
   *   4. If successful, redirect to dashboard
   *   5. If failed, display error message
   */
  const handleSubmit = async (e) => {
    // Prevent the default form submission behavior (page reload)
    e.preventDefault();
    
    // Clear previous error
    setError('');
    setLoading(true);

    try {
      // Call the login function from AuthContext
      // This will:
      //   1. Send email/password to POST /api/v1/auth/login
      //   2. Store the returned JWT token
      //   3. Update the auth state (user, token, isAuthenticated)
      await login(email, password);
      
      // If login succeeds, redirect to dashboard
      navigate('/dashboard');
    } catch (err) {
      // If login fails, display an error message
      setError(err.response?.data?.detail || 'Login failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="max-w-md w-full bg-white rounded-lg shadow-md p-8">
        {/* Title */}
        <h2 className="text-3xl font-bold text-center text-gray-800 mb-8">
          Y-Ultimate Login
        </h2>

        {/* Error Message */}
        {error && (
          <div className="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}

        {/* Login Form */}
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Email Field */}
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
              Email
            </label>
            <input
              id="email"
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="you@example.com"
            />
          </div>

          {/* Password Field */}
          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
              Password
            </label>
            <input
              id="password"
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your password"
            />
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            disabled={loading}
            className="w-full py-2 px-4 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-md transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
          >
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </form>

        {/* Additional Links */}
        <div className="mt-6 text-center text-sm text-gray-600">
          <p>Don't have an account? Contact your administrator.</p>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
