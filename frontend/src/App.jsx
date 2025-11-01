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
            <Route path="/" element={<Dashboard />} />
            <Route path="/tournaments" element={<Tournament />} />
            <Route path="/children/:profileId" element={<ChildProfile />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </div>
      </Router>
    </QueryClientProvider>
  );
}

export default App;
