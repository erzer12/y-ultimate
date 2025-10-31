/**
 * Authentication Service
 * 
 * This file will contain all authentication-related API calls.
 * It provides a clean interface for authentication operations.
 * 
 * Functions to implement:
 *   - login(email, password): Send credentials to backend
 *   - register(userData): Create a new user account
 *   - logout(): Clear token and session
 *   - getCurrentUser(token): Fetch current user data
 *   - refreshToken(): Refresh an expired token (if implementing refresh tokens)
 */

import apiClient from './api';

/**
 * Login User
 * 
 * Sends email and password to the backend login endpoint.
 * Returns the access token if successful.
 */
export const login = async (email, password) => {
  // OAuth2 standard uses "username" field, not "email"
  const formData = new URLSearchParams();
  formData.append('username', email);
  formData.append('password', password);

  const response = await apiClient.post('/auth/login', formData, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });

  return response.data;  // { access_token, token_type }
};

/**
 * Register User
 * 
 * Creates a new user account.
 */
export const register = async (userData) => {
  const response = await apiClient.post('/auth/register', userData);
  return response.data;
};

/**
 * Get Current User
 * 
 * Fetches the currently authenticated user's data.
 */
export const getCurrentUser = async () => {
  const response = await apiClient.get('/auth/me');
  return response.data;
};

// Export as default for convenience
export default {
  login,
  register,
  getCurrentUser,
};
