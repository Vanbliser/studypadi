// pages/index.js
'use client';
import Image from "next/image";
import Link from "next/link";
import { Carousel } from "react-responsive-carousel"; // Ensure to install a carousel component or create your own
import "react-responsive-carousel/lib/styles/carousel.min.css";


export default function HomePage() {
  return (
    <main className="landing-page">
      {/* Header Section */}
      <header className="header">
        <h1>Unlock Your Potential with AI-Powered Learning</h1>
        <p>Boost your study efficiency and examination success with StudyPadi, your self-learning, user-centered quiz companion.</p>
        <div className="nav-links">
          <Link href="/register">
            <button className="cta-btn">Register</button>
          </Link>
          <Link href="/login">
            <button className="cta-btn">Login</button>
          </Link>
          <Link href="/contact">
            <button className="cta-btn">Contact Us</button>
          </Link>
        </div>
        {/* Background image placeholder */}
        {/* Suggested Image: Students studying with laptops in a modern environment */}
      </header>

      {/* Carousel Section */}
      <section className="carousel-section">
        <Carousel showThumbs={false} infiniteLoop autoPlay>
          <div>
            {/* Suggested Image: AI-based learning interface screenshot */}
            <Image src="/path/to/ai-learning.jpg" alt="AI learning interface" width={800} height={400} />
            <p className="legend">AI-Powered Learning</p>
          </div>
          <div>
            {/* Suggested Image: Student answering questions on a digital quiz */}
            <Image src="/path/to/quiz-interface.jpg" alt="Quiz interface" width={800} height={400} />
            <p className="legend">User-Centered Quiz App</p>
          </div>
          <div>
            {/* Suggested Image: Person studying in a cozy environment */}
            <Image src="/path/to/self-study.jpg" alt="Self learning environment" width={800} height={400} />
            <p className="legend">Enhance Self-Learning</p>
          </div>
        </Carousel>
      </section>

      {/* Features Section */}
      <section className="features">
        <h2>Why StudyPadi?</h2>
        <div className="feature-item">
          <h3>Improved Reading & Assimilation</h3>
          <p>StudyPadi helps you absorb information faster and more effectively with techniques designed for better retention and understanding.</p>
        </div>
        <div className="feature-item">
          <h3>AI-Powered Personalization</h3>
          <p>Our app adapts to your learning style, providing personalized quizzes and study guides tailored to your strengths and weaknesses.</p>
        </div>
        <div className="feature-item">
          <h3>Self-Paced Learning</h3>
          <p>Access resources and quizzes anytime, anywhere. StudyPadi is designed for learners who want to study at their own pace.</p>
        </div>
        <div className="feature-item">
          <h3>Focused on Examination Success</h3>
          <p>Prepare confidently for exams with AI-driven quizzes that simulate the test environment, helping you track your progress.</p>
        </div>
      </section>

      {/* About Developers Section */}
      <section className="developers">
        <h2>Meet the Developers</h2>
        <div className="developer-profile">
          <div className="developer-image">
            {/* Placeholder for BE Developer Image */}
            {/* Suggested Image: Professional photo of Backend Developer */}
            <Image src="/path/to/backend-dev.jpg" alt="Backend Developer" width={200} height={200} />
          </div>
          <div className="developer-details">
            <h3>Backend Developer - John Doe</h3>
            <p>John is a seasoned backend developer with expertise in Node.js and database management, ensuring StudyPadi's robust data handling.</p>
          </div>
        </div>
        <div className="developer-profile">
          <div className="developer-image">
            {/* Placeholder for FE Developer Image */}
            {/* Suggested Image: Professional photo of Frontend Developer */}
            <Image src="/path/to/frontend-dev.jpg" alt="Frontend Developer" width={200} height={200} />
          </div>
          <div className="developer-details">
            <h3>Frontend Developer - Jane Smith</h3>
            <p>Jane is a skilled frontend developer passionate about creating seamless, user-friendly interfaces to enhance the StudyPadi experience.</p>
          </div>
        </div>
      </section>

      {/* Footer Section */}
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} StudyPadi. All rights reserved.</p>
      </footer>

      {/* CSS Styling */}
      <style jsx>{`
        .landing-page {
          background-color: #ffffff;
          color: #000000;
          font-family: Arial, sans-serif;
        }
        .header {
          text-align: center;
          padding: 4rem 2rem;
          background-color: #000000;
          color: #ffffff;
        }
        .cta-btn {
          margin: 1rem;
          padding: 0.75rem 1.5rem;
          background-color: #ffffff;
          color: #000000;
          border: none;
          cursor: pointer;
          transition: background 0.3s;
        }
        .cta-btn:hover {
          background-color: #f0f0f0;
        }
        .carousel-section {
          margin: 2rem 0;
        }
        .features {
          text-align: center;
          padding: 2rem;
        }
        .feature-item {
          margin: 2rem 0;
        }
        .developers {
          text-align: center;
          padding: 2rem;
          background-color: #f9f9f9;
        }
        .developer-profile {
          display: flex;
          justify-content: center;
          margin: 2rem 0;
        }
        .developer-image {
          margin-right: 1.5rem;
        }
        .footer {
          text-align: center;
          padding: 1rem;
          background-color: #000000;
          color: #ffffff;
        }
      `}</style>
    </main>
  );
}
