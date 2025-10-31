import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import * as sessionsService from '../services/sessionsService';

function CoachSessionsPage() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [sessions, setSessions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedDate, setSelectedDate] = useState('');

  useEffect(() => {
    fetchSessions();
  }, [selectedDate]);

  const fetchSessions = async () => {
    try {
      setLoading(true);
      const data = await sessionsService.getSessions(selectedDate || null);
      setSessions(data);
      setError('');
    } catch (err) {
      setError('Failed to load sessions');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSessionClick = (sessionId) => {
    navigate(`/coach/sessions/${sessionId}/attendance`);
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <div className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-900">Y-Ultimate - Coach Dashboard</h1>
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-600">
              {user?.name} ({user?.role})
            </span>
            <button
              onClick={logout}
              className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
            >
              Logout
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="mb-6">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">Training Sessions</h2>
          
          {/* Date Filter */}
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Filter by Date (optional)
            </label>
            <input
              type="date"
              value={selectedDate}
              onChange={(e) => setSelectedDate(e.target.value)}
              className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}

        {loading ? (
          <div className="text-center py-8">
            <div className="text-gray-600">Loading sessions...</div>
          </div>
        ) : sessions.length === 0 ? (
          <div className="bg-white rounded-lg shadow p-8 text-center text-gray-600">
            No sessions found.
          </div>
        ) : (
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {sessions.map((session) => (
              <div
                key={session.id}
                onClick={() => handleSessionClick(session.id)}
                className="bg-white rounded-lg shadow hover:shadow-lg transition-shadow cursor-pointer p-6"
              >
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  {session.site.name}
                </h3>
                <p className="text-sm text-gray-600 mb-2">
                  {formatDate(session.date)}
                </p>
                {session.notes && (
                  <p className="text-sm text-gray-500 mb-3">{session.notes}</p>
                )}
                <div className="text-sm text-blue-600 font-medium">
                  {session.attendance?.length || 0} attendance records
                </div>
                <div className="mt-4 text-sm text-gray-500">
                  Click to mark attendance
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default CoachSessionsPage;
