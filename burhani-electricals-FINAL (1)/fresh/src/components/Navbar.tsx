import React, { useState, useEffect } from 'react'
import { Zap, Menu, X } from 'lucide-react'

const Navbar: React.FC = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [isScrolled, setIsScrolled] = useState(false)

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 10)
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <nav className={`sticky top-0 z-50 transition-all duration-300 ${isScrolled ? 'bg-white shadow-md' : 'bg-white/90 backdrop-blur-sm'}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <a href="#" className="flex items-center space-x-2">
            <div className="bg-brand-600 p-1.5 rounded-lg">
              <Zap className="w-5 h-5 text-white fill-current" />
            </div>
            <span className="text-xl font-extrabold text-slate-900">Burhani <span className="text-brand-600">Electricals</span></span>
          </a>

          <div className="hidden md:flex items-center space-x-8">
            <a href="#" className="text-slate-600 hover:text-brand-600 font-medium transition-colors">Home</a>
            <a href="#services" className="text-slate-600 hover:text-brand-600 font-medium transition-colors">Services</a>
            <a href="#all-services" className="text-slate-600 hover:text-brand-600 font-medium transition-colors">All Services</a>
            <a href="#contact" className="text-slate-600 hover:text-brand-600 font-medium transition-colors">Contact</a>
            <a href="tel:+918780514062" className="bg-brand-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-brand-700 transition-colors">
              Call Now
            </a>
          </div>

          <button className="md:hidden p-2" onClick={() => setIsMenuOpen(!isMenuOpen)}>
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {isMenuOpen && (
          <div className="md:hidden py-4 border-t border-slate-100 flex flex-col space-y-3">
            <a href="#" className="text-slate-600 hover:text-brand-600 font-medium px-2 py-1" onClick={() => setIsMenuOpen(false)}>Home</a>
            <a href="#services" className="text-slate-600 hover:text-brand-600 font-medium px-2 py-1" onClick={() => setIsMenuOpen(false)}>Services</a>
            <a href="#all-services" className="text-slate-600 hover:text-brand-600 font-medium px-2 py-1" onClick={() => setIsMenuOpen(false)}>All Services</a>
            <a href="#contact" className="text-slate-600 hover:text-brand-600 font-medium px-2 py-1" onClick={() => setIsMenuOpen(false)}>Contact</a>
            <a href="tel:+918780514062" className="bg-brand-600 text-white px-4 py-2 rounded-lg font-medium text-center hover:bg-brand-700 transition-colors">Call Now</a>
          </div>
        )}
      </div>
    </nav>
  )
}

export default Navbar
