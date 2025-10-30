/**
 * Button Component
 * 
 * This is a reusable UI component for a styled button.
 * Using reusable components ensures consistent styling and behavior across the app.
 * 
 * Props:
 *   - children: The button text or content
 *   - variant: The button style (primary, secondary, danger)
 *   - size: The button size (sm, md, lg)
 *   - onClick: Function to call when clicked
 *   - disabled: Whether the button is disabled
 *   - ...rest: Any other props (className, type, etc.)
 */

import React from 'react';

function Button({ 
  children, 
  variant = 'primary', 
  size = 'md', 
  onClick, 
  disabled = false,
  className = '',
  ...rest 
}) {
  /**
   * Base styles that all buttons share
   */
  const baseStyles = 'font-medium rounded-lg transition-colors focus:outline-none focus:ring-2';

  /**
   * Variant styles (color schemes)
   */
  const variantStyles = {
    primary: 'bg-blue-600 hover:bg-blue-700 text-white focus:ring-blue-500',
    secondary: 'bg-gray-600 hover:bg-gray-700 text-white focus:ring-gray-500',
    danger: 'bg-red-600 hover:bg-red-700 text-white focus:ring-red-500',
    outline: 'border border-blue-600 text-blue-600 hover:bg-blue-50 focus:ring-blue-500',
  };

  /**
   * Size styles
   */
  const sizeStyles = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
  };

  /**
   * Disabled styles
   */
  const disabledStyles = 'opacity-50 cursor-not-allowed';

  /**
   * Combine all styles
   */
  const buttonClassName = `
    ${baseStyles}
    ${variantStyles[variant] || variantStyles.primary}
    ${sizeStyles[size] || sizeStyles.md}
    ${disabled ? disabledStyles : ''}
    ${className}
  `.trim();

  return (
    <button
      className={buttonClassName}
      onClick={onClick}
      disabled={disabled}
      {...rest}
    >
      {children}
    </button>
  );
}

export default Button;
