'use client';
import React, { useState } from 'react';
import Sidebar from './sidebar';
import './dashboard.css';
import Header from './header';


const DashboardLayout = ({ children }) => {
    return (
      <>
      <Header />
        <div className="dashboard">
          {/* Sidebar */}
          <Sidebar className='sidebar'/>
    
          {/* Main Content Area */}
          <main className="main-content">
            {children}
          </main>
        </div>
      </>
      );
    };

export default DashboardLayout;