import { useState } from 'react';

const QuestionNavigator = ({ totalQuestions, onNavigate, onSubmit }) => {
  const [currentQuestion, setCurrentQuestion] = useState(0);

  const handleNext = () => {
    if (currentQuestion < totalQuestions - 1) {
      setCurrentQuestion(currentQuestion + 1);
      onNavigate(currentQuestion + 1);
    }
  };

  const handlePrev = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
      onNavigate(currentQuestion - 1);
    }
  };

  return (
    <div className="navigation-buttons">
      <button onClick={handlePrev} disabled={currentQuestion === 0}>Previous</button>
      {currentQuestion < totalQuestions - 1 ? (
        <button onClick={handleNext}>Next</button>
      ) : (
        <button onClick={onSubmit}>Submit</button>
      )}
    </div>
  );
};

export default QuestionNavigator;
