'use client';
import React, { useState, useEffect } from 'react';
import useAuthStore from './store/authStore';
import { usePathname, useRouter } from 'next/navigation';

const Authorization = ({children}) => {
    const path = usePathname();
    const router = useRouter();

    const privatePath = ['/settings', '/modules', '/quizzes', '/test'];

    const accessToken = useAuthStore((state) => state.accessToken);

    useEffect(() => {
        console.log("Access token from Zustand:", accessToken);

        if (!accessToken && privatePath.includes(path)) {
            router.push('/auth/login')
            console.log("Data didnt persist in store");
        }
    }, [accessToken, router])

    if (privatePath.includes(path) && !accessToken) {
        
        return <p>Loading</p>
    }
    return children;


}
// how to persist state in zustand
// handle 401 response from the server, by requesting a new token from the server with the refresh token -
// if it fails then redirect to login page

//useEffect(() => {
//    const handle401Response = async () => {
//        try {
//            // Make a request to the server to refresh the token using the refresh token
//            const response = await fetch('/refresh-token', {
//                method: 'POST',
//                headers: {
//                    'Content-Type': 'application/json',
//                    'Authorization': `Bearer ${refreshToken}`
//                }
//            });
//
//            if (response.ok) {
//                // Token refresh successful, update the access token in the store
//                const data = await response.json();
//                useAuthStore.setState({ accessToken: data.accessToken });
//            } else {
//                // Token refresh failed, redirect to login page
//                router.push('/auth/login');
//            }
//        } catch (error) {
//            console.error('Error refreshing token:', error);
//            // Token refresh failed, redirect to login page
//            router.push('/auth/login');
//        }
//    };
//
//    if (accessToken && path && privatePath.includes(path)) {
//        handle401Response();
//    }
//}, [accessToken, path, privatePath, router]);

export default Authorization;