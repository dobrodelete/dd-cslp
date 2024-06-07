<template>
  <div class="bg-white shadow-md pl-11">
    <div class="max-w-7xl mx-auto px-4 py-2 flex justify-between items-center">
      <div>
        <nuxt-link to="/" class="font-bold text-xl text-blue-600 pl-3.5 pr-3.5">Главная</nuxt-link>
        <nuxt-link to="/ddctf" class="font-bold text-xl text-blue-600 pl-3.5 pr-3.5">ddCTF</nuxt-link>
        <nuxt-link to="/blog" class="font-bold text-xl text-blue-600 pl-3.5 pr-3.5">ddBlog</nuxt-link>
        <nuxt-link to="/task-tracker" class="font-bold text-xl text-blue-600 pl-3.5 pr-3.5">ddTaskTracker</nuxt-link>
        <nuxt-link to="/docs" class="font-bold text-xl text-blue-600 pl-3.5 pr-3.5">Docs</nuxt-link>
      </div>
      <div>
        <button v-if="!isAuthenticated" @click="goToLogin" class="mr-2 text-blue-600">Вход</button>
        <button v-if="!isAuthenticated" @click="goToRegister" class="mr-2 text-blue-600">Регистрация</button>
        <button v-if="isAuthenticated" @click="logout" class="">Выход</button>
        <!-- <button v-if="!isAuthenticated" @click="login" class="text-blue-500 hover:text-blue-700">Вход</button> -->
        <!-- <button v-else @click="logout" class="text-red-500 hover:text-red-700">Выход</button> -->
      </div>
    </div>
  </div>
  <div>
    <!-- <UHorizontalNavigation :links="links" class="border-b border-gray-200 dark:border-gray-800 max-w-7xl mx-auto px-4 py-2" /> -->
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const isAuthenticated = ref(false);
const router = useRouter();
const route = useRoute()


const goToLogin = () => {
  router.push({ path: '/auth/login', query: { redirect: router.currentRoute.fullPath } });
};

const goToRegister = () => {
  router.push('/auth/register');
};

const logout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  isAuthenticated.value = false;
  router.push('/');
};

const links = [{
  label: 'Главная',
  icon: 'i-heroicons-home',
  to: '/'
}, {
  label: 'ddCTF',
  icon: 'i-heroicons-chart-bar',
  to: "/ddctf"
}, {
  label: 'Blog',
  icon: 'i-heroicons-command-line',
  to: '/blog'
},  {
  label: 'Task Tracker',
  icon: 'i-heroicons-command-line',
  to: '/task-tracker'
}]
</script>

<style scoped>
</style>
  