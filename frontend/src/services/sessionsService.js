/**
 * Sessions Service
 * API calls for managing sessions and attendance
 */

import apiClient from './api';

export const getSessions = async (date = null) => {
  const params = date ? { date } : {};
  const response = await apiClient.get('/sessions', { params });
  return response.data;
};

export const createSession = async (sessionData) => {
  const response = await apiClient.post('/sessions', sessionData);
  return response.data;
};

export const saveAttendance = async (sessionId, attendance) => {
  const response = await apiClient.post(`/sessions/${sessionId}/attendance`, {
    attendance,
  });
  return response.data;
};

export default {
  getSessions,
  createSession,
  saveAttendance,
};
