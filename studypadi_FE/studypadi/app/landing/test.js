'use client';
import Image from 'next/image';
import Link from 'next/link';
import { Carousel } from 'react-responsive-carousel';
//import { FaGithub, FaTwitter, FaEnvelope } from 'react-icons/fa';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './landingStyle.css';

export default function HomePage() {
  return (
    <main className="landing-page">
      {/* Header Section */}
      <header className="header">
        <div className="logo">
          <h1>StudyPadi</h1>
          <p>Your Personalized Study Partner</p>
        </div>

        <div className="hero">
          <h1>
            Unlock Your Potential <br />
            with AI-Powered Learning
          </h1>
          <p>
            Boost your study efficiency and examination success with{' '}
            <span className="studp">StudyPadi</span>, your self-learning, user-centered quiz companion.
          </p>
          <div className="nav-links">
            <Link href="auth/register">
              <button className="cta-btn b1">Register</button>
            </Link>
            <Link href="auth/login">
              <button className="cta-btn b2">Login</button>
            </Link>
            <Link href="#about">
              <button className="cta-btn b3">Contact Us</button>
            </Link>
          </div>
        </div>
      </header>

      {/* Features Section */}
      <section className="features">
        <h2>Why StudyPadi?</h2>
        <div className="feature-children">
          <div className="feature-item c1">
            <Image src="/illustration1.png" alt="Reading" width={100} height={100} />
            <h3>Improved Reading & Assimilation</h3>
            <p>Absorb information faster and more effectively with techniques for better retention.</p>
          </div>
          <div className="feature-item c2">
            <Image src="/illustration2.png" alt="AI Personalization" width={100} height={100} />
            <h3>AI-Powered Personalization</h3>
            <p>Tailored quizzes and study guides based on your strengths and weaknesses.</p>
          </div>
          <div className="feature-item c1">
            <Image src="/illustration3.png" alt="Self Learning" width={100} height={100} />
            <h3>Self-Paced Learning</h3>
            <p>Access resources and quizzes anytime, anywhere at your own pace.</p>
          </div>
          <div className="feature-item c2">
            <Image src="/illustration4.png" alt="Exam Success" width={100} height={100} />
            <h3>Focused on Examination Success</h3>
            <p>Prepare confidently with AI-driven quizzes that simulate test environments.</p>
          </div>
        </div>
      </section>

      {/* About Developers Section */}
      <section id="about" className="developers">
        <h2>Meet the Developers</h2>
        <div className="dev-container">
          {/* Backend Developer */}
          <div className="developer-profile">
            <div className="developer-image">
              <Image className="dp" src="/profilePics2.jpg" alt="Blossom Ayogu" width={200} height={200} />
            </div>
            <div className="developer-details">
              <h3>Blossom Ayogu</h3>
              <p>Seasoned backend developer specializing in Node.js and robust data management.</p>
              <div className="social-links">
                <a href="https://github.com/blossomayogu" target="_blank" rel="noopener noreferrer">
                  {/*<FaGithub />*/}
                </a>
                <a href="mailto:blossom@example.com">
                  {/*<FaEnvelope />*/}
                </a>
                <a href="https://twitter.com/blossomdev" target="_blank" rel="noopener noreferrer">
                  {/*<FaTwitter />*/}
                </a>
              </div>
            </div>
          </div>

          {/* Frontend Developer */}
          <div className="developer-profile">
            <div className="developer-image">
              <Image className="dp" src="/profilePics3.jpeg" alt="Emmanuel Nwafor" width={200} height={200} />
            </div>
            <div className="developer-details">
              <h3>Emmanuel Nwafor</h3>
              <p>Frontend developer focused on creating seamless, user-friendly interfaces.</p>
              <div className="social-links">
                <a href="https://github.com/OracleOG" target="_blank" rel="noopener noreferrer">
                 { /*<FaGithub />*/}
                </a>
                <a href="mailto:emmanuel@example.com">
                  {/*<FaEnvelope />*/}
                </a>
                <a href="https://twitter.com/emmanwafor" target="_blank" rel="noopener noreferrer">
                  {/*<FaTwitter />*/}
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer Section */}
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} StudyPadi. All rights reserved.</p>
      </footer>
    </main>
  );
}
