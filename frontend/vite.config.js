import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Vite Configuration File
// https://vitejs.dev/config/

export default defineConfig({
  // Plugins extend Vite's functionality
  // The 'react' plugin enables React Fast Refresh (hot module replacement)
  // This allows you to see changes instantly without losing component state
  plugins: [react()],
  
  // Server configuration for development
  server: {
    port: 5173,  // Default Vite dev server port
    // Uncomment to open browser automatically on start
    // open: true,
  }
})
