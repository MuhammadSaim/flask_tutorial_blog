/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './application/views/**/*.jinja2',
      './application/assets/js/**/*.js',
      './application/forms/**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('@tailwindcss/typography'),
      require('daisyui')
  ],
}