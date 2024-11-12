// app/dashboard/page.js
'use client';
import React, { useState } from 'react';
import DashboardLayout from './dashboardLayout';
import './dashboard.css';
import useAuthStore from '../store/authStore';
import { useRouter } from 'next/navigation';
//import axios from 'axios'; // For making API requests

const SecondaryColumn = () => (
  <div className="secondaryColumn">
    <div className='stats'>
      <div className='stat_time'>
        <h3> Best Time Average </h3>
        <p>00:00:00</p>
      </div>
      <div className='stat_score'>
        <h3>Best Score Average</h3>
        <p>0%</p>
      </div>
    </div>
    <div className="recent-uploads">
      <h3>Recent Uploads</h3>
      <p>Recent files or resources will appear here.</p>
    </div>
  </div>
);

const Dashboard = () => {
  const router = useRouter();
  const firstName = useAuthStore((state) => state.firstName); // Access firstName directly
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  // Function to handle search
  const handleSearch = async () => {
    if (!searchTerm.trim()) return; // Prevent empty search

    setIsLoading(true);
//    try {
//      // Make an API call to fetch search results
//      const response = await axios.get(`/api/search?query=${searchTerm}`);
//      setSearchResults(response.data.results);
//    } catch (error) {
//      console.error('Error fetching search results:', error);
//    } finally {
//      setIsLoading(false);
//    }
  };
//
  // Handle Enter key press for search
  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <DashboardLayout>
      {/* Page-specific content */}
      <div className="dashboardContent">
        {/* Main column Section */}
        <section className="main-column">
          <div className="search-bar">
            <input
              type="text"
              placeholder="Search..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              onKeyPress={handleKeyPress}
            />
            <button onClick={handleSearch} disabled={isLoading}>
              {isLoading ? 'Searching...' : 'Search'}
            </button>
          </div>

          <h2 className='hello'>Hello!, {firstName}</h2>
          <div className="greeting-section">
            <p>If you need help, refer to the <a href="#help">help section</a>.</p>
          </div>

          <h3>My Quizzes</h3>
          <div className="recent-quizzes">
            {/* Display search results */}
            {searchResults.length > 0 && (
              <div className="search-results">
                {searchResults.map((result, index) => (
                  <div key={index} className="result-item">
                    <h4>{result.title}</h4>
                    <p>{result.description}</p>
                  </div>
                ))}
              </div>
            )}
          </div>

          <h3>Recent Modules</h3>
          <div className="recent-modules">
            {/* Module items would go here */}
          </div>
        </section>

        {/* side content Section */}
        <SecondaryColumn />
      </div>
    </DashboardLayout>
  );
};

export default Dashboard;
