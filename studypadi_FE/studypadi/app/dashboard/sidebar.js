'use client';
import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faBook, faQuestionCircle, faCog } from '@fortawesome/free-solid-svg-icons';


const Sidebar = () => {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  

  return (
    <aside className='sidebar open'>
      {/* Sidebar Header should come here when the Logo is already - remeber pls - */}
     <nav>
          <ul>
            <li>
              <a href="#dashboard">
                <FontAwesomeIcon className='ssvg' icon={faHome} />
                <span>Dashboard</span>
              </a>
              
            </li>
            <hr />
            <li>
              <a href="#modules">
                <FontAwesomeIcon className='ssvg' icon={faBook} />
                <span>Modules</span>
              </a>
            </li>
            <li>
              <a href="#quizzes">
                <FontAwesomeIcon className='ssvg' icon={faQuestionCircle} />
                <span>Quizzes</span>
              </a>
            </li>
            <li>
              <a href="#quizzes">
                <FontAwesomeIcon className='ssvg' icon={faQuestionCircle} />
                <span>Test</span>
              </a>
            </li>
            <hr />
            <li>
              <a href="#settings">
                <FontAwesomeIcon className='ssvg' icon={faCog} />
                <span>Settings</span>
              </a>
            </li>
          </ul>
        </nav>
    </aside>
  );
};

export default Sidebar;
