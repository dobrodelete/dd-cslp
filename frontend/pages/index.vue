<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <h1 class="text-3xl font-bold text-blue-600 mb-2">dd-CSLP</h1>
      <p class="text-center text-gray-700 max-w-prose mb-4">
        ddCSLP project.
      </p>
      <div class="space-x-4">
        <a href="https://github.com/dobrodelete/dd-cslp" class="text-blue-500 hover:underline">Исходный код на GitHub</a>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
const layout = "default"
</script>

<style scoped>
/* Стили, если они нужны, уже встроены через Tailwind CSS */
</style>