//import { useState, useEffect } from 'react';


const QuestionCard = ({ question, onAnswerSelect, selectedAnswer }) => {
//const QuestionCard = ({ question, onAnswerSelect, instantCorrection }) => {
//  const [selectedOption, setSelectedOption] = useState('');
//
//  const handleOptionChange = (option) => {
//    setSelectedOption(option);
//    onAnswerSelect(question.id, option);
//
//    if (instantCorrection) {
//      alert(option === question.correct_answer ? 'Correct!' : 'Wrong!');
//    }
//  };
//
//  useEffect(() => {
//    setSelectedOption('');
//  }, [question]);
//
/* return (
    <div className="question-card">
        <div className='question'>
            <h3>{question.content}</h3>
        </div>
        <div className='options'>
                {Object.entries(question.options).map(([key, value]) => (
            <label key={key}>
            <input
                type="radio"
                name={`question-${question.id}`}
                value={key}
                checked={selectedOption === key}
                onChange={() => handleOptionChange(key)}
            />
            {value}
            </label>
        
        ))}
      </div>
    </div>
  );
};
*/
return (
    <div className="question-card">
        <div className='question'>
      <h3>{question.content}</h3>
        </div>
        <div className='options'>
            {Object.entries(question.options).map(([key, value]) => (
            <div key={key} className="option">
                <label>
                <input
                    type="radio"
                    name={`question-${question.id}`}
                    value={key}
                    checked={selectedAnswer === key}
                    onChange={() => onAnswerSelect(question.id, key)}
                />
                {value}
                </label>
            </div>
            ))}
        </div>
    </div>
  );
};

export default QuestionCard;

//export default QuestionCard;
