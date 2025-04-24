<script setup lang="ts">
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  imageUrl: {
    type: [String, undefined],
    required: false,
  },
  link: {
    type: [String, undefined],
    required: false,
  },
})

const router = useRouter()

</script>

<template>
  <div class="card">
    <div style="height: 64px; background-color: var(--p-primary-500)">
      <img v-if="props.imageUrl"
           alt="Project image"
           height="64px"
           width="300px"
           style="object-fit: fill"
           :src="props.imageUrl"
      />
    </div>
    <div class="body">
      <div style="font-size: 20px;">{{ props.title }}</div>
      <div style="display: flex; flex-direction: column; flex: 1;">
        <div>
          <p style="margin-top: 8px; margin-bottom: 8px;">{{ props.description }}</p>
        </div>
        <div style="flex: 1;"/>
        <div v-if="props.link">
          <div style="width: 100%;">
            <Button label="Learn more!" outlined @click="router.push(props.link)" style="width: 100%;"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.card {
  width: 300px;
  height: 300px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.body {
  display: flex;
  flex-direction: column;
  padding: 16px;
  gap: 8px;
  flex: 1;
}

</style>