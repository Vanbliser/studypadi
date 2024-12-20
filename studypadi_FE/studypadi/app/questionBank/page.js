'use client';
import React, { useState, useEffect } from 'react';

import useAuthStore from '../store/authStore';
import { useRouter } from 'next/navigation';
import DashboardLayout from "../dashboard/dashboardLayout";
import './question.css';
import { mockData, mockClass, mockQuiz } from '../mockData';

//const QuestionBank = () => (
//    <DashboardLayout>
//
//
//    </DashboardLayout>
//);



const FileUploadAndTable = () => {
    const [data, setData] = useState([]);
    const [modules, setModules] = useState([]);
    const [submodules, setSubmodules] = useState([]);
    const [sections, setSections] = useState([]);
    const [selectedModule, setSelectedModule] = useState('');
    const [selectedSubmodule, setSelectedSubmodule] = useState('');
    const [selectedSection, setSelectedSection] = useState('');
    const [showCustomSection, setShowCustomSection] = useState(false);
    const [customSection, setCustomSection] = useState('');
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [newQuizDetails, setNewQuizDetails] = useState(null);
    const [quizName, setQuizName] = useState('');



// remove the use effect after testing
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
  /*
    // Mock fetching from the database for modules, submodules, sections
    useEffect(() => {
        async function fetchModules() {
            // Replace with actual API calls
            const fetchedModules = await fetch('/api/modules').then(res => res.json());
            setModules(fetchedModules);
        }
        fetchModules();
    }, []);

    const handleModuleChange = async (e) => {
        setSelectedModule(e.target.value);
        setSelectedSubmodule('');
        setSelectedSection('');
        setShowCustomSection(false);
        
        const fetchedSubmodules = await fetch(`/api/submodules?module=${e.target.value}`).then(res => res.json());
        setSubmodules(fetchedSubmodules);
        setSections([]);
    };

    const handleSubmoduleChange = async (e) => {
        setSelectedSubmodule(e.target.value);
        setSelectedSection('');
        setShowCustomSection(false);

        const fetchedSections = await fetch(`/api/sections?submodule=${e.target.value}`).then(res => res.json());
        setSections(fetchedSections);
    };

    const handleSectionChange = (e) => {
        if (e.target.value === 'others') {
            setShowCustomSection(true);
            setCustomSection('');
        } else {
            setSelectedSection(e.target.value);
            setShowCustomSection(false);
        }
    };
*/

//taking data from an object/ shortcut
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




    const handleSave = async () => {
        try {/*
            await fetch('/api/save-questions', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ questions: data, selectedModule, selectedSubmodule, selectedSection: showCustomSection ? customSection : selectedSection }),
            });
            setNewQuizDetails({ name: 'Sample Quiz', id: '12345' });
            setShowSuccessModal(true);*/
            setNewQuizDetails({ name: 'Sample Quiz', id: '12345' });
            setShowSuccessModal(true);
            console.log(data)
        } catch (error) {
            console.error('Error saving questions:', error);
        }
    };

    return (
      <DashboardLayout>
        <div className="file-upload-container">
          {/* File Upload Input */}
          <input type="file" accept=".txt, .csv" onChange={handleFileUpload} />
          
          {/* Module, Submodule, Section Dropdowns */}
          <div className="selection-fields">
          <div>
          <label>Module: </label>
          <select value={selectedModule} onChange={e => setSelectedModule(e.target.value)}>
            <option value="">Select Module</option>
            {modules.map(module => (
              <option key={module.id} value={module.name}>{module.name}</option>
            ))}
          </select>
          </div>



          <div>
            <label>Submodule: </label>
            <select value={selectedSubmodule} onChange={e => setSelectedSubmodule(e.target.value)}>
              <option value="">Select Submodule</option>
              {submodules.map(submodule => (
                <option key={submodule.id} value={submodule.name}>{submodule.name}</option>
              ))}
            </select>
          </div>
          <div>
            <label>Section: </label>
            <select value={selectedSection} onChange={e => setSelectedSection(e.target.value)}>
              <option value="">Select Section</option>
              {sections.map(section => (
                <option key={section.id} value={section.name}>{section.name}</option>
              ))}
            </select>

            </div>
            <div>

            <label>Quiz Name</label>
              <input type="text" value={quizName} onChange={e => setQuizName(e.target.value)} />
            </div>
           
            </div>  
          
          {/* Questions Table */}
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
          
          {/* Success Modal */}
          {showSuccessModal && (
            <div className="success-modal">
              <h2>Quiz Saved Successfully!</h2>
              <p>Quiz Name: {newQuizDetails?.name}</p>
              <p>Quiz ID: {newQuizDetails?.id}</p>
              <button onClick={() => setShowSuccessModal(false)}>OK</button>
            </div>
          )}
        </div>
      </DashboardLayout>
    );
};

export default FileUploadAndTable;

/*
</div>
            <label>
              Module:
              <select value={selectedModule} onChange={handleModuleChange}>
                <option value="">Select Module</option>
                {modules.map((mod) => (
                  <option key={mod.id} value={mod.id}>{mod.name}</option>
                ))}
              </select>
            </label>
            <label>
              Submodule:
              <select value={selectedSubmodule} onChange={handleSubmoduleChange} disabled={!selectedModule}>
                <option value="">Select Submodule</option>
                {submodules.map((sub) => (
                  <option key={sub.id} value={sub.id}>{sub.name}</option>
                ))}
              </select>
            </label>
            <label>
              Section:
              <select value={selectedSection} onChange={handleSectionChange} disabled={!selectedSubmodule}>
                <option value="">Select Section</option>
                {sections.map((sec) => (
                  <option key={sec.id} value={sec.id}>{sec.name}</option>
                ))}
                <option value="others">Others</option>
              </select>
              {showCustomSection && (
                <input
                  type="text"
                  value={customSection}
                  onChange={(e) => setCustomSection(e.target.value)}
                  placeholder="Enter custom section name"
                />
              )}
            </label>
          </div>
*/