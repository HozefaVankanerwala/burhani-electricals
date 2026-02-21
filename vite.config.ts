import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // IMPORTANT: Replace 'burhani-electrical' below with your actual GitHub repository name
  base: '/burhani-electricals/',
})
