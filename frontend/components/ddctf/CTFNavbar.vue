<template>
  <div class="bg-gray-800 text-white p-3 ">
    <ul class="flex space-x-4 justify-center">
      <li><nuxt-link to="/" class="hover:text-blue-300">CSLP</nuxt-link></li>
      <li><nuxt-link to="/ddctf/dashboard/" class="hover:text-blue-300">Dashboard</nuxt-link></li>
      <li><nuxt-link to="/ddctf/users/" class="hover:text-blue-300">Пользователи</nuxt-link></li>
      <li><nuxt-link to="/ddctf/teams/" class="hover:text-blue-300">Команды</nuxt-link></li>
      <li><nuxt-link to="/ddctf/scoreboard/" class="hover:text-blue-300">Рейтинг</nuxt-link></li>
      <li><nuxt-link to="/ddctf/challenges/" class="hover:text-blue-300">Задания</nuxt-link></li>
      <li><nuxt-link to="/ddctf/notifications/" class="hover:text-blue-300">Уведомления</nuxt-link></li>
      <li><nuxt-link to="/ddctf/profile/" class="hover:text-blue-300">Профиль</nuxt-link></li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
// Импорты и скрипты не нужны для этого простого компонента навигации
</script>

<style>
/* Немного стилей, если нужно дополнительно кастомизировать */
</style>
