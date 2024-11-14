'use client';
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMoon, faSun, faSignOutAlt, faUserCircle } from '@fortawesome/free-solid-svg-icons';
import Image from 'next/image'; // assuming profile picture from assets or URL
import useAuthStore from '../store/authStore';
import { useRouter } from 'next/navigation';

const Header = () => {
    const { logout } = useAuthStore();
    const router = useRouter();
    const [darkTheme, setDarkTheme] = React.useState(false);
    
    const handleToggleTheme = () => {
        setDarkTheme(!darkTheme);
        document.body.classList.toggle('dark-theme', darkTheme);
    };
    
    const handleLogout = () => {
        logout();
        router.push('/auth/login');
    };
    
    return (
        <header className="header">
        <div className="logo">
            <h2>StudyPadi</h2>
        </div>
    
        <div className="theme-toggle">
            <button onClick={handleToggleTheme} aria-label="Toggle Theme">
            <FontAwesomeIcon icon={darkTheme ? faSun : faMoon} size="lg" />
            </button>
        </div>
    
        <div className="profile">
            <Image src="/profilePics1.jpg" alt="Profile" width={40} height={40} className="profile-pic" />
            <FontAwesomeIcon icon={faSignOutAlt} onClick={handleLogout} size="lg" className="logout-icon" />
        </div>
        </header>
    );
    };
    
    export default Header;