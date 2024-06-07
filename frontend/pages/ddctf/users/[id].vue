<template>
  <NuxtLayout name="ddctf">
    <div class="p-5">
      <h1 class="text-3xl font-bold text-center mb-6">Профиль пользователя</h1>
      <div class="max-w-4xl mx-auto bg-white shadow-lg rounded-lg p-8 flex items-start space-x-6">
        <img :src="user.avatar" alt="Avatar пользователя" class="h-40 w-40 rounded-full">
        <div class="flex-grow">
          <h2 class="text-2xl font-semibold">{{ user.name }}</h2>
          <p class="text-gray-600">{{ user.email }}</p>
          <div class="mt-4">
            <h3 class="text-lg font-semibold">О пользователе</h3>
            <p>{{ user.bio }}</p>
          </div>
          <div class="mt-4">
            <h3 class="text-lg font-semibold">Достижения</h3>
            <ul>
              <li v-for="achievement in user.achievements" :key="achievement.id" class="mb-2">
                {{ achievement.title }}
              </li>
            </ul>
          </div>
          <button class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Перейти к полному профилю
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
  bio: 'Любитель CTF и кибербезопасности. Стремлюсь к постоянному обучению и развитию в этой области.',
  achievements: [
    { id: 1, title: 'Победитель CTF Challenge 2023' },
    { id: 2, title: 'Лучший новичок 2022' }
  ]
});
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: block;
}
</style>
