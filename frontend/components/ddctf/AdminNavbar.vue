<template>
  <div class="bg-gray-800 text-white p-3">
    <ul class="flex space-x-4">
      <li><nuxt-link to="/ddctf/" class="hover:text-gray-300">ddCTF</nuxt-link></li>
      <li><nuxt-link to="/ddctf/admin/users" class="hover:text-gray-300">Пользователи</nuxt-link></li>
      <li><nuxt-link to="/ddctf/admin/teams" class="hover:text-gray-300">Команды</nuxt-link></li>
      <li><nuxt-link to="/ddctf/admin/challenges" class="hover:text-gray-300">Задания</nuxt-link></li>
      <li><nuxt-link to="/ddctf/admin/categories" class="hover:text-gray-300">Категории</nuxt-link></li>
      <li><nuxt-link to="/ddctf/admin/hints" class="hover:text-gray-300">Подсказки</nuxt-link></li>
      <li><nuxt-link to="/ddctf/admin/submissions" class="hover:text-gray-300">Ответы</nuxt-link></li>
    </ul>
  </div>
</template>
