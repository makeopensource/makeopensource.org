<script setup lang="ts">

</script>

<template>
  <div class="page">
    <div class="content">
      <slot/>
    </div>
  </div>
</template>

<style scoped>
.page {
  margin: 0 12px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  .content {
    width: 100%;
    max-width: 1200px;
  }
}

</style>