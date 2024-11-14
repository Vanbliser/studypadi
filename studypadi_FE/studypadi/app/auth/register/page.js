// app/auth/register/page.js

"use client";
import React, { useState } from 'react';
import Link from 'next/link';

const SignUpPage = () => {
    const [email, setEmail] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [message, setMessage] = useState('');

    const url = 'http://localhost:8000/api/v1/signup/';

    const handleSignUp = async (e) => {
        e.preventDefault();

        // Ensure all fields are filled
        if (!email || !firstName || !lastName || !password || !confirmPassword) {
            setMessage("Please fill in all fields.");
            return;
        }

        // Ensure passwords match
        if (password !== confirmPassword) {
            setMessage("Passwords do not match.");
            return;
        }


        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    'email': email,
                    'first_name': firstName,
                    'last_name': lastName,
                    'password': password,
                    'confirm_password': confirmPassword,
                }),
            });

            const data = await response.json();
            if (response.ok) {
                setMessage(data.message);
                // Optionally, redirect to the login page
                window.location.href = '/auth/verify';
            } else {
                setMessage(data.error || "An error occurred during signup.");
            }
        } catch (error) {
            setMessage(String(error && error.message) || "An error occurred during signup.");
        }
    };

    return (
        <div className="form">
            <br></br>
            <br></br>
            <br></br>
            <h2>Sign Up</h2>
            {message && <p>{message}</p>}
            <form onSubmit={handleSignUp}>
                <label htmlFor="email">Email</label>
                <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <label htmlFor="firstName">First Name</label>
                <input
                    type="text"
                    id="firstName"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                />
                <label htmlFor="lastName">Last Name</label>
                <input
                    type="text"
                    id="lastName"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                />
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <label htmlFor="confirmPassword">Confirm Password</label>
                <input
                    type="password"
                    id="confirmPassword"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                />
                <button type="submit">Register</button>

                <Link className='signup'
                        href={'/auth/login'}>
                        <span>Registered Already? Sign In !!!</span>
                </Link>
            </form>
        </div>
    );
};

export default SignUpPage;
