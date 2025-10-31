/**
 * Children Service
 * API calls for managing children
 */

import apiClient from './api';

export const getChildren = async () => {
  const response = await apiClient.get('/children');
  return response.data;
};

export const createChild = async (childData) => {
  const response = await apiClient.post('/children', childData);
  return response.data;
};

export const importChildren = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  
  const response = await apiClient.post('/children/import', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  
  return response.data;
};

export default {
  getChildren,
  createChild,
  importChildren,
};
