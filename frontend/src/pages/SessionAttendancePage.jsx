import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import * as sessionsService from '../services/sessionsService';
import * as childrenService from '../services/childrenService';

function SessionAttendancePage() {
  const { id } = useParams();
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  
  const [session, setSession] = useState(null);
  const [children, setChildren] = useState([]);
  const [attendance, setAttendance] = useState({});
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    fetchData();
  }, [id]);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [sessionsData, childrenData] = await Promise.all([
        sessionsService.getSessions(),
        childrenService.getChildren(),
      ]);

      const currentSession = sessionsData.find((s) => s.id === parseInt(id, 10));
      setSession(currentSession);

      // Filter children by session site
      const siteChildren = childrenData.filter(
        (child) => child.siteId === currentSession?.siteId
      );
      setChildren(siteChildren);

      // Initialize attendance from existing records
      const attendanceMap = {};
      currentSession?.attendance?.forEach((record) => {
        attendanceMap[record.childId] = {
          present: record.present,
          notes: record.notes || '',
        };
      });
      setAttendance(attendanceMap);

      setError('');
    } catch (err) {
      setError('Failed to load session data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const toggleAttendance = (childId) => {
    setAttendance((prev) => ({
      ...prev,
      [childId]: {
        present: !prev[childId]?.present,
        notes: prev[childId]?.notes || '',
      },
    }));
  };

  const handleNotesChange = (childId, notes) => {
    setAttendance((prev) => ({
      ...prev,
      [childId]: {
        present: prev[childId]?.present || false,
        notes,
      },
    }));
  };

  const handleSave = async () => {
    try {
      setSaving(true);
      setError('');
      setSuccess('');

      // Convert attendance object to array format
      const attendanceArray = Object.entries(attendance).map(([childId, data]) => ({
        childId: parseInt(childId, 10),
        present: data.present,
        notes: data.notes || null,
      }));

      await sessionsService.saveAttendance(parseInt(id, 10), attendanceArray);
      setSuccess('Attendance saved successfully!');
      
      setTimeout(() => {
        navigate('/coach/sessions');
      }, 1500);
    } catch (err) {
      setError('Failed to save attendance');
      console.error(err);
    } finally {
      setSaving(false);
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="text-gray-600">Loading session...</div>
      </div>
    );
  }

  if (!session) {
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="text-red-600">Session not found</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <div className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-900">Mark Attendance</h1>
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
          <button
            onClick={() => navigate('/coach/sessions')}
            className="text-blue-600 hover:text-blue-800 mb-4"
          >
            ← Back to Sessions
          </button>
          
          <h2 className="text-xl font-semibold text-gray-800 mb-2">
            {session.site.name}
          </h2>
          <p className="text-gray-600">{formatDate(session.date)}</p>
          {session.notes && (
            <p className="text-sm text-gray-500 mt-2">{session.notes}</p>
          )}
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}

        {success && (
          <div className="mb-4 p-3 bg-green-100 border border-green-400 text-green-700 rounded">
            {success}
          </div>
        )}

        <div className="bg-white rounded-lg shadow overflow-hidden">
          <div className="px-6 py-4 bg-gray-50 border-b border-gray-200">
            <h3 className="text-lg font-medium text-gray-900">
              Children at {session.site.name} ({children.length})
            </h3>
          </div>

          <div className="divide-y divide-gray-200">
            {children.map((child) => (
              <div key={child.id} className="px-6 py-4 hover:bg-gray-50">
                <div className="flex items-center justify-between">
                  <div className="flex-1">
                    <h4 className="text-base font-medium text-gray-900">
                      {child.firstName} {child.lastName}
                    </h4>
                  </div>
                  
                  <div className="flex items-center gap-4">
                    <button
                      onClick={() => toggleAttendance(child.id)}
                      className={`px-6 py-2 rounded-md font-medium transition-colors ${
                        attendance[child.id]?.present
                          ? 'bg-green-600 text-white hover:bg-green-700'
                          : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                      }`}
                    >
                      {attendance[child.id]?.present ? 'Present' : 'Absent'}
                    </button>
                  </div>
                </div>
                
                <div className="mt-2">
                  <input
                    type="text"
                    placeholder="Notes (optional)"
                    value={attendance[child.id]?.notes || ''}
                    onChange={(e) => handleNotesChange(child.id, e.target.value)}
                    className="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
              </div>
            ))}
          </div>

          <div className="px-6 py-4 bg-gray-50 border-t border-gray-200">
            <div className="flex justify-between items-center">
              <div className="text-sm text-gray-600">
                Present: {Object.values(attendance).filter((a) => a.present).length} / {children.length}
              </div>
              <button
                onClick={handleSave}
                disabled={saving}
                className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
              >
                {saving ? 'Saving...' : 'Save Attendance'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SessionAttendancePage;
