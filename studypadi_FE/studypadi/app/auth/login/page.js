
"use client";
import React, { useState } from 'react';
import useAuthStore from '../../store/authStore';


const LoginPage = () => {
    const [email, setemail] = useState('');
    const [password, setPassword] = useState('');
    const login = useAuthStore((state) => state.login);
    const [message, setMessage] = useState('');
    
    const url = 'http://localhost:8000/api/v1/login/';


    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
              { 'email': email,
               'password': password }),
        });
        if (!response.ok) {
            setMessage(String(response.statusText) || "An error occurred during login.");
        }
        else {
          const data = await response.json();
          login(data.access_token, data.refresh_token, data.first_name)// Store token in zustand state
          setMessage('Login successful')
          console.log(data)
          window.location.href = '/dashboard';
      };
    }

    return (
        <div className="form">
            <h2>LOG In</h2>
            <br></br>
            {message && <p>{message}</p>}
            <form onSubmit={handleSubmit}>
                <label htmlFor="email">Email Address</label>
                <input
                    type="text"
                    id="email"
                    value={email}
                    onChange={(e) => setemail(e.target.value)}
                />
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">LOG In</button>
            </form>
        </div>
    );
};

export default LoginPage;
