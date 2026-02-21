import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Services from './components/Services';
import Contact from './components/Contact';
import Footer from './components/Footer';
import FloatingCTA from './components/FloatingCTA';
import AIChat from './components/AIChat';
import ServicesPage from './components/ServicesPage';

const App: React.FC = () => {
  const [currentHash, setCurrentHash] = useState(window.location.hash);

  useEffect(() => {
    const handleHashChange = () => {
      setCurrentHash(window.location.hash);
    };

    window.addEventListener('hashchange', handleHashChange);
    return () => window.removeEventListener('hashchange', handleHashChange);
  }, []);

  // Effect to handle scrolling when the hash is #contact or empty (Home)
  useEffect(() => {
    if (currentHash === '#contact') {
      // Use a timeout to allow the DOM to update if we are switching views
      setTimeout(() => {
        const contactSection = document.getElementById('contact');
        if (contactSection) {
          contactSection.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
    } else if (currentHash === '' || currentHash === '#') {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }, [currentHash]);

  // Determine which view to show
  // We only show the full ServicesPage if the hash is exactly #all-services
  const isServicesPage = currentHash === '#all-services';

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col">
      <Navbar />
      <main className="flex-grow">
        {isServicesPage ? (
          <ServicesPage />
        ) : (
          <>
            <Hero />
            <Services />
            <Contact />
          </>
        )}
      </main>
      <Footer />
      <FloatingCTA />
      <AIChat />
    </div>
  );
};

export default App;