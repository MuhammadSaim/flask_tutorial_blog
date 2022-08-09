const mix = require('laravel-mix');


mix.options({
  fileLoaderDirs: {
    fonts: "assets/fonts",
    images: "assets/images",
  },
});



mix.js("src/js/app.js", "application/assets/js")
  .postCss("src/css/app.css", "application/assets/css", [
    require("tailwindcss"),
  ]);