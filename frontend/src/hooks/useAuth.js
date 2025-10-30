/**
 * Custom Hook: useAuth
 * 
 * This custom hook will simplify accessing the AuthContext.
 * 
 * NOTE: The useAuth hook is already defined in AuthContext.jsx,
 * so this file is optional. Some projects prefer to keep hooks
 * in a separate hooks/ directory for better organization.
 * 
 * If you prefer this structure, you would export the useAuth hook
 * from here instead of from AuthContext.jsx.
 * 
 * For now, this file re-exports the useAuth hook from AuthContext.
 */

export { useAuth } from '../context/AuthContext';
