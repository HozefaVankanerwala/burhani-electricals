import React, { useEffect } from 'react'
import { Fan, Wind, Cpu, Wrench, Flame, Droplets, PenTool, ArrowLeft } from 'lucide-react'
import { services } from '../data'

const iconMap: Record<string, React.ReactNode> = {
  fan: <Fan className="w-7 h-7" />,
  wind: <Wind className="w-7 h-7" />,
  cpu: <Cpu className="w-7 h-7" />,
  wrench: <Wrench className="w-7 h-7" />,
  flame: <Flame className="w-7 h-7" />,
  droplets: <Droplets className="w-7 h-7" />,
}

const ServicesPage: React.FC = () => {
  useEffect(() => { window.scrollTo(0, 0) }, [])

  return (
    <div className="py-24 bg-slate-50 min-h-screen">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <a href="#" className="inline-flex items-center text-brand-600 hover:text-brand-700 font-medium mb-6">
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Home
          </a>
          <h1 className="text-3xl md:text-5xl font-extrabold text-slate-900 mb-6">All Repair Services</h1>
          <p className="max-w-3xl mx-auto text-xl text-slate-600">
            Comprehensive repair solutions for your home and office appliances by Burhani Electricals.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service) => (
            <div key={service.id} className="bg-white rounded-xl shadow-lg overflow-hidden border border-slate-100 flex flex-col hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1">
              <div className="p-8 flex-grow">
                <div className="flex items-center mb-6">
                  <div className="p-3 bg-brand-100 rounded-lg text-brand-600">
                    {iconMap[service.icon]}
                  </div>
                  <h3 className="ml-4 text-xl font-bold text-slate-900">{service.title}</h3>
                </div>
                <p className="text-slate-600 leading-relaxed">{service.description}</p>
              </div>
              <div className="px-8 py-4 bg-slate-50 border-t border-slate-100 flex justify-between items-center">
                <span className="text-sm font-medium text-brand-600 flex items-center">
                  <PenTool className="w-4 h-4 mr-2" />
                  Service Available
                </span>
                <span className="text-xs font-semibold px-2 py-1 bg-brand-100 text-brand-700 rounded uppercase">
                  {service.category}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default ServicesPage
