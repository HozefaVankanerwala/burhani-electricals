import React from 'react';
import { Wind, Cpu, Flame, Droplets, Fan, Wrench } from 'lucide-react';
import { ServiceItem } from './types';

export const services: ServiceItem[] = [
  {
    id: '1',
    title: 'Ceiling Fan Repair & Rewinding',
    description: 'Expert repair and rewinding of all types of ceiling fans. We fix noise issues, speed problems, motor burnouts, and more to restore full performance.',
    icon: React.createElement(Fan, { className: 'w-7 h-7' }),
    category: 'fan',
  },
  {
    id: '2',
    title: 'Table, Wall & Pedestal Fans',
    description: 'Complete repair service for table fans, wall fans, pedestal fans, stand fans, cabin fans, and tower fans. All brands and models accepted.',
    icon: React.createElement(Wind, { className: 'w-7 h-7' }),
    category: 'fan',
  },
  {
    id: '3',
    title: 'Exhaust & Industrial Fans',
    description: 'Repair and rewinding of exhaust fans, mini exhaust fans, talvar fans, farata fans, lift fans, and other industrial ventilation fans.',
    icon: React.createElement(Cpu, { className: 'w-7 h-7' }),
    category: 'fan',
  },
  {
    id: '4',
    title: 'Mixer & Blender Repair',
    description: 'Professional repair for all brands of mixers and blenders. We fix motor failures, blade issues, speed control problems, and electrical faults.',
    icon: React.createElement(Wrench, { className: 'w-7 h-7' }),
    category: 'appliance',
  },
  {
    id: '5',
    title: 'Iron Repair',
    description: 'Fast and reliable repair for all types of irons — steam irons, dry irons, and automatic irons. Fixing heating element, thermostat, and cord issues.',
    icon: React.createElement(Flame, { className: 'w-7 h-7' }),
    category: 'appliance',
  },
  {
    id: '6',
    title: 'Geyser Repair',
    description: 'Expert geyser and water heater repair service. We handle thermostat issues, heating element replacement, leaks, and all electrical problems.',
    icon: React.createElement(Droplets, { className: 'w-7 h-7' }),
    category: 'appliance',
  },
];
