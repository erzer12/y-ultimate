import React from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';
import { Disc3, Users, TrendingUp, Heart } from 'lucide-react';

const HeroSection = () => {
  const { scrollY } = useScroll();
  
  // Parallax effects for different layers
  const skyY = useTransform(scrollY, [0, 500], [0, 150]);
  const fieldY = useTransform(scrollY, [0, 500], [0, 100]);
  const discRotate = useTransform(scrollY, [0, 500], [0, 180]);
  const discY = useTransform(scrollY, [0, 500], [0, -200]);

  return (
    <div className="relative h-screen overflow-hidden bg-gradient-to-b from-primary-50 via-secondary-50 to-white">
      {/* Sky Layer - slowest */}
      <motion.div 
        style={{ y: skyY }}
        className="absolute inset-0 bg-gradient-to-b from-primary-200 to-primary-50 opacity-60"
      >
        {/* Decorative clouds */}
        <div className="absolute top-20 left-10 w-32 h-16 bg-white opacity-40 rounded-full blur-xl"></div>
        <div className="absolute top-40 right-20 w-40 h-20 bg-white opacity-30 rounded-full blur-xl"></div>
      </motion.div>

      {/* Field Layer - medium speed */}
      <motion.div 
        style={{ y: fieldY }}
        className="absolute bottom-0 left-0 right-0 h-1/3 bg-gradient-to-t from-secondary-200 to-secondary-100 opacity-50"
      >
        {/* Field lines */}
        <div className="absolute bottom-20 left-0 right-0 h-1 bg-white opacity-30"></div>
        <div className="absolute bottom-40 left-0 right-0 h-0.5 bg-white opacity-20"></div>
      </motion.div>

      {/* Animated Frisbee Disc */}
      <motion.div
        style={{ 
          y: discY,
          rotate: discRotate
        }}
        className="absolute top-1/3 right-1/4 z-10"
      >
        <Disc3 className="w-24 h-24 text-accent-500 drop-shadow-lg animate-float" />
      </motion.div>

      {/* Main Content */}
      <div className="relative z-20 flex flex-col items-center justify-center h-full px-4">
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center max-w-4xl"
        >
          <motion.h1 
            className="text-6xl md:text-7xl font-headline font-bold text-primary-700 mb-6"
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2, duration: 0.6 }}
          >
            Teaching Life Skills Through
            <span className="block text-secondary-600 mt-2">
              the Spirit of Ultimate
            </span>
          </motion.h1>

          <motion.p 
            className="text-xl md:text-2xl text-gray-600 mb-8 font-body"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4, duration: 0.6 }}
          >
            Empowering children from under-resourced communities through
            Ultimate Frisbee, building confidence, teamwork, and resilience.
          </motion.p>

          <motion.div 
            className="flex flex-wrap justify-center gap-6 mb-12"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6, duration: 0.6 }}
          >
            <div className="flex items-center gap-2 bg-white px-6 py-3 rounded-xl shadow-soft">
              <Users className="w-6 h-6 text-primary-500" />
              <span className="font-semibold text-gray-700">Community Programs</span>
            </div>
            <div className="flex items-center gap-2 bg-white px-6 py-3 rounded-xl shadow-soft">
              <TrendingUp className="w-6 h-6 text-secondary-500" />
              <span className="font-semibold text-gray-700">Track Progress</span>
            </div>
            <div className="flex items-center gap-2 bg-white px-6 py-3 rounded-xl shadow-soft">
              <Heart className="w-6 h-6 text-accent-500" />
              <span className="font-semibold text-gray-700">Build Character</span>
            </div>
          </motion.div>

          <motion.div 
            className="flex flex-wrap justify-center gap-4"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.8, duration: 0.6 }}
          >
            <button className="bg-primary-500 hover:bg-primary-600 text-white font-semibold px-8 py-4 rounded-xl shadow-lg transition-all duration-300 transform hover:scale-105">
              Get Started
            </button>
            <button className="bg-white hover:bg-gray-50 text-primary-600 font-semibold px-8 py-4 rounded-xl shadow-lg border-2 border-primary-500 transition-all duration-300">
              Learn More
            </button>
          </motion.div>
        </motion.div>

        {/* Scroll Indicator */}
        <motion.div
          className="absolute bottom-10"
          animate={{ y: [0, 10, 0] }}
          transition={{ repeat: Infinity, duration: 1.5 }}
        >
          <div className="w-6 h-10 border-2 border-primary-500 rounded-full flex justify-center">
            <div className="w-1 h-3 bg-primary-500 rounded-full mt-2 animate-bounce"></div>
          </div>
        </motion.div>
      </div>

      {/* Decorative SVG Players - background silhouettes */}
      <div className="absolute bottom-0 left-0 right-0 opacity-10 pointer-events-none">
        <svg viewBox="0 0 1200 300" className="w-full h-auto">
          {/* Simplified player silhouettes */}
          <ellipse cx="200" cy="280" rx="30" ry="10" fill="currentColor" className="text-primary-700" />
          <path d="M200 150 L200 250 M180 180 L220 180 M200 250 L180 280 M200 250 L220 280" 
                stroke="currentColor" strokeWidth="8" strokeLinecap="round" className="text-primary-700" />
          
          <ellipse cx="400" cy="280" rx="30" ry="10" fill="currentColor" className="text-secondary-700" />
          <path d="M400 160 L400 250 M380 190 L420 190 M400 250 L380 280 M400 250 L420 280" 
                stroke="currentColor" strokeWidth="8" strokeLinecap="round" className="text-secondary-700" />
          
          <ellipse cx="1000" cy="280" rx="30" ry="10" fill="currentColor" className="text-primary-700" />
          <path d="M1000 140 L1000 250 M980 170 L1020 170 M1000 250 L980 280 M1000 250 L1020 280" 
                stroke="currentColor" strokeWidth="8" strokeLinecap="round" className="text-primary-700" />
        </svg>
      </div>
    </div>
  );
};

export default HeroSection;
