<template>
  <NuxtLayout name="ddctf">
    <div class="p-5">
      <h1 class="text-3xl font-bold text-center mb-6">Профиль пользователя</h1>
      <div class="max-w-4xl mx-auto bg-white shadow-lg rounded-lg p-8">
        <div class="flex items-center space-x-6 mb-6">
          <img :src="user.avatar" alt="Avatar" class="h-24 w-24 rounded-full object-cover">
          <div>
            <h2 class="text-2xl font-semibold">{{ user.name }}</h2>
            <p class="text-gray-600">{{ user.email }}</p>
          </div>
        </div>
        <div>
          <h3 class="text-xl font-semibold mb-4">О пользователе</h3>
          <p>{{ user.bio }}</p>
        </div>
        <div class="mt-6">
          <button @click="editProfile" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Редактировать профиль
          </button>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';

const user = ref({
  name: 'John Doe',
  email: 'john.doe@example.com',
  avatar: 'https://via.placeholder.com/150',
  bio: 'Любитель CTF и кибербезопасности. Стремлюсь к постоянному обучению и развитию в этой области.'
});

const editProfile = () => {
  // Логика для перехода к форме редактирования профиля или открытия модального окна редактирования
  console.log('Редактирование профиля');
};
</script>

<style scoped>
img {
  display: block;
}
</style>
