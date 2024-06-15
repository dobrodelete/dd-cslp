<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl font-bold mb-4">Список команд</h1>
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white">
            <thead>
              <tr class="w-full bg-gray-200 text-left">
                <th class="px-4 py-2">Название команды</th>
                <th class="px-4 py-2">Количество участников</th>
                <th class="px-4 py-2">Очки</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="team in teams" :key="team.id" class="hover:bg-gray-100">
                <td class="border px-4 py-2">{{ team.name }}</td>
                <td class="border px-4 py-2">{{ team.membersCount }}</td>
                <td class="border px-4 py-2">{{ team.points }}</td>
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

const teams = ref([
  { id: 1, name: 'Alpha', membersCount: 5, points: 350 },
  { id: 2, name: 'Beta', membersCount: 4, points: 290 },
  { id: 3, name: 'Gamma', membersCount: 6, points: 410 }
]);
const layout = "admin-ctf"
</script>

<style>
table {
  border-collapse: collapse;
  width: 100%;
}
th, td {
  border: solid 1px #ddd;
  padding: 8px;
}
thead {
  background-color: #f9fafb;
}
tr:hover {
  background-color: #f1f1f1;
}
</style>