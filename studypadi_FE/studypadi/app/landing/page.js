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
      <section className="featuresGen">
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
{/* feautures section to enter here below*/}
      {/* Advanced Features Section */}
<section className="features">
  <h2 className="section-title">Discover the Power of StudyPadi</h2>
  <p className="section-subtitle">
    Transform your study sessions with a suite of innovative tools designed to enhance your learning experience.
  </p>

  <div className="feature-grid">
    {/* Feature 1: Robust Question Bank */}
    <div className="feature-card">
      <h3>📚 Extensive Question Bank</h3>
      <p>
        Access a vast, ever-growing <strong>Question Bank</strong> filled with carefully curated questions
        across multiple subjects and domains. Whether you're prepping for exams or brushing up on knowledge,
        StudyPadi has the resources you need to excel.
      </p>
    </div>

    {/* Feature 2: Traditional Quiz Functionality */}
    <div className="feature-card">
      <h3>📝 Classic Quiz Taking</h3>
      <p>
        Engage with familiar quiz formats like <strong>Multiple Choice</strong>, <strong>True/False</strong>,
        and more. Tailor your quizzes by setting timers and get instant feedback to sharpen your skills and
        boost your exam readiness.
      </p>
    </div>

    {/* Feature 3: Structured Educational Modules */}
    <div className="feature-card">
      <h3>🔍 Organized Learning Resources</h3>
      <p>
        Navigate through our well-structured modules, broken down into <strong>submodules</strong>, sections,
        and topics. StudyPadi simplifies complex subjects, making it easy to focus and master one topic at a time.
      </p>
    </div>

    {/* Feature 4: Dynamic Quiz Generation */}
    <div className="feature-card">
      <h3>⚙️ Advanced Quiz Algorithms</h3>
      <p>
        Experience personalized learning with our <strong>AI-powered quiz algorithms</strong>. Choose from
        <strong>Random, Adaptive, or Targeted</strong> quiz modes to match your study needs. Boost your learning
        curve with quizzes tailored to your weaknesses.
      </p>
    </div>

    {/* Feature 5: AI-Assisted Study Material Generator */}
    <div className="feature-card">
      <h3>🤖 AI-Assisted Test Generator</h3>
      <p>
        Leverage our <strong>AI-powered study tool</strong> to convert your notes and study materials into
        custom quizzes. Upload your documents and get instant, personalized practice questions to reinforce learning.
      </p>
    </div>

    {/* Feature 6: Comprehensive User Dashboard */}
    <div className="feature-card">
      <h3>📊 Smart Progress Tracking Dashboard</h3>
      <p>
        Track your study journey with our intuitive <strong>User Dashboard</strong>. Review past quizzes, monitor
        progress, set goals, and identify areas of improvement, all in one place.
      </p>
    </div>
  </div>
  
  {/* Call to Action */}
  <div className="cta-section">
    <p>Ready to elevate your study game?</p>
    <Link href="auth/register">
      <button className="cta-btn b1">Get Started for Free</button>
    </Link>
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
