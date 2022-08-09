/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './application/views/**/*.jinja2',
      './application/assets/js/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('@tailwindcss/typography'),
      require('daisyui')
  ],
}