'use client';
import { useState } from 'react';
import DashboardLayout from '../dashboard/dashboardLayout';
import '../quiz/quiz.css';

const RevisionTestConfig = () => {
  // Function to read file content using FileReader
  const readFile = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = () => reject(reader.error);
      reader.readAsText(file);
    });
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (file && file.size < 5 * 1024 * 1024) { // Limit size to 5 MB
      try {
        const content = await readFile(file);
        console.log('File content:', content); // You can send this content to the server
        // Send file content to server for question generation
      } catch (error) {
        console.error('Error reading file:', error);
      }
    } else {
      alert('Please upload a file smaller than 5 MB');
    }
  };

  return (
    <DashboardLayout>
      <div className="revision-test-config dark-theme">
        <h1>Revision Test Setup</h1>
        <input type="file" accept=".pdf,.txt" onChange={handleFileUpload} />
        <form>
          <label>Number of Questions</label>
          <input type="number" min="1" />

          <label>Time Allocation (in minutes)</label>
          <input type="number" min="1" />

          <button type="submit">Generate Revision Test</button>
        </form>
      </div>
    </DashboardLayout>
  );
};

export default RevisionTestConfig;
