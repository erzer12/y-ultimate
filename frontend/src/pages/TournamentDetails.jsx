/**
 * Tournament Details Page Component
 * 
 * This page will display detailed information about a specific tournament.
 * The tournament ID is extracted from the URL (e.g., /tournaments/123).
 * 
 * It could include:
 *   - Tournament information (name, location, dates)
 *   - List of participating teams
 *   - Scores and standings
 *   - Edit tournament button (for owners)
 * 
 * This is a placeholder component. Expand it with actual tournament detail logic.
 */

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import apiClient from '../services/api';

function TournamentDetails() {
  // Extract the 'id' parameter from the URL
  // For URL /tournaments/123, params.id will be '123'
  const { id } = useParams();
  
  const navigate = useNavigate();
  
  const [tournament, setTournament] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchTournamentDetails();
  }, [id]);

  const fetchTournamentDetails = async () => {
    try {
      setLoading(true);
      // TODO: Uncomment when backend endpoint is implemented
      // const response = await apiClient.get(`/tournaments/${id}`);
      // setTournament(response.data);
      
      // Placeholder: Show error for now
      setError('Tournament details not yet implemented');
    } catch (err) {
      setError('Failed to load tournament details');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="text-center py-12">Loading tournament details...</div>;
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-red-600 mb-4">{error}</p>
        <button
          onClick={() => navigate('/tournaments')}
          className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg"
        >
          Back to Tournaments
        </button>
      </div>
    );
  }

  return (
    <div>
      <button
        onClick={() => navigate('/tournaments')}
        className="mb-6 text-blue-600 hover:underline"
      >
        ← Back to Tournaments
      </button>

      {tournament && (
        <div className="bg-white rounded-lg shadow p-6">
          <h1 className="text-3xl font-bold text-gray-800 mb-4">
            {tournament.name}
          </h1>
          <p className="text-gray-600 mb-6">{tournament.description}</p>
          
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <span className="font-medium">Location:</span> {tournament.location}
            </div>
            <div>
              <span className="font-medium">Start Date:</span>{' '}
              {new Date(tournament.start_date).toLocaleDateString()}
            </div>
            <div>
              <span className="font-medium">End Date:</span>{' '}
              {new Date(tournament.end_date).toLocaleDateString()}
            </div>
            <div>
              <span className="font-medium">Status:</span>{' '}
              {tournament.is_active ? 'Active' : 'Inactive'}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default TournamentDetails;
