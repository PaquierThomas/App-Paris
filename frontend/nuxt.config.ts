// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ['~/assets/css/reset.css'],
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      apiBase: 'http://localhost:8000',
    },
  },

  // Proxy pour éviter les erreurs CORS en développement
  routeRules: {
    '/api/**': { proxy: 'http://localhost:8000/**' },
  },
})
