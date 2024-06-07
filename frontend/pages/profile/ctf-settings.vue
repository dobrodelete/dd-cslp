<template>
    <div>
      <h1>CTF Settings</h1>
      <!-- CTF Settings Form -->
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useStore } from '@/store'
  
  const ctfSettings = ref(null)
  const store = useStore()
  
  onMounted(async () => {
    const response = await $fetch('/api/v1/ctf/settings', {
      headers: { Authorization: `Bearer ${store.state.token}` }
    })
    ctfSettings.value = response
  })
  </script>
  