<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl font-bold mb-4">Управление заданиями</h1>
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white">
            <thead>
              <tr class="w-full bg-gray-200 text-left">
                <th class="px-4 py-2">Название задания</th>
                <th class="px-4 py-2">Категория</th>
                <th class="px-4 py-2">Очки</th>
                <th class="px-4 py-2">Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="challenge in challenges" :key="challenge.id" class="hover:bg-gray-100">
                <td class="border px-4 py-2">{{ challenge.name }}</td>
                <td class="border px-4 py-2">{{ challenge.category }}</td>
                <td class="border px-4 py-2">{{ challenge.points }}</td>
                <td class="border px-4 py-2">
                  <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Редактировать
                  </button>
                  <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2">
                    Удалить
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const challenges = ref([
  { id: 1, name: 'SQL Injection Basics', category: 'Web Security', points: 100 },
  { id: 2, name: 'Cross-site Scripting (XSS)', category: 'Web Security', points: 150 },
  { id: 3, name: 'Binary Exploitation 101', category: 'Binary Exploitation', points: 200 }
]);
const layout = "admin-ctf"
</script>

<style>

</style>