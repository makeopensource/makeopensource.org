<script setup lang="ts">
const isOnProjectsPage = computed(() => {
  return useRoute().path.startsWith('/projects')
})
</script>

<template>
  <nav>
    <NuxtLink class="nav-link" active-class="active" to="/">
      <img class="logo" src="/logo.png" alt="Logo"/>
      MakeOpenSource
    </NuxtLink>
    <NuxtLink class="nav-link" :class="{'active': isOnProjectsPage}" to="/projects">Projects</NuxtLink>
    <NuxtLink class="nav-link" active-class="active" to="/about">About</NuxtLink>
    <div class="separator"/>
    <ThemeSelectorButton/>
  </nav>
</template>

<style scoped>

nav {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  height: 48px;
  flex-direction: row;
  width: 100%;
  max-width: 1200px;
}

.logo {
  height: 32px;
  width: 32px;
  border-radius: 5px;
}

.nav-link {
  display: flex;
  gap: 12px;
  align-items: center;
  color: black;
  padding: 8px 4px;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  height: 48px;

  &.active {
    border-bottom: 2px solid var(--p-primary-color);
  }
}

.separator {
  flex-grow: 1;
}

</style>