<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">CTF Dashboard</h1>
        <div class="grid grid-cols-3 gap-4">
          <!-- Обзорные панели -->
          <div class="bg-white p-4 shadow rounded-lg">
            <h2 class="text-lg font-semibold text-gray-800">Статистика</h2>
            <p class="text-black">Общее количество задач: {{ totalChallenges }}</p>
            <p class="text-black">Активные пользователи: {{ activeUsers }}</p>
            <p class="text-black">Количество команд: {{ totalTeams }}</p>
          </div>
          <!-- Недавние активности -->
          <div class="col-span-2 bg-white p-4 shadow rounded-lg">
            <h2 class="text-lg font-semibold text-gray-800">Недавние активности</h2>
            <ul>
              <li v-for="activity in recentActivities" :key="activity.id" class="py-2 border-b text-black">
                {{ activity.description }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';
const layout = "ddctf"
const totalChallenges = ref(10);
const activeUsers = ref(40);
const totalTeams = ref(5);
const recentActivities = ref([
  { id: 1, description: 'User X solved challenge Y' },
  { id: 2, description: 'Team Z scored 200 points on challenge A' }
]);
</script>
  