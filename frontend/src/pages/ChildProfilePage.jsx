/**
 * Child Profile Page Component
 * 
 * This page will display a list of child profiles for the current user (parent).
 * It could include:
 *   - List of child profiles
 *   - Create new profile button
 *   - View/edit profile details
 *   - Link to LSAS assessments
 * 
 * This is a placeholder component. Expand it with actual profile listing logic.
 */

import React, { useState, useEffect } from 'react';
import apiClient from '../services/api';

function ChildProfilePage() {
  const [profiles, setProfiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchProfiles();
  }, []);

  const fetchProfiles = async () => {
    try {
      setLoading(true);
      // TODO: Uncomment when backend endpoint is implemented
      // const response = await apiClient.get('/profiles');
      // setProfiles(response.data);
      
      // Placeholder: Empty array
      setProfiles([]);
    } catch (err) {
      setError('Failed to load profiles');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="text-center py-12">Loading profiles...</div>;
  }

  if (error) {
    return <div className="text-center py-12 text-red-600">{error}</div>;
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Child Profiles</h1>
        <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors">
          + Create Profile
        </button>
      </div>

      {/* Profile List */}
      {profiles.length === 0 ? (
        <div className="bg-white rounded-lg shadow p-8 text-center">
          <p className="text-gray-600">No profiles found</p>
          <p className="text-sm text-gray-500 mt-2">
            Create your first child profile to get started
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {profiles.map((profile) => (
            <div
              key={profile.id}
              className="bg-white rounded-lg shadow p-6 hover:shadow-lg transition-shadow"
            >
              <h3 className="text-xl font-semibold mb-2">{profile.name}</h3>
              <p className="text-gray-600 text-sm mb-4">
                Born: {new Date(profile.date_of_birth).toLocaleDateString()}
              </p>
              <button className="w-full px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded transition-colors">
                View Details
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ChildProfilePage;
