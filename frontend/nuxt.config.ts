// https://nuxt.com/docs/api/configuration/nuxt-config

import {theme} from './theme'

export default defineNuxtConfig({
    compatibilityDate: '2024-11-01',
    devtools: {enabled: true},

    modules: [
        '@nuxt/eslint',
        '@nuxt/icon',
        '@nuxt/image',
        '@nuxt/fonts',
        '@primevue/nuxt-module'
    ],
    primevue: {
        options: {
            theme: {
                preset: theme,
                options: {
                    darkModeSelector: 'dark-theme',
                }
            }
        }
    }
})