<template>
  <!-- <div :class="{'w-64': isOpen, 'w-0': !isOpen}" class="fixed h-full bg-gray-800 text-white transition-width duration-300 overflow-hidden">
    <button @click="toggle" class="p-4 focus:outline-none">
      <svg v-if="!isOpen" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
      <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
    </button>
    <ul v-if="isOpen" class="mt-2">
      <li><nuxt-link to="/ddctf" class="block p-4 hover:bg-gray-700">DDCTF</nuxt-link></li>
      <li><nuxt-link to="/blog" class="block p-4 hover:bg-gray-700">Blog</nuxt-link></li>
      <li><nuxt-link to="/task-tracker" class="block p-4 hover:bg-gray-700">Task Tracker</nuxt-link></li>
      <li><nuxt-link to="/profile" class="block p-4 hover:bg-gray-700">Profile</nuxt-link></li>
    </ul>
  </div> -->
  <div>
    <slot />
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isOpen = ref(true);

const toggle = () => {
  isOpen.value = !isOpen.value;
};
</script>

<style scoped>
.transition-width {
  transition-property: width;
}
</style>
