<script setup lang="ts">
  import {useDarkTheme} from "#imports";

  const theme = useDarkTheme()
</script>

<template>
  <Button
      @click="theme.toggleDarkTheme()"
      aria-label="Toggle dark theme"
  >
    T
  </Button>
</template>

<style scoped>

</style>