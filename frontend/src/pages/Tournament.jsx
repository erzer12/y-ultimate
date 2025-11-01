import React from 'react';

const Tournament = () => {
  return (
    <div>
      <h1>Tournaments</h1>
      <p>This page will display a list of upcoming and past tournaments. Users will be able to view tournament details, register for events, and see results.</p>
      {/* Placeholder for tournament list */}
      <div className="tournament-list">
        <div className="tournament-item">
          <h3>Tournament 1</h3>
          <p>Date: 2024-08-15</p>
          <p>Location: City Park</p>
          <button>View Details</button>
        </div>
        <div className="tournament-item">
          <h3>Tournament 2</h3>
          <p>Date: 2024-09-10</p>
          <p>Location: State University</p>
          <button>View Details</button>
        </div>
      </div>
    </div>
  );
};

export default Tournament;
