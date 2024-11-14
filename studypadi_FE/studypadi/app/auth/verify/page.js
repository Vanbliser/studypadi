
"use client";
import React, { useState } from 'react';


const Verify = () => {
    const [otp, setotp] = useState('');
    const [email, setemail] = useState('');
    const [message, setMessage] = useState('');
    
    const url = 'http://localhost:8000/api/v1/verify-otp/';


    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
              { 'email': email,
               'otp': otp }),
        });
        if (!response.ok) {
            setMessage(String(response.statusText) || "An error occurred during verification.");
        }
        else {
          const data = await response.json();
            setMessage(data.message)
            console.log(data)
            //window.location.href = '/auth/login';
        }
    }

    return (
        <div className="form">
            <h2>Verify User Acess</h2>
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
                <label htmlFor="otp">OTP</label>
                <input
                    type="otp"
                    id="otp"
                    value={otp}
                    onChange={(e) => setotp(e.target.value)}
                />
                <button type="submit">Verify</button>
            </form>
        </div>
    );
};

export default Verify;
