import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://jonaselgammal.github.io',
  output: 'static',
  build: { assets: '_astro' },
});
