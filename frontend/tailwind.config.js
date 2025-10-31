/** @type {import('tailwindcss').Config} */

// Tailwind CSS Configuration File

export default {
  // CRITICAL: The 'content' array tells Tailwind where to look for class names
  // Tailwind scans these files and only includes CSS for classes that are actually used
  // This keeps the final CSS bundle small and fast
  //
  // Why this is important:
  //   - If you add a new .jsx file, Tailwind will automatically scan it
  //   - If you use a class like "bg-blue-500", Tailwind includes that CSS
  //   - If you never use a class, it won't be in the final CSS (tree-shaking)
  //
  // Pattern explanation:
  //   "./index.html" - The root HTML file
  //   "./src/**/*.{js,ts,jsx,tsx}" - All JavaScript/TypeScript files in src/ (and subdirectories)
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  
  // Theme customization (optional)
  // You can extend Tailwind's default theme here
  theme: {
    extend: {
      // Example: Add custom colors
      // colors: {
      //   'brand-blue': '#1E40AF',
      // }
    },
  },
  
  // Plugins (optional)
  // Add Tailwind plugins for additional functionality
  plugins: [],
}
