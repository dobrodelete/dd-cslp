<template>
  <div class="bg-gray-800 text-white p-3 ">
    <ul class="flex space-x-4 justify-center">
      <li><nuxt-link to="/" class="hover:text-blue-300">CSLP</nuxt-link></li>
      <li><nuxt-link to="/blog/" class="hover:text-blue-300">Главная</nuxt-link></li>
      <li><nuxt-link to="/blog/recomendation/" class="hover:text-blue-300">Рекомендации</nuxt-link></li>
      <li><nuxt-link to="/blog/subscribe/" class="hover:text-blue-300">Подписки</nuxt-link></li>
      <li><nuxt-link to="/blog/cms/" class="hover:text-blue-300">Мои посты</nuxt-link></li>
    </ul>
  </div>
</template>

<script setup>
const logout = () => {
  console.log('Logging out...');
  // Add your logout logic here
};
</script>

<style scoped>
.header {
  width: 100%;
  background-color: #333;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  display: inline;
}
</style>
