/**
 * Reports Service
 * API calls for generating reports
 */

import apiClient from './api';

export const getAttendanceReport = async (from, to, site = null) => {
  const params = { from, to };
  if (site) params.site = site;
  
  const response = await apiClient.get('/reports/attendance', {
    params,
    responseType: 'blob', // Important for downloading files
  });
  
  // Create a download link
  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', `attendance-report-${from}-to-${to}.csv`);
  document.body.appendChild(link);
  link.click();
  link.remove();
  
  return response.data;
};

export default {
  getAttendanceReport,
};
