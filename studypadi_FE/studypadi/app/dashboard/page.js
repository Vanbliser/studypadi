// app/dashboard/page.js
'use client';
import React, { useState } from 'react';
import './dashboard.css';
import useAuthStore from '../store/authStore';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';  
import { useRouter } from 'next/navigation';



import  Sidebar  from './sidebar';


const ThirdColumn = () => (
    <div className="third-column">
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
  

  const [sidebarOpen, setSidebarOpen] = useState(true);

  const firstName = useAuthStore((state) => state.firstName); // Access firstName directly


  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <div className="dashboard">
      {/* Sidebar */}
        <Sidebar />

      {/* Main Content Section */}
      <main className="main-content">
        
        {/* Column 2 */}
        <section className="main-column">
          <div className="search-bar">
            <input type="text" placeholder="Search..." />
          </div>

          <h2 className='hello'>Hello!, {firstName}</h2>
          <div className="greeting-section">
            <p>If you need help, refer to the <a href="#help">help section</a>.</p>
          </div>

          <h3>My Quizzes</h3>
          <div className="recent-quizzes">
            {/* Quiz items would go here */}
          </div>

          <h3>Recent Modules</h3>
          <div className="recent-modules">
            
            {/* Module items would go here */}
          </div>
        </section>
        < ThirdColumn />

        
      </main>
    </div>
  );
};

export default Dashboard;
