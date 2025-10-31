/**
 * Tournaments Page Component
 * 
 * This page will display a list of all tournaments.
 * It could include:
 *   - List of tournaments (past and upcoming)
 *   - Search and filter functionality
 *   - Create new tournament button
 *   - Link to tournament details
 * 
 * This is a placeholder component. Expand it with actual tournament listing logic.
 */

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import apiClient from '../services/api';

function TournamentsPage() {
  const [tournaments, setTournaments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  /**
   * Fetch tournaments on component mount
   * 
   * useEffect with an empty dependency array [] runs once when the component mounts.
   * This is where you'd fetch data from the API.
   */
  useEffect(() => {
    fetchTournaments();
  }, []);

  const fetchTournaments = async () => {
    try {
      setLoading(true);
      // TODO: Uncomment when backend endpoint is implemented
      // const response = await apiClient.get('/tournaments');
      // setTournaments(response.data);
      
      // Placeholder: Empty array
      setTournaments([]);
    } catch (err) {
      setError('Failed to load tournaments');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="text-center py-12">Loading tournaments...</div>;
  }

  if (error) {
    return <div className="text-center py-12 text-red-600">{error}</div>;
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Tournaments</h1>
        <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors">
          + Create Tournament
        </button>
      </div>

      {/* Tournament List */}
      {tournaments.length === 0 ? (
        <div className="bg-white rounded-lg shadow p-8 text-center">
          <p className="text-gray-600">No tournaments found</p>
          <p className="text-sm text-gray-500 mt-2">
            Create your first tournament to get started
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {tournaments.map((tournament) => (
            <Link
              key={tournament.id}
              to={`/tournaments/${tournament.id}`}
              className="bg-white rounded-lg shadow p-6 hover:shadow-lg transition-shadow"
            >
              <h3 className="text-xl font-semibold mb-2">{tournament.name}</h3>
              <p className="text-gray-600 text-sm mb-4">{tournament.description}</p>
              <div className="flex justify-between text-sm text-gray-500">
                <span>{tournament.location}</span>
                <span>{new Date(tournament.start_date).toLocaleDateString()}</span>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}

export default TournamentsPage;
