/**
 * Main App Component
 * MVP version with minimal routing
 */

import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import LoginPage from './pages/LoginPage';
import CoachSessionsPage from './pages/CoachSessionsPage';
import SessionAttendancePage from './pages/SessionAttendancePage';
import ManagerChildrenPage from './pages/ManagerChildrenPage';
import AdminImportPage from './pages/AdminImportPage';

// Legacy pages (from existing app)
import Dashboard from './pages/Dashboard';
import TournamentsPage from './pages/TournamentsPage';
import TournamentDetails from './pages/TournamentDetails';
import ChildProfilePage from './pages/ChildProfilePage';

function App() {
  return (
    <AuthProvider>
      <Routes>
        {/* Root route */}
        <Route path="/" element={<Navigate to="/login" replace />} />
        
        {/* Authentication */}
        <Route path="/login" element={<LoginPage />} />
        
        {/* MVP Pages */}
        <Route path="/coach/sessions" element={<CoachSessionsPage />} />
        <Route path="/coach/sessions/:id/attendance" element={<SessionAttendancePage />} />
        <Route path="/manager/children" element={<ManagerChildrenPage />} />
        <Route path="/admin/import" element={<AdminImportPage />} />
        
        {/* Legacy Pages (from existing app) */}
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/tournaments" element={<TournamentsPage />} />
        <Route path="/tournaments/:id" element={<TournamentDetails />} />
        <Route path="/profiles" element={<ChildProfilePage />} />
        
        {/* 404 */}
        <Route path="*" element={<div>404 - Page Not Found</div>} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
