"use client";
import { useState, useEffect } from 'react';
import DashboardLayout from '../dashboard/dashboardLayout';
import './quiz.css';
import { mockData, mockClass, mockQuiz } from '../mockData';
import { useRouter } from 'next/navigation';

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

  const router = useRouter();

  useEffect(() => {
    // Fetch modules from mockData
    fetchModules();
  }, []);

  useEffect(() => {
    // Fetch submodules when a module is selected
    if (selectedModule) fetchSubmodules(selectedModule);
  }, [selectedModule]);

  useEffect(() => {
    // Fetch sections when a submodule is selected
    if (selectedModule && selectedSubmodule) fetchSections(selectedModule, selectedSubmodule);
  }, [selectedSubmodule]);

//  useEffect(() => {
//    // Fetch quizzes when section and module selections are updated
//    if (selectedSection && selectedModule && selectedSubmodule) {
//      fetchQuizzes(selectedModule, selectedSubmodule, selectedSection);
//    }
//  }, [selectedSection, selectedModule, selectedSubmodule]);

  const fetchModules = () => {
    // Fetch modules from mockData
    const data = mockClass.modules.map((modules) => ({
      'id': modules.id,
      'name': modules.name
    }));
    setModules(data);
  };

  const fetchSubmodules = (moduleName) => {
    // Fetch submodules based on selected module from mockData
    const sMdata = Object.values(mockClass.modules).find(
      (module) => module.name === moduleName
    ) || [];
    const formattedData = sMdata.submodules.map((module, index) => ({
      id: index + 1,
      name: module.name,
    }));
    setSubmodules(formattedData);
  };

  const fetchSections = (moduleName, submoduleName) => {
    // Fetch sections based on selected submodule from mockData
    const sMdata = Object.values(mockClass.modules).find(
      (module) => module.name === moduleName) || {};
    const data = sMdata.submodules ? Object.values(sMdata.submodules).find(
      (submodule) => submodule.name === submoduleName) : [];
    //const data = sMdata.section[submoduleName] || [];
    const formattedData = data.sections.map((section, index) => ({
      id: index + 1,
      name: section,
    }));
    setSections(formattedData);
  };

 // const fetchQuizzes = (moduleName, submoduleName, sectionName) => {
 //   // Fetch quizzes based on section from mockData
 //   if (mockData.quiz) {
 //     setQuizzes([
 //       {
 //         id: 1,
 //         name: mockData.quiz.quiz_name,
 //       },
 //     ]);
 //     setQuizId(1); // Set a default quiz ID
 //   }
 // };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic

    // Create URL with query parameters
    const queryParams = new URLSearchParams({
      module: selectedModule,
      submodule: selectedSubmodule,
      section: selectedSection,
      quizType: quizType,
      algorithm: algorithm,
      instantCorrection: instantCorrection,
      quizName: quizName,
    });

    // Navigate to the new route with parameters
    router.push(`/quiz/section?${queryParams.toString()}`);
  
      
    alert(`Starting Quiz: ${quizName} with ID: ${quizId}`);
    // Add navigation logic here to route to the quiz page with `quizId`
  };

  return (
    <DashboardLayout>
      <div className="quiz-config-container dark-theme">
        <h1>Select Quiz Configuration</h1>
        <form onSubmit={handleSubmit} className="quiz-form">
        <div>
          <label>Module: </label><br />
          <select value={selectedModule} onChange={e => setSelectedModule(e.target.value)}>
            <option value="">Select Module</option>
            {modules.map(module => (
              <option key={module.id} value={module.name}>{module.name}</option>
            ))}
          </select>
          </div>

          <div>
            <label>Submodule: </label><br />
            <select value={selectedSubmodule} onChange={e => setSelectedSubmodule(e.target.value)}>
              <option value="">Select Submodule</option>
              {submodules.map(submodule => (
                <option key={submodule.id} value={submodule.name}>{submodule.name}</option>
              ))}
            </select>
          </div>

          <div>
            <label>Section: </label><br />
            <select value={selectedSection} onChange={e => setSelectedSection(e.target.value)}>
              <option value="">Select Section</option>
              {sections.map(section => (
                <option key={section.id} value={section.name}>{section.name}</option>
              ))}
            </select>
          </div>

          <div>
            <label>Quiz Type</label><br />
            <select value={quizType} onChange={e => setQuizType(e.target.value)}>
              <option value="past">Past Quiz</option>
              <option value="special">Educator Special</option>
            </select>
          </div>

          <div>
            <label>Question Generation Algorithm</label><br />
            <select value={algorithm} onChange={e => setAlgorithm(e.target.value)}>
              <option value="random">Random</option>
              {/*<option value="leastAttempted">Least Attempted</option>*/}
              <option value="mostFailed">Most Failed</option>
              <option value="neverAttempted">Never Attempted</option>
            </select>
          </div>

          <div>
            <label>Instant Correction</label><br />
            <input
              type="checkbox"
              checked={instantCorrection}
              onChange={() => setInstantCorrection(!instantCorrection)}
            />
          </div>

          <div>
            <label>Quiz Name</label><br />
              <input type="text" value={quizName} onChange={e => setQuizName(e.target.value)} />
          </div>

          <button type="submit">Start Quiz</button>
        </form>
      </div>
    </DashboardLayout>
  );
};

export default QuizConfig;
