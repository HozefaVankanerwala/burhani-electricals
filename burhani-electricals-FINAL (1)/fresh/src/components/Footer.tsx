import React from 'react'
import { Zap, Phone, MessageCircle } from 'lucide-react'

const Footer: React.FC = () => {
  return (
    <footer className="bg-slate-900 text-slate-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <div className="bg-brand-600 p-1.5 rounded-lg">
                <Zap className="w-5 h-5 text-white fill-current" />
              </div>
              <span className="text-xl font-extrabold text-white">Burhani <span className="text-brand-400">Electricals</span></span>
            </div>
            <p className="text-slate-400 text-sm leading-relaxed">
              Professional repair and rewinding services for all types of fans and home appliances. Owned by Mr. Husain M Vankanerwala.
            </p>
          </div>

          <div>
            <h3 className="text-white font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-brand-400 transition-colors">Home</a></li>
              <li><a href="#services" className="hover:text-brand-400 transition-colors">Services</a></li>
              <li><a href="#all-services" className="hover:text-brand-400 transition-colors">All Services</a></li>
              <li><a href="#contact" className="hover:text-brand-400 transition-colors">Contact</a></li>
            </ul>
          </div>

          <div>
            <h3 className="text-white font-semibold mb-4">Contact</h3>
            <div className="space-y-3 text-sm">
              <a href="tel:+918780514062" className="flex items-center hover:text-brand-400 transition-colors">
                <Phone className="w-4 h-4 mr-2 text-brand-400" />
                +91 87805 14062
              </a>
              <a href="https://wa.me/918780514062" target="_blank" rel="noopener noreferrer" className="flex items-center hover:text-brand-400 transition-colors">
                <MessageCircle className="w-4 h-4 mr-2 text-brand-400" />
                WhatsApp Us
              </a>
            </div>
          </div>
        </div>

        <div className="mt-10 border-t border-slate-800 pt-6 text-center text-sm text-slate-500">
          © {new Date().getFullYear()} Burhani Electricals. All rights reserved.
        </div>
      </div>
    </footer>
  )
}

export default Footer
