import React, { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Services from './components/Services'
import Contact from './components/Contact'
import Footer from './components/Footer'
import FloatingCTA from './components/FloatingCTA'
import AIChat from './components/AIChat'
import ServicesPage from './components/ServicesPage'

const App: React.FC = () => {
  const [currentHash, setCurrentHash] = useState(window.location.hash)

  useEffect(() => {
    const handleHashChange = () => setCurrentHash(window.location.hash)
    window.addEventListener('hashchange', handleHashChange)
    return () => window.removeEventListener('hashchange', handleHashChange)
  }, [])

  useEffect(() => {
    if (currentHash === '#contact') {
      setTimeout(() => {
        document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })
      }, 100)
    } else if (currentHash === '' || currentHash === '#') {
      window.scrollTo({ top: 0, behavior: 'smooth' })
    }
  }, [currentHash])

  const isServicesPage = currentHash === '#all-services'

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans">
      <Navbar />
      <main className="flex-grow">
        {isServicesPage ? (
          <ServicesPage />
        ) : (
          <>
            <Hero />
            <Services />
            <Contact />
          </>
        )}
      </main>
      <Footer />
      <FloatingCTA />
      <AIChat />
    </div>
  )
}

export default App
