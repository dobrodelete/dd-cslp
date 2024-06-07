<template>
  <NuxtLayout :name="layout">
    <FlashMessage :message="flashMessage" :type="flashType" />
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
      <form @submit.prevent="handleLogin" class="p-8 bg-white shadow-lg rounded-lg">
        <h2 class="text-2xl font-semibold mb-4 text-black">Авторизация</h2>
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
          <input id="username" v-model="username" type="username" required class="mt-1 p-2 w-full border rounded-md bg-stone-50 text-black">
        </div>
        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <input id="password" v-model="password" type="password" required class="mt-1 p-2 w-full border rounded-md bg-stone-50 text-black">
        </div>
        <button type="submit" class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Войти
        </button>
      </form>
    </div>
  </NuxtLayout>
</template>

<script setup>
import FlashMessage from '@/components/FlashMessage.vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const layout = "default";
const username = ref('');
const password = ref('');
const router = useRouter();
const route = useRoute();
const flashMessage = ref('');
const flashType = ref('info');
const redirect = ref(route.query.redirect || '/');

const handleLogin = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/v1/jwt/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    });

    if (!response.ok) {
      throw new Error('Ошибка при авторизации');
    }

    const data = await response.json();
    flashMessage.value = 'Успешная авторизация!';
    flashType.value = 'success';

    localStorage.setItem('access_token', data.access_token);
    localStorage.setItem('refresh_token', data.refresh_token);

    router.push(redirect.value);
    router.push({ name: 'home', query: { flash: 'Успешная авторизация!' } });
  } catch (error) {
    flashMessage.value = 'Ошибка при авторизации. Попробуйте снова.';
    flashType.value = 'error';
  }
};
</script>

<style scoped>
/* Стилизация формы здесь */
</style>
