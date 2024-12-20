'use client';
import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faBook, faQuestionCircle, faCog ,} from '@fortawesome/free-solid-svg-icons';
import { faDatabase, faListCheck, faChalkboardTeacher } from '@fortawesome/free-solid-svg-icons';
import { usePathname } from 'next/navigation';
import Link from 'next/link';


const Sidebar = () => {
  const pathname = usePathname();

  const isActive = (path) => pathname === path;
  

  return (
    <aside className='sidebar open'>
      {/* Sidebar Header should come here when the Logo is already - remeber pls - */}
     <nav>
          <ul>
            <li className={isActive('#dashboard') ? 'active' : ''}>
              <Link href="/dashboard">
                <FontAwesomeIcon className='ssvg' icon={faHome} />
                <span>Dashboard</span>

              </Link>

              
            </li>
            <hr />
            <li className={isActive('#questionBank') ? 'active' : ''}>
              <Link href="/questionBank">
                <FontAwesomeIcon className='ssvg' icon={faDatabase} />
                <span>Question Bank</span>              

              </Link>
            </li>
            <li className={isActive('#quizzes') ? 'active' : ''}>
              <Link href="/quiz">
                <FontAwesomeIcon className='ssvg' icon={faListCheck} />
                <span>Quizzes</span>

              </Link>
            </li>

            <li className={isActive('#test') ? 'active' : ''}>
              <Link href="/test">
                <FontAwesomeIcon className='ssvg' icon={faChalkboardTeacher} />
                <span>Revision Test</span>


              </Link>
            </li>
            <hr />
            <li className={isActive('#settings') ? 'active' : ''}>
              <Link href="/dashboard">
                <FontAwesomeIcon className='ssvg' icon={faCog} />
                <span>Settings</span>

              </Link>

            </li>
          </ul>
        </nav>
    </aside>
  );
};

export default Sidebar;
