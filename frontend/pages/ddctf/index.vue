<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 py-6">
        <h1 class="text-xl font-bold text-gray-900 mb-6">Capture The Flag (CTF)</h1>
        <div class="grid grid-cols-3 gap-4">
          <div class="bg-white p-4 shadow rounded-lg">
            <h2 class="text-lg font-semibold text-gray-800">Задачи</h2>
            <ul class="text-gray-900">
              <li v-for="challenge in challenges" :key="challenge.id">
                <nuxt-link :to="`/ddctf/challenges/${challenge.id}`" class="text-blue-500 hover:text-blue-700">
                  {{ challenge.name }}
                </nuxt-link>
              </li>
            </ul>
          </div>
          <div class="col-span-2 bg-white p-4 shadow rounded-lg">
            <h2 class="text-lg font-semibold text-gray-800">Таблица результатов</h2>
            <table class="w-full text-sm text-gray-900">
              <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                <tr>
                  <th scope="col" class="px-6 py-3">Команда</th>
                  <th scope="col" class="px-6 py-3">Очки</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="team in teams" :key="team.id" class="bg-white border-b">
                  <td class="px-6 py-4">{{ team.name }}</td>
                  <td class="px-6 py-4">{{ team.score }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>


<script setup>
import { ref } from 'vue';

const layout = "ddctf";

const challenges = ref([
  { id: 1, name: 'SQL Injection Basics' },
  { id: 2, name: 'Cross-site Scripting (XSS)' }
]);

const teams = ref([
  { id: 1, name: 'Alpha Team', score: 150 },
  { id: 2, name: 'Beta Squad', score: 120 }
]);

</script>

<style>
/* Дополнительные стили, если нужны */
</style>
  