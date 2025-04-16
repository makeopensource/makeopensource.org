import Aura from '@primeuix/themes/aura'
import {definePreset} from '@primeuix/themes'

export const theme = definePreset(Aura, {
    semantic: {
        primary: {
            50: '#fbca8e',
            100: '#fabf77',
            200: '#f9b461',
            300: '#f9a94a',
            400: '#f89f34',
            500: '#f7941d',
            600: '#de851a',
            700: '#c67617',
            800: '#ad6814',
            900: '#945911',
            950: '#7c4a0f'
        },
        colorScheme: {
            light: {
                primary: {
                    color: '{primary.500}',
                    hoverColor: '{primary.400}',
                    activeColor: '{primary.300}',
                    inverseColor: '{zinc.900}',
                    contrastColor: '{zinc.900}'
                },
            },
            dark: {
                primary: {
                    color: '{primary.500}',
                    hoverColor: '{primary.400}',
                    activeColor: '{primary.300}',
                    inverseColor: '{zinc.900}',
                    contrastColor: '{zinc.900}'
                },
            }
        }
    }
})