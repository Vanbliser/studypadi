// /quiz configuration form
"use client";
import { useState, useEffect } from 'react';
import DashboardLayout from '../dashboard/dashboardLayout';
import './quiz.css';

const QuizConfig = () => {
  const [modules, setModules] = useState([]);
  const [submodules, setSubmodules] = useState([]);
  const [sections, setSections] = useState([]);
  const [quizzes, setQuizzes] = useState([]);
  const [selectedModule, setSelectedModule] = useState('');
  const [selectedSubmodule, setSelectedSubmodule] = useState('');
  const [selectedSection, setSelectedSection] = useState('');
  const [quizType, setQuizType] = useState('past');
  const [algorithm, setAlgorithm] = useState('random');
  const [instantCorrection, setInstantCorrection] = useState(false);
  const [quizId, setQuizId] = useState('');
  const [quizName, setQuizName] = useState('');

  useEffect(() => {
    
  }, []);

  useEffect(() => {
    // Fetch submodules when a module is selected
    if (selectedModule) fetchSubmodules(selectedModule);
  }, [selectedModule]);

  useEffect(() => {
    // Fetch sections when a submodule is selected
    if (selectedSubmodule) fetchSections(selectedSubmodule);
  }, [selectedSubmodule]);

  useEffect(() => {
    // Fetch quizzes when section and module selections are updated
    if (selectedSection && selectedModule && selectedSubmodule) fetchQuizzes(selectedModule, selectedSubmodule, selectedSection);
  }, [selectedSection, selectedModule, selectedSubmodule]);

  const fetchModules = async () => {
    // Fetch modules from the API
    const response = await fetch('/api/modules');
    const data = await response.json();
    setModules(data);
  };

  const fetchSubmodules = async (moduleId) => {
    // Fetch submodules based on selected module
    const response = await fetch(`/api/submodules?module=${moduleId}`);
    const data = await response.json();
    setSubmodules(data);
  };

  const fetchSections = async (submoduleId) => {
    // Fetch sections based on selected submodule
    const response = await fetch(`/api/sections?submodule=${submoduleId}`);
    const data = await response.json();
    setSections(data);
  };

  const fetchQuizzes = async (moduleId, submoduleId, sectionId) => {
    // Fetch quizzes based on module, submodule, and section
    const response = await fetch(`/api/quizzes?module=${moduleId}&submodule=${submoduleId}&section=${sectionId}`);
    const data = await response.json();
    setQuizzes(data);
  };

  const handleSubmit == () => {
    // Submit form and navigate to quiz page with chosen quiz ID
    // Add navigation logic here to route to the quiz page with `quizId`
  };

  return (
    <DashboardLayout>
      <div className="quiz-config-container dark-theme">
        <h1>Select Quiz Configuration</h1>
        <form onSubmit={handleSubmit} className="quiz-form">
          <label>Module</label>
          <select value={selectedModule} onChange={e => setSelectedModule(e.target.value)}>
            <option value="">Select Module</option>
            {modules.map(module => (
              <option key={module.id} value={module.id}>{module.name}</option>
            ))}
          </select>

          <label>Submodule</label>
          <select value={selectedSubmodule} onChange={e => setSelectedSubmodule(e.target.value)}>
            <option value="">Select Submodule</option>
            {submodules.map(submodule => (
              <option key={submodule.id} value={submodule.id}>{submodule.name}</option>
            ))}
          </select>

          <label>Section</label>
          <select value={selectedSection} onChange={e => setSelectedSection(e.target.value)}>
            <option value="">Select Section</option>
            {sections.map(section => (
              <option key={section.id} value={section.id}>{section.name}</option>
            ))}
          </select>

          <label>Quiz Type</label>
          <select value={quizType} onChange={e => setQuizType(e.target.value)}>
            <option value="past">Past Quiz</option>
            <option value="special">Educator Special</option>
          </select>

          <label>Question Generation Algorithm</label>
          <select value={algorithm} onChange={e => setAlgorithm(e.target.value)}>
            <option value="random">Random</option>
            <option value="leastAttempted">Least Attempted</option>
            <option value="mostFailed">Most Failed</option>
            <option value="neverAttempted">Never Attempted</option>
          </select>

          <label>Instant Correction</label>
          <input
            type="checkbox"
            checked={instantCorrection}
            onChange={() => setInstantCorrection(!instantCorrection)}
          />

          <label>Quiz Name</label>
          <select value={quizName} onChange={e => setQuizName(e.target.value)}>
            <option value="">Select Quiz</option>
            {quizzes.map(quiz => (
              <option key={quiz.id} value={quiz.id}>{quiz.name}</option>
            ))}
          </select>

          <label>Quiz ID</label>
          <input type="text" value={quizId} readOnly />

          <button type="submit">Start Quiz</button>
        </form>
      </div>
    </DashboardLayout>
  );
};

export default QuizConfig;