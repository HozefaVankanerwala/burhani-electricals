import React from 'react';
import { PenTool } from 'lucide-react';
import { services } from '../data';

const Services: React.FC = () => {
  return (
    <section id="services" className="py-20 bg-slate-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-brand-600 font-semibold tracking-wide uppercase text-sm">What We Do</h2>
          <p className="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-slate-900 sm:text-4xl">
            Our Premium Services
          </p>
          <p className="mt-4 max-w-2xl text-xl text-slate-500 mx-auto">
            We specialize in extending the life of your electrical appliances with quality parts and expert workmanship.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service) => (
            <div 
              key={service.id} 
              className="bg-white rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden group border border-slate-100"
            >
              <div className="p-8">
                <div className="inline-flex items-center justify-center p-3 bg-brand-100 rounded-lg text-brand-600 group-hover:bg-brand-500 group-hover:text-white transition-colors duration-300 mb-5">
                  {service.icon}
                </div>
                <h3 className="text-xl font-bold text-slate-900 mb-3">{service.title}</h3>
                <p className="text-slate-600 leading-relaxed">
                  {service.description}
                </p>
              </div>
              <div className="px-8 py-4 bg-slate-50 border-t border-slate-100 group-hover:bg-brand-50 transition-colors">
                <span className="text-sm font-medium text-brand-600 flex items-center">
                  <PenTool className="w-4 h-4 mr-2" />
                  Expert Repair
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Services;