// /quiz configuration form
import { useState, useEffect } from 'react';

const QuizConfig = () => {
  const [modules, setModules] = useState([]);
  const [submodules, setSubmodules] = useState([]);
  const [sections, setSections] = useState([]);
  const [quizType, setQuizType] = useState('past');
  const [algorithm, setAlgorithm] = useState('random');
  const [instantCorrection, setInstantCorrection] = useState(false);

  useEffect(() => {
    // Fetch data from DB
    fetchModules();
    fetchSubmodules();
    fetchSections();
  }, []);

  const handleSubmit = () => {
    // Submit form and route to /quiz/section/id with selected options
  };

  return (
    <DashboardLayout>
      <div className="quiz-config-container dark-theme">
        <h1>Select Quiz Configuration</h1>
        <form onSubmit={handleSubmit}>
          <label>Module</label>
          <select onChange={e => setModule(e.target.value)}>
            {modules.map((module) => (
              <option key={module.id} value={module.id}>{module.name}</option>
            ))}
          </select>

          <label>Submodule</label>
          <select onChange={e => setSubmodule(e.target.value)}>
            {submodules.map((sub) => (
              <option key={sub.id} value={sub.id}>{sub.name}</option>
            ))}
          </select>

          <label>Section</label>
          <select onChange={e => setSection(e.target.value)}>
            {sections.map((section) => (
              <option key={section.id} value={section.id}>{section.name}</option>
            ))}
          </select>

          <label>Quiz Type</label>
          <select onChange={e => setQuizType(e.target.value)}>
            <option value="past">Past Quiz</option>
            <option value="special">Educator Special</option>
          </select>

          <label>Question Generation Algorithm</label>
          <select onChange={e => setAlgorithm(e.target.value)}>
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

          <button type="submit">Start Quiz</button>
        </form>
      </div>
    </DashboardLayout>
  );
};

export default QuizConfig;
