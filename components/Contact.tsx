import React from 'react';
import { MapPin, Phone, Mail, Clock } from 'lucide-react';

const Contact: React.FC = () => {
  return (
    <section id="contact" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-slate-900 rounded-2xl shadow-2xl overflow-hidden flex flex-col md:flex-row relative">
          
          {/* Info Side with Background Image */}
          <div className="md:w-1/2 p-10 md:p-14 text-white relative overflow-hidden">
             {/* Background for Contact Info */}
             <div className="absolute inset-0 z-0">
                <img 
                  src="https://images.unsplash.com/photo-1618331835717-801e976710b2?auto=format&fit=crop&q=80" 
                  alt="Copper Coils Background" 
                  className="w-full h-full object-cover opacity-10"
                />
                <div className="absolute inset-0 bg-slate-900/90 mix-blend-multiply"></div>
             </div>

            <div className="relative z-10">
              <h2 className="text-3xl font-bold mb-6 text-brand-200">Contact Us</h2>
              <p className="mb-10 text-slate-300 text-lg">
                Need a quick repair or a quote? Reach out to Husain M Vankanerwala today. We are always happy to help!
              </p>
              
              <div className="space-y-6">
                <div className="flex items-start group">
                  <div className="bg-brand-500/20 p-3 rounded-lg mr-4 group-hover:bg-brand-500/30 transition-colors">
                    <Phone className="w-6 h-6 text-brand-300" />
                  </div>
                  <div>
                    <p className="text-sm text-slate-400 font-medium uppercase tracking-wide">Call Us</p>
                    <a href="tel:+918780514062" className="text-xl font-semibold hover:text-brand-300 transition">+91 8780514062</a>
                  </div>
                </div>

                <div className="flex items-start group">
                   <div className="bg-brand-500/20 p-3 rounded-lg mr-4 group-hover:bg-brand-500/30 transition-colors">
                    <Mail className="w-6 h-6 text-brand-300" />
                  </div>
                  <div>
                    <p className="text-sm text-slate-400 font-medium uppercase tracking-wide">Email Us</p>
                    <a href="mailto:vankanerwalahusain@gmail.com" className="text-lg font-semibold hover:text-brand-300 transition break-all">vankanerwalahusain@gmail.com</a>
                  </div>
                </div>

                <div className="flex items-start group">
                   <div className="bg-brand-500/20 p-3 rounded-lg mr-4 group-hover:bg-brand-500/30 transition-colors">
                    <Clock className="w-6 h-6 text-brand-300" />
                  </div>
                  <div>
                    <p className="text-sm text-slate-400 font-medium uppercase tracking-wide">Working Hours</p>
                    <p className="text-lg font-semibold">Mon - Sat: 9:00 AM - 8:00 PM</p>
                    <p className="text-slate-400 text-sm">Sunday Closed</p>
                  </div>
                </div>

                <div className="flex items-start group">
                   <div className="bg-brand-500/20 p-3 rounded-lg mr-4 group-hover:bg-brand-500/30 transition-colors">
                    <MapPin className="w-6 h-6 text-brand-300" />
                  </div>
                  <div>
                    <p className="text-sm text-slate-400 font-medium uppercase tracking-wide">Visit Us</p>
                    <p className="text-lg font-medium leading-snug">301, Sabri Manzil,<br/>Nr Evergreen Bakery,<br/>Navsari Bazar Main Road,<br/>Surat-395002</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Map/Image Side */}
          <div className="md:w-1/2 relative h-80 md:h-auto min-h-[400px]">
             <img 
              src="https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?auto=format&fit=crop&q=80" 
              alt="Electrical Tools and Workbench" 
              className="absolute inset-0 w-full h-full object-cover"
             />
             <div className="absolute inset-0 bg-brand-900/30 mix-blend-multiply"></div>
             <div className="absolute inset-0 flex items-center justify-center">
                <div className="bg-white/95 backdrop-blur-md p-6 rounded-xl shadow-xl m-8 text-center border-l-4 border-brand-500">
                  <h3 className="text-xl font-bold text-slate-900 mb-2">Expert Service</h3>
                  <p className="text-slate-600 italic">
                    “Repairing trust, not just machines.”<br/>
                    <span className="font-semibold text-brand-600 mt-2 block not-italic">- Husain M Vankanerwala</span>
                  </p>
                </div>
             </div>
          </div>

        </div>
      </div>
    </section>
  );
};

export default Contact;