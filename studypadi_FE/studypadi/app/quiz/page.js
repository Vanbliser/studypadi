import React from 'react';
import Sidebar from '../dashboard/sidebar';

const QuizzesPage = () => (
  <div className="quizzes-page">
    <Sidebar />
    <main className="quiz-container">
      <header className="quiz-header">
        <h1>StudyPadi</h1>
        <div className="user-controls">
          <img src="/path/to/profile.jpg" alt="Profile" className="profile-pic" />
          <button className="logout-button">Logout</button>
        </div>
      </header>
      <section className="quiz-content">
        <h2>Quiz Topic: Biology Basics</h2>
        <div className="question-section">
          <p>Q1. What is the powerhouse of the cell?</p>
        </div>
        <div className="answer-options">
          <button>Option A: Nucleus</button>
          <button>Option B: Mitochondria</button>
          <button>Option C: Ribosome</button>
          <button>Option D: Chloroplast</button>
        </div>
        <div className="question-nav">
          <div className="question-box answered">1</div>
          <div className="question-box unanswered">2</div>
          <div className="question-box unanswered">3</div>
          {/* Additional question boxes as needed */}
        </div>
      </section>
    </main>
  </div>
);

export default QuizzesPage;
