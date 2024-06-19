<template>
  <div class="bg-gray-800 text-white p-3 ">
    <ul class="flex space-x-4 justify-center">
      <li><nuxt-link to="/" class="hover:text-gray-300">CSLP</nuxt-link></li>
      <li><nuxt-link to="/admin/" class="hover:text-gray-300">Админ панель</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/" class="hover:text-gray-300">Дашборд</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/ctf-events" class="hover:text-gray-300">События</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/categories" class="hover:text-gray-300">Категории</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/challenges" class="hover:text-gray-300">Задачи</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/hints" class="hover:text-gray-300">Подсказки</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/submissions" class="hover:text-gray-300">Ответы</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/teams" class="hover:text-gray-300">Команды</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/users" class="hover:text-gray-300">Пользователи</nuxt-link></li>
      <li><nuxt-link to="/admin/ddctf/settings" class="hover:text-gray-300">Настройки</nuxt-link></li>
    </ul>
  </div>
</template>
