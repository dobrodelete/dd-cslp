<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
      <form @submit.prevent="handleRegister" class="p-8 bg-white shadow-lg rounded-lg">
        <h2 class="text-2xl font-semibold mb-4 text-black">Регистрация</h2>
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium text-gray-700">Имя пользователя</label>
          <input id="username" v-model="username" type="text" required class="mt-1 p-2 w-full border rounded-md bg-stone-50 text-black">
        </div>
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input id="email" v-model="email" type="email" required class="mt-1 p-2 w-full border rounded-md bg-stone-50 text-black">
        </div>
        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <input id="password" v-model="password" type="password" required class="mt-1 p-2 w-full border rounded-md bg-stone-50 text-black">
        </div>
        <button type="submit" class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Зарегистрироваться
        </button>
      </form>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const layout = "default"
const username = ref('');
const email = ref('');
const full_name = ref('');
const phone_number = ref('');
const password = ref('');
const router = useRouter();

const handleRegister = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/v1/jwt/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        full_name: full_name.value,
        password: password.value
      })
    });

    if (!response.ok) {
      throw new Error('Ошибка при регистрации');
    }

    const data = await response.json();
    router.push({ path: '/auth/login', query: { flash: 'Регистрация прошла успешно! Пожалуйста, войдите в систему.' } });
  } catch (error) {
    console.error('Registration error:', error);
  }
};
</script>

<style scoped>
</style>
