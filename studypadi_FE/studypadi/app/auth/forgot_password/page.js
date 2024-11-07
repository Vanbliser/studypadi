"use client";
import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';


const ForgetPassword = () => {
    const [email, setemail] = useState('');
    const [message, setMessage] = useState('');
    const resetUrl = 'http://localhost:8000/api/vi/forget-password/'; // This is the forget password BE endpoint

    const base_url = 'http://localhost:3000/auth/reset'; // This is the base url of the frontend

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
            return(
                <div>
                    <p>A mail with the Reset link has just been sent to your mail</p>
                    <p>Kidly check your mail and follow the link to reset your password</p>
                </div>
            )
        //  const data = await response.json();
        //  setMessage(data.message)
        //  
        //  //redirect user to the reset password page form
        //  router.push('/reset')
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
                <Link className='signup'
                        href={'/auth/login'}>
                        <span>{'<<<'} Go back to Login</span>
                </Link>
            </form>
        </div>
    );
};

export default ForgetPassword;
