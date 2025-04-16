const STORAGE_KEY = 'darkThemeEnabled'
const DARK_THEME_CLASS = 'dark-theme'

export function useDarkTheme() {
    const isDark = ref(false)

    function setDarkTheme(enabled: boolean) {
        isDark.value = enabled
        localStorage.setItem(STORAGE_KEY, enabled)
        document.documentElement.classList.toggle(DARK_THEME_CLASS, enabled)
    }

    function toggleDarkTheme() {
        setDarkTheme(!isDark.value)
    }

    function loadThemePreference() {
        const stored: string | null = localStorage.getItem(STORAGE_KEY)
        if (stored == null) {
            // If no preference is stored, use the system preference
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            setDarkTheme(prefersDark)
        } else {
            setDarkTheme(stored === 'true')
        }
    }

    onMounted(loadThemePreference)

    return {isDark, setDarkTheme, toggleDarkTheme}

}