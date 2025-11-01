import React from 'react';

const Dashboard = () => {
  return (
    <div>
      <h1>Dashboard</h1>
      
      <div className="dashboard-section">
        <h2>Recent Activity</h2>
        <p>This section will display recent updates and activities.</p>
      </div>
      
      <div className="dashboard-section">
        <h2>Key Metrics</h2>
        <p>This section will display important metrics and statistics.</p>
      </div>
      
      <div className="dashboard-section">
        <h2>Upcoming Events</h2>
        <p>This section will display upcoming tournaments and other events.</p>
      </div>
    </div>
  );
};

export default Dashboard;
