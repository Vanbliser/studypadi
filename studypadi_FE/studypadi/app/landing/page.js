// pages/index.js
'use client';
import Image from "next/image";
import Link from "next/link";
import { Carousel } from "react-responsive-carousel"; // Ensure to install a carousel component or create your own
import "react-responsive-carousel/lib/styles/carousel.min.css";
import "./landingStyle.css";


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
        <h1>Unlock Your Potential <br></br>with AI-Powered Learning</h1>
        <p>Boost your study efficiency and examination success with <span className="studp">StudyPadi</span>,<br></br> your self-learning, user-centered quiz companion.</p>
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
        {/* Background image placeholder */}
        {/* Suggested Image: Students studying with laptops in a modern environment */}
      </div>
      </header>
      

      {/* Carousel Section 
      <section className="carousel-section">
        <Carousel showThumbs={true} infiniteLoop autoPlay>
          <div>
            {/* Suggested Image: AI-based learning interface screenshot *
            <Image src="/carousel_004.jpg" alt="AI learning interface" width={400} height={600} />
            <p className="legend">AI-Powered Learning</p>
          </div>
          <div>
            {/* Suggested Image: Student answering questions on a digital quiz *
            <Image src="/carousel_005.jpg" alt="Quiz interface" width={400} height={600} />
            <p className="legend">User-Centered Quiz App</p>
          </div>
          <div>
            {/* Suggested Image: Person studying in a cozy environment *
            <Image src="/carousel_006.jpg" alt="Self learning environment" width={600} height={400} />
            <p className="legend">Enhance Self-Learning</p>
          </div>
        </Carousel>
      </section>

      {/* Features Section */}
      <section className="features">
        <h2>Why StudyPadi?</h2>
        <div className="feature-children">
        <div className="feature-item c1">
          <h3>Improved Reading & Assimilation</h3>
          <p>StudyPadi helps you absorb information faster and more effectively with techniques designed for better retention and understanding.</p>
        </div>
        <div className="feature-item c2">
          <h3>AI-Powered Personalization</h3>
          <p>Our app adapts to your learning style, providing personalized quizzes and study guides tailored to your strengths and weaknesses.</p>
        </div>
        <div className="feature-item c1">
          <h3>Self-Paced Learning</h3>
          <p>Access resources and quizzes anytime, anywhere. StudyPadi is designed for learners who want to study at their own pace.</p>
        </div>
        <div className="feature-item c2">
          <h3>Focused on Examination Success</h3>
          <p>Prepare confidently for exams with AI-driven quizzes that simulate the test environment, helping you track your progress.</p>
        </div>
        </div>
      </section>

      {/* About Developers Section */}
      <div id="about">
<section className="developers">
  <h2 className="dev-text">Meet the Developers</h2>
  <div className="dev-container">
    {/* Backend Developer Profile */}
    <div className="developer-profile">
      <h1 className="dev-text">Backend Developer</h1>
      <div className="developer-image">
        <Image
          className="dp"
          src="/profilePics2.jpg"
          alt="Backend Developer"
          width={200}
          height={200}
        />
      </div>
      <div className="developer-details">
        <h3 className="dev-text">Blossom Ayogu</h3>
        <p className="dev-text">
          Blossom is a seasoned backend developer with expertise in Node.js and
          database management, ensuring StudyPadi's robust data handling.
        </p>
        <div className="social-links">
          {/* Add social icons here */}
        </div>
      </div>
    </div>

    {/* Frontend Developer Profile */}
    <div className="developer-profile">
      <h1 className="dev-text">Frontend Developer</h1>
      <div className="developer-image">
        <Image
          className="dp"
          src="/profilePics3.jpeg"
          alt="Frontend Developer"
          width={200}
          height={200}
        />
      </div>
      <div className="developer-details">
        <h3 className="dev-text">Emmanuel Nwafor</h3>
        <p className="dev-text">
          Emmanuel is a skilled frontend developer passionate about creating
          seamless, user-friendly interfaces to enhance the StudyPadi experience.
        </p>
        <div className="social-links">
          {/* Add social icons here */}
        </div>
      </div>
    </div>
  </div>
</section>
</div>


      {/* Footer Section */}
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} StudyPadi. All rights reserved.</p>
      </footer>
    
    </main>
  );
}
