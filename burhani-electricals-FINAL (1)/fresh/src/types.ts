export interface ServiceItem {
  id: string
  title: string
  description: string
  icon: string
  category: 'fan' | 'appliance'
}

export interface ChatMessage {
  role: 'user' | 'model'
  text: string
  timestamp: Date
}
