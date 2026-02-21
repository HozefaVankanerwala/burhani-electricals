import React from 'react'
import { Phone } from 'lucide-react'

const FloatingCTA: React.FC = () => {
  return (
    <a
      href="tel:+918780514062"
      className="fixed bottom-6 right-6 z-40 flex items-center space-x-2 bg-brand-600 text-white px-5 py-3 rounded-full shadow-2xl hover:bg-brand-700 transition-all duration-300 hover:scale-105"
      aria-label="Call Burhani Electricals"
    >
      <Phone className="w-5 h-5" />
      <span className="font-semibold text-sm hidden sm:inline">Call Now</span>
    </a>
  )
}

export default FloatingCTA
