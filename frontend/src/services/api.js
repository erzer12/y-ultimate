/**
 * API Client - Centralized Axios Configuration
 * 
 * This file creates a pre-configured Axios instance for making HTTP requests
 * to the FastAPI backend. It centralizes all API logic in one place.
 * 
 * Benefits of this approach:
 *   1. DRY (Don't Repeat Yourself): The baseURL is defined once, not in every request
 *   2. Interceptors: We can add authentication headers to every request automatically
 *   3. Error handling: We can handle errors consistently across the entire app
 *   4. Easy testing: We can mock this API client in tests
 */

import axios from 'axios';

/**
 * Create an Axios instance with custom configuration
 * 
 * baseURL: The base URL for all requests
 *   - Instead of writing "http://localhost:8000/api/v1/users" every time,
 *   - You can write apiClient.get("/users")
 *   - Axios will automatically prepend the baseURL
 */
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
  // Timeout after 10 seconds
  timeout: 10000,
});

/**
 * Request Interceptor
 * 
 * CRITICAL CONCEPT: Interceptors run before every request
 * This is where we add the JWT token to the Authorization header
 * 
 * How it works:
 *   1. User logs in and receives a JWT token
 *   2. Token is stored in localStorage (or a state management system)
 *   3. Every subsequent request automatically includes the token
 *   4. The backend validates the token and knows who the user is
 * 
 * Why this is important:
 *   - Without this, you'd have to manually add the token to every request
 *   - This ensures protected routes always have authentication
 *   - If the token is missing or invalid, the backend returns 401 Unauthorized
 */
apiClient.interceptors.request.use(
  (config) => {
    // Get the token from localStorage
    // (This assumes you store the token when the user logs in)
    const token = localStorage.getItem('access_token');
    
    // If a token exists, add it to the Authorization header
    if (token) {
      // Format: "Bearer <token>"
      // "Bearer" is the authentication scheme for JWT tokens
      config.headers.Authorization = `Bearer ${token}`;
    }
    
    return config;
  },
  (error) => {
    // Handle request errors
    return Promise.reject(error);
  }
);

/**
 * Response Interceptor (Optional)
 * 
 * This runs after every response. You can use it to:
 *   - Handle errors globally (e.g., redirect to login on 401)
 *   - Refresh expired tokens automatically
 *   - Log all API responses for debugging
 */
apiClient.interceptors.response.use(
  (response) => {
    // Just return the response data
    return response;
  },
  (error) => {
    // Handle specific error cases
    if (error.response?.status === 401) {
      // Unauthorized - token might be expired
      // Optionally: Clear token and redirect to login
      // localStorage.removeItem('access_token');
      // window.location.href = '/login';
    }
    
    return Promise.reject(error);
  }
);

export default apiClient;
