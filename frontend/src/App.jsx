/**
 * Main App Component
 * 
 * This is the root component of the React application.
 * It handles:
 *   1. Global state (via AuthProvider)
 *   2. Layout structure (Sidebar + main content)
 *   3. Routing (which component to render based on URL)
 * 
 * Component hierarchy:
 *   <App>
 *     <AuthProvider>    <- Provides auth state to all children
 *       <Sidebar>       <- Navigation sidebar
 *       <main>          <- Main content area
 *         <Routes>      <- React Router renders the appropriate page
 *           <Route>     <- Individual routes (LoginPage, Dashboard, etc.)
 */

import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Sidebar from './components/layout/Sidebar';
import Navbar from './components/layout/Navbar';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import TournamentsPage from './pages/TournamentsPage';
import TournamentDetails from './pages/TournamentDetails';
import ChildProfilePage from './pages/ChildProfilePage';

function App() {
  return (
    /**
     * AuthProvider wraps the entire app
     * 
     * This provides authentication state (user, login, logout, etc.) to all
     * child components. Any component can access auth state using useAuth().
     */
    <AuthProvider>
      <div className="flex h-screen bg-gray-100">
        {/* 
          Sidebar Component
          
          The sidebar provides navigation links and is visible on all pages.
          It's positioned on the left side of the screen.
        */}
        <Sidebar />

        {/* 
          Main Content Area
          
          This is where the page content is rendered based on the current route.
          The "flex-1" class makes this take up all remaining space after the sidebar.
        */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* 
            Navbar Component (optional)
            
            A top navigation bar that could contain user info, notifications, etc.
          */}
          <Navbar />

          {/* 
            Main Content Container
            
            This scrollable container holds the actual page content.
          */}
          <main className="flex-1 overflow-y-auto p-6">
            {/*
              React Router Routes
              
              <Routes> is the container for all route definitions.
              <Route> defines a single route (URL path -> Component).
              
              How it works:
                - User navigates to "/dashboard"
                - React Router finds the matching <Route path="/dashboard">
                - It renders the specified element (<Dashboard />)
                - The URL changes WITHOUT a full page reload
              
              Why <Link> instead of <a>?
                - <a href="/dashboard"> causes a full page reload
                - <Link to="/dashboard"> uses React Router's client-side navigation
                - This keeps the app fast and preserves state
            */}
            <Routes>
              {/* 
                Root route: Redirect to dashboard
                
                When user visits "/", redirect them to "/dashboard"
              */}
              <Route path="/" element={<Navigate to="/dashboard" replace />} />
              
              {/* Authentication */}
              <Route path="/login" element={<LoginPage />} />
              
              {/* Main Pages */}
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/tournaments" element={<TournamentsPage />} />
              <Route path="/tournaments/:id" element={<TournamentDetails />} />
              <Route path="/profiles" element={<ChildProfilePage />} />
              
              {/* 
                Catch-all route: 404 Not Found
                
                If no route matches, show a 404 page.
                The "*" path matches any URL that hasn't been matched yet.
              */}
              <Route path="*" element={<div>404 - Page Not Found</div>} />
            </Routes>
          </main>
        </div>
      </div>
    </AuthProvider>
  );
}

export default App;
