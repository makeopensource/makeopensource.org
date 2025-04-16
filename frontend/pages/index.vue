<script setup lang="ts">
const router = useRouter()
</script>

<template>
  <PageContainer>
    <h1>Welcome to MakeOpenSource!</h1>
    <p>We are the University at Buffalo's official open-source software club.</p>
    <Button label="Get Involved!" @click="router.push('/projects')" />
  </PageContainer>
</template>

<style scoped>

</style>