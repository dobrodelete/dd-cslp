<template>
  <NuxtLayout :name="layout">
    <div>
      <h1>Profile</h1>
      <p>Welcome, {{ user.username }}</p>
      <nuxt-link to="/profile/ctf-settings">CTF Settings</nuxt-link>
      <nuxt-link to="/profile/blog-settings">Blog Settings</nuxt-link>
      <nuxt-link to="/profile/task-tracker-settings">Task Tracker Settings</nuxt-link>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
// import { useStore } from '@/store'

const layout = "ddctf"

const user = ref(null)
// const store = useStore()

// onMounted(async () => {
//   const response = await $fetch('/api/v1/jwt/users/me', {
//     headers: { Authorization: `Bearer ${store.state.token}` }
//   })
//   user.value = response
// })
</script>
  