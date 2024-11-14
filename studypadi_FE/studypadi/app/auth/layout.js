import React from 'react';
import './module.auth.css';

const AuthLayout = ({ children }) => (
    <div className="authContainer">
        <div className="left-column">
            <div className="logo">
                <h1>StudyPadi</h1>
                <p>Your Personalized Study Partner</p>
            </div>
            {children}
        </div>
        <div className="right-column">
            <div className="text-overlay">
                <h2>StudyPadi - Your Study <br></br>Companion</h2>
                <br></br>
                <p>Personalized quizzes and dynamic revision questions</p>
            </div>
        </div>
    </div>
);

export default AuthLayout;
