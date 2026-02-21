import React from 'react';
import { Zap } from 'lucide-react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-slate-900 text-white py-12 border-t border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center">
        
        <div className="flex items-center mb-6 md:mb-0">
          <div className="flex items-center justify-center px-2 py-1.5 bg-brand-500 rounded-lg mr-3 text-slate-900 shadow-sm">
             <span className="font-bold text-xl leading-none tracking-tighter">B</span>
             <Zap className="w-5 h-5 fill-current" />
             <span className="font-bold text-xl leading-none tracking-tighter">E</span>
          </div>
          <div>
            <h3 className="text-xl font-bold">Burhani Electrical's</h3>
            <p className="text-slate-400 text-sm">Best Service in Repairing & Rewinding</p>
          </div>
        </div>

        <div className="text-center md:text-right">
          <p className="text-slate-400 text-sm">
            &copy; {new Date().getFullYear()} Burhani Electrical's. All rights reserved.
          </p>
          <p className="text-slate-500 text-xs mt-1">
            Owned by Husain M Vankanerwala
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;