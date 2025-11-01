/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Primary Palette: Bright blues, greens, and white
        primary: {
          50: '#e6f7ff',
          100: '#b3e5ff',
          200: '#80d4ff',
          300: '#4dc2ff',
          400: '#1ab0ff',
          500: '#0099e6',  // Main bright blue
          600: '#0077b3',
          700: '#005580',
          800: '#00334d',
          900: '#00111a',
        },
        secondary: {
          50: '#e6f9f0',
          100: '#b3efd4',
          200: '#80e5b8',
          300: '#4ddb9c',
          400: '#1ad180',
          500: '#00b359',  // Main bright green
          600: '#008f47',
          700: '#006b35',
          800: '#004723',
          900: '#002311',
        },
        accent: {
          50: '#fff5e6',
          100: '#ffe0b3',
          200: '#ffcb80',
          300: '#ffb64d',
          400: '#ffa11a',
          500: '#ff8c00',  // Orange energy
          600: '#cc7000',
          700: '#995400',
          800: '#663800',
          900: '#331c00',
        },
        yellow: {
          50: '#fffce6',
          100: '#fff7b3',
          200: '#fff280',
          300: '#ffed4d',
          400: '#ffe81a',
          500: '#ffe300',  // Yellow highlights
          600: '#ccb600',
          700: '#998900',
          800: '#665c00',
          900: '#332e00',
        },
      },
      fontFamily: {
        headline: ['Poppins', 'Montserrat', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
      },
      boxShadow: {
        'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
      },
      animation: {
        'float': 'float 3s ease-in-out infinite',
        'slide-up': 'slideUp 0.5s ease-out',
        'fade-in': 'fadeIn 0.6s ease-out',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        slideUp: {
          '0%': { transform: 'translateY(100px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
