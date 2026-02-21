import React, { useState, useRef, useEffect } from 'react'
import { MessageCircle, Send, X, Bot } from 'lucide-react'
import { ChatMessage } from '../types'

const GEMINI_API_KEY = (import.meta as any).env?.VITE_GEMINI_API_KEY || ''

const AIChat: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false)
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      role: 'model',
      text: "Hello! I'm the Burhani Electricals Assistant. Ask me about fan issues, mixer problems, or how we can help you!",
      timestamp: new Date(),
    },
  ])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isOpen])

  const handleSend = async () => {
    if (!input.trim()) return

    const userMsg: ChatMessage = { role: 'user', text: input, timestamp: new Date() }
    setMessages((prev) => [...prev, userMsg])
    setInput('')
    setIsLoading(true)

    try {
      if (!GEMINI_API_KEY) throw new Error('No API key')

      const res = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            system_instruction: {
              parts: [{
                text: `You are the friendly AI assistant for "Burhani Electricals" owned by Mr. Husain M Vankanerwala. 
Services: Repairing and rewinding of all types of fans (Ceiling, Wall, Table, Cabin, Pedestal, Stand, Tower, Exhaust, Mini Exhaust, Talvar, Farata, Lift fans), Mixer/Blender, Iron, and Geyser repairing.
Always conclude by suggesting the user contact Mr. Husain at +91 8780514062. Keep answers concise and polite.`
              }]
            },
            contents: [{ parts: [{ text: input }] }],
            generationConfig: { temperature: 0.7, maxOutputTokens: 300 },
          }),
        }
      )
      const data = await res.json()
      const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || "I'm having trouble right now. Please call us at +91 8780514062!"
      setMessages((prev) => [...prev, { role: 'model', text, timestamp: new Date() }])
    } catch {
      setMessages((prev) => [...prev, { role: 'model', text: 'Please contact Husain directly at +91 8780514062.', timestamp: new Date() }])
    }

    setIsLoading(false)
  }

  return (
    <>
      <button
        onClick={() => setIsOpen(true)}
        className={`fixed bottom-20 right-6 z-40 p-4 rounded-full shadow-lg transition-all duration-300 bg-indigo-600 text-white hover:bg-indigo-700 ${isOpen ? 'scale-0' : 'scale-100'}`}
        aria-label="Open AI Assistant"
      >
        <Bot className="w-6 h-6" />
      </button>

      <div
        className={`fixed bottom-20 right-6 z-50 w-full sm:w-96 bg-white rounded-2xl shadow-2xl overflow-hidden flex flex-col transition-all duration-300 origin-bottom-right border border-slate-200 ${
          isOpen ? 'scale-100 opacity-100' : 'scale-0 opacity-0 pointer-events-none'
        }`}
        style={{ maxHeight: 'calc(100vh - 120px)', height: '500px' }}
      >
        <div className="bg-indigo-600 p-4 flex justify-between items-center text-white">
          <div className="flex items-center space-x-2">
            <Bot className="w-5 h-5" />
            <h3 className="font-semibold">Burhani Electricals Assistant</h3>
          </div>
          <button onClick={() => setIsOpen(false)} className="hover:bg-indigo-500 rounded-full p-1 transition">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-4 bg-slate-50 space-y-4">
          {messages.map((msg, idx) => (
            <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-[85%] p-3 rounded-2xl text-sm shadow-sm ${
                msg.role === 'user'
                  ? 'bg-indigo-600 text-white rounded-br-none'
                  : 'bg-white text-slate-800 border border-slate-200 rounded-bl-none'
              }`}>
                {msg.text}
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-white border border-slate-200 p-3 rounded-2xl rounded-bl-none shadow-sm">
                <div className="flex space-x-2">
                  <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-75"></div>
                  <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-150"></div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 bg-white border-t border-slate-100">
          <div className="flex items-center space-x-2">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSend()}
              placeholder="Ask about fan repair..."
              className="flex-1 border border-slate-300 rounded-full px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
            <button
              onClick={handleSend}
              disabled={isLoading || !input.trim()}
              className="p-2 bg-indigo-600 text-white rounded-full hover:bg-indigo-700 disabled:opacity-50 transition"
            >
              <Send className="w-4 h-4" />
            </button>
          </div>
          <p className="text-center mt-2 text-[10px] text-slate-400">AI can make mistakes. Contact Husain for official quotes.</p>
        </div>
      </div>
    </>
  )
}

export default AIChat
