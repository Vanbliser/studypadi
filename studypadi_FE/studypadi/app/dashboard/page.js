'use client';
import React, { useState } from 'react';
import './dashboard.css';
import useAuthStore from '../store/authStore';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';



import  Sidebar  from './sidebar';


const ThirdColumn = () => (
    <div className="third-column">
      <div className="calendar">
        <h3>Week Overview</h3>
        <Calendar view="week" />
      </div>
      <div className="recent-uploads">
        <h3>Recent Uploads</h3>
        <p>Recent files or resources will appear here.</p>
      </div>
    </div>
  );


const Dashboard = () => {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <div className="dashboard">
      {/* Sidebar Section */}
      {/*<aside className={`sidebar ${sidebarOpen ? 'open' : 'closed'}`}>
        <button className="sidebar-toggle" onClick={toggleSidebar}>
          {sidebarOpen ? '←' : '→'}
        </button>
        <nav>
          <ul>
            <li><a href="#dashboard">Dashboard</a></li>
            <li><a href="#modules">Modules</a></li>
            <li><a href="#quizzes">Quizzes</a></li>
            <li><a href="#settings">Settings</a></li>
            {/* Additional links as needed 
          </ul>
        </nav>
      </aside>*/}
        <Sidebar />

      {/* Main Content Section */}
      <main className="main-content">
        {/* Column 2 */}
        <section className="main-column">
          <div className="search-bar">
            <input type="text" placeholder="Search..." />
          </div>

          <h2>Hello!, {useAuthStore((state) => state.login.firstName)}</h2>
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

        {/* Column 3 */}
        <aside className="third-column">
          <div className="calendar">
            <Calendar />
            {/* Calendar would be implemented here */}
            <h3>Week Overview</h3>
          </div>
          <div className="recent-uploads">
            <h3>Recent Uploads</h3>
            {/* List of recent uploads would go here */}
          </div>
        </aside>
      </main>
    </div>
  );
};

export default Dashboard;
