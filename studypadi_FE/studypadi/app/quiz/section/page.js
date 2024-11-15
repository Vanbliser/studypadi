// app/quiz/section/page.js
'use client';
import { useRouter } from 'next/navigation';
import { useState, useEffect } from 'react';
import QuizTimer from './QuizTimer';
import QuestionCard from './QuestionCard';
import QuestionNavigator from './QuestionNavigator';
import { mockQuiz } from '../../mockData';
import './quizStyle.css';
import DashboardLayout from '../../dashboard/dashboardLayout';
import { useQuizStore } from '../../store/quizStore'; // Zustand store


const QuizContainer = () => {
  const router = useRouter();
  const { quiz } = mockQuiz;
  const [currentIndex, setCurrentIndex] = useState(0);
  const { userAnswers, setUserAnswers, timeTaken, setTimeTaken, clearAnswers } = useQuizStore();
  const [isSubmitted, setIsSubmitted] = useState(false);
  const startTime = Date.now();
  const handleAnswerSelect = (questionId, answer) => {
    setUserAnswers(questionId, answer);
  };

  const handleSubmit = () => {
    console.log(userAnswers)
    setIsSubmitted(true);
    const endTime = Date.now();
    setTimeTaken(Math.floor((endTime - startTime) / 1000)); // Save total time in seconds
  
    
  };
  

  const handleTimeUp = () => {
    alert('Time is up! Submitting your quiz.');
    handleSubmit();
  };

  const calculateScore = () => {
    const totalQuestions = quiz.questions.length;
    let correctAnswers = 0;

    quiz.questions.forEach((q) => {
      if (userAnswers[q.id] === q.correct_answer) correctAnswers++;
    });

    const scorePercentage = ((correctAnswers / totalQuestions) * 100).toFixed(2);
    const avgTimePerQuestion = (timeTaken / totalQuestions).toFixed(2);
  
  

    return {
      score: correctAnswers,
      scorePercentage,
      timeTaken: `${Math.floor(timeTaken / 60)}m ${timeTaken % 60}s`,
      avgTimePerQuestion,
    };
  };

  // Quiz Summary Page
  if (isSubmitted) {
    const scoreData = calculateScore();

    const handleClearSubmit = () => {
      // Clear Zustand store and localStorage
      clearAnswers();
      localStorage.removeItem('userAnswers'); // Clear saved answers in localStorage
  
      router.push('/quiz')
      
    }

    return (
      <div className="quiz-score dark-theme">
        <h1>Quiz Summary</h1>
        <p>Score: {scoreData.scorePercentage}%</p>
        <p>Time Taken: {scoreData.timeTaken}</p>
        <p>Average Time per Question: {scoreData.avgTimePerQuestion} seconds</p>
        <div className="question-review">
          {quiz.questions.map((q, index) => (
            <div key={q.id} className="review-item">
              <h4>Question {index + 1}:</h4>
              <p>Your Answer: {userAnswers[index + 1] || 'No answer'}</p>
              <p>Correct Answer: {q.id}{q.correct_answer}</p>
            </div>
          ))}
        </div>
        <button onClick={handleClearSubmit}>Ok</button>
      </div>
    );
  }

  return (
    <DashboardLayout>
    <div className="quiz-container">
      {/* New Progress Indicator */}
      <div className="progress-indicator">
        Question {currentIndex + 1} / {quiz.total_questions}
      </div>
      <QuizTimer duration={quiz.duration} onTimeUp={handleTimeUp} />
      <QuestionCard
        question={quiz.questions[currentIndex]}
        onAnswerSelect={handleAnswerSelect}
        selectedAnswer={userAnswers[quiz.questions[currentIndex].id] || ''}
      />
      <div className="quiz-navigation">
        {/* Disable 'Prev' on the first question */}
        <button
          disabled={currentIndex === 0}
          onClick={() => setCurrentIndex((prev) => prev - 1)}
        >
          Prev
        </button>

        {/* Show 'Next' until the last question, then show 'Submit' */}
        {/*currentIndex < quiz.total_questions - 1 ? (*/}
          <button
            disabled={currentIndex === quiz.total_questions - 1}
            onClick={() => setCurrentIndex((prev) => prev + 1)}
          >
            Next
          </button>
       
          <button className="submit-btn" onClick={handleSubmit}>
            Submit
          </button>
        
      </div>
    </div>
    </DashboardLayout>
  );
};

export default QuizContainer;