/**
 * Card Component
 * 
 * This is a reusable UI component for a styled card container.
 * Cards are commonly used to group related content with consistent styling.
 * 
 * Props:
 *   - children: The card content
 *   - title: Optional card title
 *   - className: Additional CSS classes
 */

import React from 'react';

function Card({ children, title, className = '' }) {
  return (
    <div className={`bg-white rounded-lg shadow p-6 ${className}`.trim()}>
      {title && (
        <h3 className="text-xl font-semibold mb-4 text-gray-800">
          {title}
        </h3>
      )}
      {children}
    </div>
  );
}

export default Card;
