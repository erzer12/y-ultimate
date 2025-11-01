import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const ChildProfile = () => {
  const [profile, setProfile] = useState(null);
  const { profileId } = useParams(); // Assuming you're using React Router with a dynamic route like /child-profile/:profileId

  useEffect(() => {
    // Hardcoded profile_id for now
    const profile_id = 1; 
    
    fetch(`http://localhost:8000/api/v1/profiles/${profile_id}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setProfile(data);
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      });
  }, [profileId]);

  if (!profile) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{profile.name}'s Profile</h1>
      <p>Date of Birth: {profile.date_of_birth}</p>
      <p>School: {profile.school}</p>
      <p>Community: {profile.community}</p>

      {/* This part needs to be adjusted based on how assessments are structured in your API response */}
      {profile.assessments && profile.assessments.length > 0 && (
        <div>
          <h2>Assessments</h2>
          <div className="assessment-list">
            {profile.assessments.map(assessment => (
              <div key={assessment.id} className="assessment-item">
                <h3>Assessment - {assessment.date}</h3>
                <ul>
                  <li>Throwing: {assessment.throwing}</li>
                  <li>Catching: {assessment.catching}</li>
                  <li>Athleticism: {assessment.athleticism}</li>
                </ul>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ChildProfile;
