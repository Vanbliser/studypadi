'use client';
import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faBook, faQuestionCircle, faCog } from '@fortawesome/free-solid-svg-icons';

const Sidebar = () => {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <aside className={`sidebar ${sidebarOpen ? 'open' : 'closed'}`}>
      <button className="sidebar-toggle" onClick={toggleSidebar}>
        {sidebarOpen ? '←' : '→'}
      </button>
      <nav>
        <ul>
          <li>
            <a href="#dashboard">
              <FontAwesomeIcon icon={faHome} />
              <span>Dashboard</span>
            </a>
          </li>
          <li>
            <a href="#modules">
              <FontAwesomeIcon icon={faBook} />
              <span>Modules</span>
            </a>
          </li>
          <li>
            <a href="#quizzes">
              <FontAwesomeIcon icon={faQuestionCircle} />
              <span>Quizzes</span>
            </a>
          </li>
          <li>
            <a href="#settings">
              <FontAwesomeIcon icon={faCog} />
              <span>Settings</span>
            </a>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
