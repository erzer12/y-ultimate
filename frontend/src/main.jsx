import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import './index.css'

/**
 * React Application Entry Point
 * 
 * This is the first JavaScript file that runs when the app starts.
 * It "boots" the React application by mounting it to the DOM.
 * 
 * Key components:
 *   1. ReactDOM.createRoot(): Creates a React root that can render React components
 *   2. root.render(): Renders the React component tree into the DOM
 *   3. <BrowserRouter>: Enables client-side routing (React Router)
 *   4. <App />: The root component of your application
 * 
 * Why wrap <App /> with <BrowserRouter>?
 *   - BrowserRouter provides routing context to all child components
 *   - It enables navigation without full page reloads
 *   - It synchronizes the UI with the browser's URL
 *   - All <Route>, <Link>, and useNavigate() hooks depend on this
 */

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* BrowserRouter enables routing for the entire app */}
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
)
