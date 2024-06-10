<template>
  <div class="bg-gray-800 text-white p-3 ">
    <ul class="flex space-x-4 justify-center">
      <nuxt-link to="/" class="px-3 hover:bg-gray-700 py-2 rounded">CSLP</nuxt-link>
        <nuxt-link to="/task-tracker" class="px-3 hover:bg-gray-700 py-2 rounded">Task Tracker</nuxt-link>
        <nuxt-link to="/task-tracker/settings" class="px-3 hover:bg-gray-700 py-2 rounded">Настройки</nuxt-link>
    </ul>
  </div>
</template>

<script setup>
</script>

<style scoped>
.navbar { background-color: #333; }
</style>
