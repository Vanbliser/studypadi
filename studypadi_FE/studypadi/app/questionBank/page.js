'use client';
import React, { useState } from 'react';

import useAuthStore from '../store/authStore';
import { useRouter } from 'next/navigation';
import DashboardLayout from "../dashboard/dashboardLayout";
import './question.css';

//const QuestionBank = () => (
//    <DashboardLayout>
//
//
//    </DashboardLayout>
//);



const FileUploadAndTable = () => {
    const [data, setData] = useState([]);
  
    const handleFileUpload = (event) => {
      const file = event.target.files[0];
      if (!file) return;
  
      const reader = new FileReader();
      reader.onload = (e) => {
        const content = e.target.result;
        const parsedData = parseFileContent(content);
        setData(parsedData);
      };
  
      reader.readAsText(file);
    };
  
    const parseFileContent = (content) => {
      const rows = content.split('\n');
      return rows.map((row, index) => {
        const cells = row.split(',');
        return {
          sn: index + 1,
          question: cells[0] || '',
          correctAnswer: cells[1] || '',
          wrongAnswer1: cells[2] || '',
          wrongAnswer2: cells[3] || '',
          wrongAnswer3: cells[4] || '',
          difficultyLevel: cells[5] || 'Easy',
        };
      });
    };
  
    const handleSave = async () => {
      try {
        await fetch('/api/save-questions', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ questions: data }),
        });
        alert('Questions saved successfully!');
      } catch (error) {
        console.error('Error saving questions:', error);
      }
    };
  
    return (
      <DashboardLayout>
        <div>
          <input type="file" accept=".txt, .csv" onChange={handleFileUpload} />
          <table className='questionsForUpload'>
            <thead>
              <tr>
                <th>SN</th>
                <th>Question</th>
                <th>Correct Answer</th>
                <th>Wrong Answer 1</th>
                <th>Wrong Answer 2</th>
                <th>Wrong Answer 3</th>
                <th>Difficulty Level</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item, index) => (
                <tr key={index}>
                  <td>{item.sn}</td>
                  <td contentEditable>{item.question}</td>
                  <td contentEditable>{item.correctAnswer}</td>
                  <td contentEditable>{item.wrongAnswer1}</td>
                  <td contentEditable>{item.wrongAnswer2}</td>
                  <td contentEditable>{item.wrongAnswer3}</td>
                  <td contentEditable>{item.difficultyLevel}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <button className='saveToDB' onClick={handleSave}>Save</button>
        </div>
      </DashboardLayout>
    );
  };
  
  export default FileUploadAndTable;