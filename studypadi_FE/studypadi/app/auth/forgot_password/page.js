"use client";
import React, { useState } from 'react';
import { useRouter } from 'next/router';


const ForgetPassword = () => {
    const [email, setemail] = useState('');
    const resetUrl = 'http://localhost:8000/api/vi/forget-password/'; // This is the forget password BE endpoint

    const router = useRouter();

    const handleReset = async (e) => {
        e.preventDefault();
        const response = await fetch(resetUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
              { 'email': email, 'base_url': base_url }),
        });
        if (!response.ok) {
            setMessage(String(response.statusText) || "An error occurred during login.");
        }
        else {
          const data = await response.json();
          setMessage(data.message)
          
          //redirect user to the reset password page form
          router.push('/reset')
        }
    }


    return (
        <div className="form">
            <h2>Forgot Password</h2>
            <br></br>
            {message && <p>{message}</p>}
            <form onSubmit={handleReset}>
                <label htmlFor="email">Email Address</label>
                <input
                    type="text"
                    id="email"
                    value={email}
                    onChange={(e) => setemail(e.target.value)}
                />
                <br></br>
                <button type="submit">Forgot password</button>
            </form>
        </div>
    );
};

export default ForgetPassword;
