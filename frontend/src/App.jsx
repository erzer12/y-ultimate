import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import Tournament from './pages/Tournament';
import ChildProfile from './pages/ChildProfile';
import Login from './pages/Login';

// Create a client for React Query
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen bg-gray-50">
          <Navbar />
          <Routes>
            {/* Public Routes - No authentication required */}
            <Route path="/" element={<Dashboard />} />
            <Route path="/tournaments" element={<Tournament />} />
            <Route path="/about" element={<Dashboard />} />
            <Route path="/login" element={<Login />} />
            
            {/* Protected Routes - Authentication required (can be wrapped with ProtectedRoute later) */}
            <Route path="/children" element={<ChildProfile />} />
            <Route path="/children/:profileId" element={<ChildProfile />} />
            <Route path="/sessions" element={<Dashboard />} />
            <Route path="/analytics" element={<Dashboard />} />
            <Route path="/profile" element={<Dashboard />} />
          </Routes>
        </div>
      </Router>
    </QueryClientProvider>
  );
}

export default App;
