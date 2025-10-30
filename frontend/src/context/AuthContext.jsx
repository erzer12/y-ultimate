/**
 * Authentication Context
 * 
 * This file provides global authentication state and functions using React Context.
 * 
 * What is React Context?
 *   - A way to share state across multiple components without "prop drilling"
 *   - Prop drilling = passing props through many intermediate components
 *   - Context provides a "global" state that any component can access
 * 
 * Why use Context for authentication?
 *   - Many components need to know if a user is logged in (Navbar, Sidebar, etc.)
 *   - Many components need access to the current user's data
 *   - Without Context, you'd have to pass user/login/logout through every component
 * 
 * This file provides:
 *   1. AuthContext: The React Context object
 *   2. AuthProvider: A component that wraps your app and provides auth state
 *   3. useAuth: A custom hook to easily access auth state in any component
 */

import React, { createContext, useContext, useState, useEffect } from 'react';
import apiClient from '../services/api';

/**
 * Create the Auth Context
 * 
 * This is the "container" for the authentication state.
 * Components can subscribe to this context to get auth data.
 */
const AuthContext = createContext(null);

/**
 * Auth Provider Component
 * 
 * This component maintains the authentication state and provides it to all children.
 * It should wrap your entire app (or at least the parts that need auth).
 * 
 * State:
 *   - user: The current logged-in user (or null if not logged in)
 *   - token: The JWT access token (or null if not logged in)
 *   - loading: Whether we're checking if a user is logged in (on app start)
 */
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);

  /**
   * Effect: Check for existing token on mount
   * 
   * When the app loads, check if there's a token in localStorage.
   * If there is, fetch the current user's data.
   */
  useEffect(() => {
    const storedToken = localStorage.getItem('access_token');
    if (storedToken) {
      setToken(storedToken);
      // TODO: Fetch current user data from /api/v1/auth/me
      // fetchCurrentUser(storedToken);
    }
    setLoading(false);
  }, []);

  /**
   * Login Function
   * 
   * Calls the backend login endpoint and stores the token.
   * 
   * Steps:
   *   1. Send email/password to POST /api/v1/auth/login
   *   2. Receive JWT token in response
   *   3. Store token in localStorage and state
   *   4. Fetch current user data
   * 
   * Usage in components:
   *   const { login } = useAuth();
   *   await login('user@example.com', 'password123');
   */
  const login = async (email, password) => {
    try {
      // TODO: Implement actual login API call
      // const response = await apiClient.post('/auth/login', { 
      //   username: email,  // OAuth2 standard uses "username" field
      //   password 
      // });
      // const { access_token } = response.data;
      // localStorage.setItem('access_token', access_token);
      // setToken(access_token);
      // fetchCurrentUser(access_token);
      
      console.log('Login function not yet fully implemented');
      throw new Error('Login not yet implemented');
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  };

  /**
   * Logout Function
   * 
   * Clears the authentication state and removes the token.
   * 
   * Steps:
   *   1. Remove token from localStorage
   *   2. Clear user and token state
   *   3. Optionally: Call backend logout endpoint
   * 
   * Usage in components:
   *   const { logout } = useAuth();
   *   logout();
   */
  const logout = () => {
    localStorage.removeItem('access_token');
    setToken(null);
    setUser(null);
  };

  /**
   * Context Value
   * 
   * This object is provided to all child components via the Context.
   * Any component can access this by calling useAuth().
   */
  const value = {
    user,
    token,
    loading,
    login,
    logout,
    isAuthenticated: !!token,  // Boolean: true if token exists
  };

  /**
   * Provider Component
   * 
   * Wraps all children and provides the auth value to them.
   * Any child component can access this value using useAuth().
   */
  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

/**
 * Custom Hook: useAuth
 * 
 * This is a convenience hook that makes it easy to access the auth context.
 * 
 * Without this hook:
 *   const context = useContext(AuthContext);
 *   if (!context) throw new Error('...');
 *   const { user, login, logout } = context;
 * 
 * With this hook:
 *   const { user, login, logout } = useAuth();
 * 
 * Usage in any component:
 *   import { useAuth } from '../context/AuthContext';
 *   
 *   function MyComponent() {
 *     const { user, isAuthenticated, logout } = useAuth();
 *     
 *     if (!isAuthenticated) {
 *       return <div>Please log in</div>;
 *     }
 *     
 *     return <div>Welcome, {user.email}</div>;
 *   }
 */
export const useAuth = () => {
  const context = useContext(AuthContext);
  
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  
  return context;
};
