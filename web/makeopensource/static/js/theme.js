/**
 * Theme Management System
 * Handles dark mode theme selection with localStorage persistence and system preference detection
 * Prevents flash of unstyled theme by applying theme before page renders
 */

const THEME_STORAGE_KEY = "theme-preference";
const VALID_THEMES = ["light", "dark", "auto"];
const THEME_CLASS = "dark-theme";

/**
 * Get the user's theme preference from localStorage, defaulting to "auto"
 * @returns {string} - "light", "dark", or "auto"
 */
function getStoredTheme() {
    const theme = localStorage.getItem(THEME_STORAGE_KEY);

    if (!theme) return "auto";

    return VALID_THEMES.includes(theme) ? theme : "auto";
}

/**
 * Get the effective theme based on preference and system settings
 * @param {string} preference - "light", "dark", or "auto"
 * @returns {string} - "light" or "dark"
 */
function getEffectiveTheme(preference) {
    if (preference === "auto") {
        return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }
    return preference;
}

/**
 * Apply the theme to the body
 * @param {string} theme - "light" or "dark"
 */
function applyTheme(theme) {
    const isDark = theme === "dark";
    document.body.classList.toggle(THEME_CLASS, isDark);
}

/**
 * Set the user's theme preference and save it to localStorage
 * @param {string} preference - "light", "dark", or "auto"
 */
function setThemePreference(preference) {
    if (!VALID_THEMES.includes(preference)) {
        preference = "auto";
    }

    // Store in localStorage
    localStorage.setItem(THEME_STORAGE_KEY, preference);

    // Apply the effective theme
    const effectiveTheme = getEffectiveTheme(preference);
    applyTheme(effectiveTheme);

    // Update button icon
    updateThemeIcon(preference);
}

/**
 * Update the theme toggle button to show the correct icon
 * @param {string} preference - Current theme preference
 */
function updateThemeIcon(preference) {
    const button = document.getElementById("theme-toggle-btn");
    if (!button) {
        // Button doesn't exist yet, retry after a short delay
        setTimeout(() => updateThemeIcon(preference), 50);
        return;
    }

    // Hide all icons
    const icons = button.querySelectorAll(".theme-icon");
    icons.forEach(icon => icon.style.display = "none");

    // Show the current preference icon
    const currentIcon = button.querySelector(`[data-theme="${preference}"]`);
    if (currentIcon) {
        currentIcon.style.display = "block";
    }
}

/**
 * Initialize theme system
 * This should be called as early as possible to prevent theme flash
 */
function initializeTheme() {
    const preference = getStoredTheme();
    const effectiveTheme = getEffectiveTheme(preference);
    applyTheme(effectiveTheme);
    updateThemeIcon(preference);
}

/**
 * Cycle to the next theme option
 */
function toggleTheme() {
    const current = getStoredTheme();
    const nextTheme = current === "light" ? "dark" : current === "dark" ? "auto" : "light";
    setThemePreference(nextTheme);
}

// Listen for system theme changes when in "auto" mode
if (window.matchMedia) {
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (e) => {
        const preference = getStoredTheme();
        if (preference === "auto") {
            const effectiveTheme = e.matches ? "dark" : "light";
            applyTheme(effectiveTheme);
        }
    });
}

// Initialize theme immediately when script loads
initializeTheme();
