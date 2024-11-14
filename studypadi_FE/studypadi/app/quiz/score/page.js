const QuizScore = ({ scoreData }) => {
    return (
      <DashboardLayout>
        <div className="quiz-score dark-theme">
          <h1>Quiz Summary</h1>
          <p>Score: {scoreData.scorePercentage}%</p>
          <p>Time Taken: {scoreData.timeTaken}</p>
          <p>Average Time per Question: {scoreData.avgTimePerQuestion}</p>
          <div className="question-review">
            {/* Map through questions and answers for review */}
          </div>
        </div>
      </DashboardLayout>
    );
  };
  
  export default QuizScore;
  