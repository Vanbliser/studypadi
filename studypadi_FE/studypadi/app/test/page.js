"use client";
import { useState, useEffect } from 'react';
import DashboardLayout from '../dashboard/dashboardLayout';
import '../quiz/quiz.css';

const RevisionTestConfig = () => {
    const handleFileUpload = async (event) => {
      const file = event.target.files[0];
      if (file && file.size < 5 * 1024 * 1024) { // Limit size to 5 MB
        const content = await readFile(file);
        // Send file content to server for question generation
      }
    };
  
    return (
      <DashboardLayout>
        <div className="revision-test-config dark-theme">
          <h1>Revision Test Setup</h1>
          <input type="file" accept=".pdf,.txt" onChange={handleFileUpload} />
          <form>
            <label>Number of Questions</label>
            <input type="number" />
  
            <label>Time Allocation (in minutes)</label>
            <input type="number" />
  
            <button type="submit">Generate Revision Test</button>
          </form>
        </div>
      </DashboardLayout>
    );
  };
  
  export default RevisionTestConfig;
  