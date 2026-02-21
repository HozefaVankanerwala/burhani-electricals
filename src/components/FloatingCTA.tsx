import React from 'react';
import { MessageCircle, Phone } from 'lucide-react';

const FloatingCTA: React.FC = () => {
  const whatsappNumber = "918780514062";
  const whatsappUrl = `https://wa.me/${whatsappNumber}?text=Hello%20Burhani%20Electrical's,%20I%20need%20assistance%20with%20a%20repair.`;

  return (
    <div className="fixed bottom-6 right-6 z-50 flex flex-col gap-4">
      {/* Phone Dialer */}
      <a
        href="tel:+918780514062"
        className="group flex items-center justify-center w-14 h-14 bg-brand-500 rounded-full shadow-lg hover:bg-brand-600 hover:scale-110 transition-all duration-300 text-white relative"
        title="Call Now"
      >
        <Phone className="w-6 h-6 fill-current" />
        <span className="absolute right-full mr-3 px-2 py-1 bg-gray-900 text-white text-xs rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">
          Call Husain
        </span>
      </a>

      {/* WhatsApp */}
      <a
        href={whatsappUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="group flex items-center justify-center w-14 h-14 bg-[#25D366] rounded-full shadow-lg hover:bg-[#20bd5a] hover:scale-110 transition-all duration-300 text-white relative"
        title="Chat on WhatsApp"
      >
        <MessageCircle className="w-7 h-7 fill-current" />
        <span className="absolute right-full mr-3 px-2 py-1 bg-gray-900 text-white text-xs rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">
          WhatsApp Us
        </span>
      </a>
    </div>
  );
};

export default FloatingCTA;