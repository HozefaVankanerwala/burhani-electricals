import React, { useState, useEffect } from 'react';
import { Zap, Menu, X } from 'lucide-react';

const Navbar: React.FC = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  
  const googleSearchUrl = "https://www.google.com/search?q=burhani+electricals+surat+navsari+bazar&sca_esv=5dca0e6f8aa8611e&biw=1920&bih=911&sxsrf=ANbL-n793-biMMCcYn6EDUATTBXGRWUKBQ%3A1771521361675&ei=UUWXaa34KMCfvr0PrYHqgQk&ved=0ahUKEwjt5OWrh-aSAxXAj68BHa2AOpAQ4dUDCBM&uact=5&oq=burhani+electricals+surat+navsari+bazar&gs_lp=Egxnd3Mtd2l6LXNlcnAiJ2J1cmhhbmkgZWxlY3RyaWNhbHMgc3VyYXQgbmF2c2FyaSBiYXphcjIFECEYoAEyBRAhGKABSOQyUPwCWJEwcAF4AJABAJgBqgKgAZUWqgEFMC45LjW4AQPIAQD4AQGYAg-gAsgWwgILEAAYgAQYsAMYogTCAggQABiwAxjvBcICBRAhGJ8FwgIEECEYFZgDAIgGAZAGBZIHBzEuNy42LjGgB_5AsgcHMC43LjYuMbgHxRbCBwYzLjExLjHIBxqACAA&sclient=gws-wiz-serp";

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 10);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleContactClick = (e: React.MouseEvent) => {
     // If we are already on the home page (no hash or empty hash), just scroll
     if (!window.location.hash || window.location.hash === '#') {
         const contactSection = document.getElementById('contact');
         if (contactSection) {
             e.preventDefault();
             contactSection.scrollIntoView({ behavior: 'smooth' });
         }
     }
     // If we are on services page (#all-services), normal href="#contact" works via App.tsx logic
     setIsMobileMenuOpen(false);
  };

  return (
    <nav 
      className={`fixed w-full z-40 transition-all duration-300 ${
        isScrolled ? 'bg-white shadow-md py-2' : 'bg-transparent py-4'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center">
          
          {/* Logo */}
          <div className="flex items-center cursor-pointer" onClick={() => window.location.href = '/'}>
            <div className="flex items-center justify-center px-2 py-1.5 rounded-lg mr-2 bg-brand-600 text-white shadow-sm">
               <span className="font-bold text-xl leading-none tracking-tighter">B</span>
               <Zap className="w-5 h-5 fill-current" />
               <span className="font-bold text-xl leading-none tracking-tighter">E</span>
            </div>
            <span className="text-xl font-bold text-slate-900">
              Burhani Electrical's
            </span>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex space-x-8">
            <a 
              href={googleSearchUrl}
              target="_blank"
              rel="noopener noreferrer"
              className={`font-medium hover:text-brand-600 transition ${isScrolled ? 'text-slate-700' : 'text-slate-800'}`}
            >
              Home
            </a>
            <a 
              href="#all-services" 
              className={`font-medium hover:text-brand-600 transition ${isScrolled ? 'text-slate-700' : 'text-slate-800'}`}
            >
              Services
            </a>
            <a 
              href="#contact" 
              onClick={handleContactClick}
              className={`font-medium hover:text-brand-600 transition ${isScrolled ? 'text-slate-700' : 'text-slate-800'}`}
            >
              Contact
            </a>
          </div>

          {/* Mobile Menu Button */}
          <div className="md:hidden">
            <button 
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="text-slate-900"
            >
              {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu Dropdown */}
      {isMobileMenuOpen && (
        <div className="md:hidden bg-white shadow-lg absolute top-full left-0 w-full py-4 px-4 flex flex-col space-y-4">
           <a 
             href={googleSearchUrl}
             target="_blank"
             rel="noopener noreferrer"
             onClick={() => setIsMobileMenuOpen(false)}
             className="text-slate-800 font-medium hover:text-brand-600 block"
           >Home</a>
           <a 
             href="#all-services" 
             onClick={() => setIsMobileMenuOpen(false)}
             className="text-slate-800 font-medium hover:text-brand-600 block"
           >Services</a>
           <a 
             href="#contact" 
             onClick={handleContactClick}
             className="text-slate-800 font-medium hover:text-brand-600 block"
           >Contact</a>
        </div>
      )}
    </nav>
  );
};

export default Navbar;