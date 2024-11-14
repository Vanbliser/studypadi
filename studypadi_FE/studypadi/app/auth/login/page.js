// app/auth/login/page.js
"use client";
import React, { useState } from 'react';
import useAuthStore from '../../store/authStore';
import { useRouter } from 'next/navigation';
import '../module.auth.css';
import Link from 'next/link';


const LoginPage = () => {
    const router = useRouter();
    const [email, setemail] = useState('');
    const [password, setPassword] = useState('');
    const login = useAuthStore((state) => state.login);
    const [message, setMessage] = useState('');
    
    const url = 'http://localhost:8000/api/v1/login/';

    

    const handleReset = async (e) => {
        e.preventDefault();
        
        router.push('/auth/forgot_password')
        
    }



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
          console.log(data)
          login(data.access_token, data.refresh_token, data.first_name)// Store token in zustand state
         // router.push({
         //   pathname: '/dashboard',
         //   query: { message: 'Login successful!' } // Pass message here
         // });
          //setMessage('Login successful')
          //console.log(data)
          //router.push(`/dashboard?message=${data.first_name}`) this is how you pass param to the url query 
          router.push('/dashboard')
          //window.location.href = '/dashboard';
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
                <div className='other_links'>
                    <Link className='signup'
                        href={'/auth/register'}>
                        <span>Sign Up</span>
                    </Link>
                    <a className='forgotPassword' onClick={handleReset}>Forgot password ?</a>
                </div>
            </form>
        </div>
    );
};

export default LoginPage;
