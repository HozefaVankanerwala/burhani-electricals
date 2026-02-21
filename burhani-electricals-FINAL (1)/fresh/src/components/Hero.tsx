import React from 'react'
import { Phone, Wrench, Zap } from 'lucide-react'

const Hero: React.FC = () => {
  return (
    <div className="relative bg-brand-50 overflow-hidden">
      <div className="absolute inset-0">
        <img
          src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&q=80"
          alt="Electrical Repair Services"
          className="w-full h-full object-cover opacity-10"
        />
        <div className="absolute inset-0 bg-gradient-to-r from-brand-100/90 to-brand-50/80"></div>
      </div>

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 md:py-32">
        <div className="text-center">
          <div className="flex justify-center mb-6">
            <span className="inline-flex items-center px-4 py-1.5 rounded-full text-sm font-semibold bg-white/60 backdrop-blur-sm text-brand-800 border border-brand-200 shadow-sm">
              <Zap className="w-4 h-4 mr-2 fill-current text-brand-600" />
              Trusted Repair Service Since 2018
            </span>
          </div>
          <h1 className="text-4xl md:text-6xl font-extrabold text-slate-900 tracking-tight mb-6 drop-shadow-sm">
            Burhani Electricals
          </h1>
          <p className="mt-4 max-w-2xl mx-auto text-xl text-slate-700 mb-10 font-medium">
            Expert rewinding and repairing for all types of fans, mixers, irons, and geysers. Fast, reliable, and affordable service.
          </p>
          <div className="flex flex-col sm:flex-row justify-center gap-4">
            <a
              href="tel:+918780514062"
              className="inline-flex items-center justify-center px-8 py-3 text-base font-medium rounded-md text-white bg-brand-600 hover:bg-brand-700 transition-colors shadow-lg"
            >
              <Phone className="w-5 h-5 mr-2" />
              Call Now
            </a>
            <a
              href="#all-services"
              className="inline-flex items-center justify-center px-8 py-3 text-base font-medium rounded-md text-white bg-brand-600 hover:bg-brand-700 transition-colors shadow-lg"
            >
              <Wrench className="w-5 h-5 mr-2" />
              Our Services
            </a>
          </div>
        </div>
      </div>

      <div className="absolute bottom-0 w-full overflow-hidden leading-none">
        <svg className="relative block w-full h-12 md:h-24 text-slate-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" className="fill-current"></path>
        </svg>
      </div>
    </div>
  )
}

export default Hero
