import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ChildProfile = () => {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    // Hardcoding profile_id for now
    const profile_id = 1;
    axios.get(`/api/v1/profiles/${profile_id}`)
      .then(response => {
        setProfile(response.data);
      })
      .catch(error => {
        console.error('Error fetching child profile:', error);
      });
  }, []);

  if (!profile) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Child Profile</h1>
      <p>Name: {profile.name}</p>
      <p>Date of Birth: {profile.date_of_birth}</p>
      <p>School: {profile.school}</p>
      <p>Community: {profile.community}</p>
    </div>
  );
};

export default ChildProfile;
