import React from 'react'
import { Phone, MapPin, Clock, MessageCircle } from 'lucide-react'

const Contact: React.FC = () => {
  return (
    <section id="contact" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-brand-600 font-semibold tracking-wide uppercase text-sm">Get In Touch</h2>
          <p className="mt-2 text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">Contact Us</p>
          <p className="mt-4 max-w-2xl text-xl text-slate-500 mx-auto">
            Reach out to Mr. Husain M Vankanerwala for fast, affordable repairs.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
          <div className="bg-brand-50 rounded-xl p-8 text-center border border-brand-100 hover:shadow-lg transition-shadow">
            <div className="inline-flex items-center justify-center w-14 h-14 bg-brand-600 rounded-full mb-5">
              <Phone className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-lg font-bold text-slate-900 mb-2">Call / WhatsApp</h3>
            <a href="tel:+918780514062" className="text-brand-600 font-semibold text-lg hover:text-brand-700 transition-colors">
              +91 87805 14062
            </a>
          </div>

          <div className="bg-brand-50 rounded-xl p-8 text-center border border-brand-100 hover:shadow-lg transition-shadow">
            <div className="inline-flex items-center justify-center w-14 h-14 bg-brand-600 rounded-full mb-5">
              <MapPin className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-lg font-bold text-slate-900 mb-2">Location</h3>
            <p className="text-slate-600">Surat, Gujarat, India</p>
          </div>

          <div className="bg-brand-50 rounded-xl p-8 text-center border border-brand-100 hover:shadow-lg transition-shadow">
            <div className="inline-flex items-center justify-center w-14 h-14 bg-brand-600 rounded-full mb-5">
              <Clock className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-lg font-bold text-slate-900 mb-2">Working Hours</h3>
            <p className="text-slate-600">Mon – Sat: 9AM – 8PM</p>
          </div>
        </div>

        <div className="mt-12 text-center">
          <a
            href="https://wa.me/918780514062"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center px-8 py-4 bg-green-500 text-white font-bold rounded-xl hover:bg-green-600 transition-colors shadow-lg text-lg"
          >
            <MessageCircle className="w-6 h-6 mr-3" />
            Chat on WhatsApp
          </a>
        </div>
      </div>
    </section>
  )
}

export default Contact
