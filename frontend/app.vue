<template>
  <div class="page">
    <header>
      <NavigationHeader/>
    </header>
    <main>
      <NuxtPage/>
    </main>
  </div>
</template>

<style scoped lang="scss">
.page {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
</style>

<style lang="scss">

header {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin: 0 12px;
}

main {
  flex: 1;
}

body {
  margin: 0;
  font-family: Arial, sans-serif;
}

html {
  a, a:visited {
    color: var(--p-sky-800);
  }

  a:hover {
    color: var(--p-sky-700);
  }

  a:active, {
    color: var(--p-sky-600);
  }


  &.dark-theme {
    a, a:visited {
      color: var(--p-primary-color);
    }

    a:hover {
      color: var(--p-primary-300);
    }

    a:active, {
      color: var(--p-primary-100);
    }
  }
}


</style>

<script setup lang="ts">
</script>