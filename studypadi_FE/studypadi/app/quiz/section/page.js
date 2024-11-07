'use client';
import { useState } from "react";
import DashboardLayout from '../../dashboard/dashboardLayout'
const QuizSection = () => {
    const [timer, setTimer] = useState(0); // A timer state that counts down/up.
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [answers, setAnswers] = useState({});
  
    const handleAnswer = (answer) => {
      setAnswers({ ...answers, [currentQuestion]: answer });
    };
  
    return (
      <DashboardLayout>
        <div className="quiz-section dark-theme">
          <header>
            <h2>Quiz: [Quiz Title]</h2>
            <div>Timer: {timer} seconds</div>
          </header>
          <div className="question-container">
            <div className="question">
              {/* Render current question */}
            </div>
            <div className="options">
              {/* Render options for the question */}
            </div>
          </div>
          <div className="quiz-controls">
            <button onClick={() => setCurrentQuestion(currentQuestion - 1)}>Previous</button>
            <button onClick={() => setCurrentQuestion(currentQuestion + 1)}>Next</button>
            <button >Submit Quiz</button>
          </div>
        </div>
      </DashboardLayout>
    );
  };
  
  export default QuizSection;
  