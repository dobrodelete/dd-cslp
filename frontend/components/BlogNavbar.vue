<template>
  <div class="bg-gray-800 text-white p-3 rounded-lg">
    <ul class="flex space-x-4">
      <li><nuxt-link to="/blog/" class="hover:text-blue-300">Главная</nuxt-link></li>
      <li><nuxt-link to="/blog/my/" class="hover:text-blue-300">Мои подписки</nuxt-link></li>
      <li><nuxt-link to="/blog/new_post/" class="hover:text-blue-300">Добавить пост</nuxt-link></li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
</script>

<style>
</style>