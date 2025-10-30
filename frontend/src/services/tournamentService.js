/**
 * Tournament Service
 * 
 * This file will contain all tournament-related API calls.
 * It provides a clean interface for tournament operations.
 * 
 * Functions to implement:
 *   - getTournaments(): Fetch all tournaments
 *   - getTournament(id): Fetch a specific tournament by ID
 *   - createTournament(data): Create a new tournament
 *   - updateTournament(id, data): Update an existing tournament
 *   - deleteTournament(id): Delete a tournament
 */

import apiClient from './api';

/**
 * Get All Tournaments
 * 
 * Fetches a list of all tournaments.
 */
export const getTournaments = async () => {
  const response = await apiClient.get('/tournaments');
  return response.data;
};

/**
 * Get Tournament by ID
 * 
 * Fetches details of a specific tournament.
 */
export const getTournament = async (id) => {
  const response = await apiClient.get(`/tournaments/${id}`);
  return response.data;
};

/**
 * Create Tournament
 * 
 * Creates a new tournament.
 */
export const createTournament = async (data) => {
  const response = await apiClient.post('/tournaments', data);
  return response.data;
};

/**
 * Update Tournament
 * 
 * Updates an existing tournament.
 */
export const updateTournament = async (id, data) => {
  const response = await apiClient.put(`/tournaments/${id}`, data);
  return response.data;
};

/**
 * Delete Tournament
 * 
 * Deletes a tournament.
 */
export const deleteTournament = async (id) => {
  const response = await apiClient.delete(`/tournaments/${id}`);
  return response.data;
};

// Export as default for convenience
export default {
  getTournaments,
  getTournament,
  createTournament,
  updateTournament,
  deleteTournament,
};
