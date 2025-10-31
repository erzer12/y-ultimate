/**
 * Authentication Service
 * 
 * API calls for authentication with the Node.js backend.
 */

import apiClient from './api';

/**
 * Login User
 * Returns JWT token and user data
 */
export const login = async (email, password) => {
  const response = await apiClient.post('/auth/login', {
    email,
    password,
  });

  return response.data;  // { token, user: { id, email, name, role } }
};

/**
 * Get Current User
 * Not currently implemented in backend, but can be added later
 */
export const getCurrentUser = async () => {
  // For now, retrieve from localStorage
  const userStr = localStorage.getItem('user');
  return userStr ? JSON.parse(userStr) : null;
};

export default {
  login,
  getCurrentUser,
};
