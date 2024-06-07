<template>
  <NuxtLayout name="ddctf">
    <div class="p-5">
      <h1 class="text-3xl font-bold text-center mb-6">Детали команды</h1>
      <div class="max-w-4xl mx-auto bg-white shadow-lg rounded-lg p-8">
        <div class="mb-6">
          <h2 class="text-2xl font-semibold">{{ team.name }}</h2>
          <p class="text-gray-600">Очки: {{ team.points }}</p>
        </div>
        <div class="mb-6">
          <h3 class="text-xl font-semibold">Члены команды</h3>
          <ul>
            <li v-for="member in team.members" :key="member.id" class="mb-2">
              {{ member.name }} - {{ member.role }}
            </li>
          </ul>
        </div>
        <div class="mb-6">
          <h3 class="text-xl font-semibold">Достижения команды</h3>
          <ul>
            <li v-for="achievement in team.achievements" :key="achievement.id" class="mb-2">
              {{ achievement.title }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const team = ref({
  name: 'Team Alpha',
  points: 300,
  members: [
    { id: 1, name: 'Alice', role: 'Leader' },
    { id: 2, name: 'Bob', role: 'Analyst' },
    { id: 3, name: 'Charlie', role: 'Developer' }
  ],
  achievements: [
    { id: 1, title: 'Winner of Regional CTF 2023' },
    { id: 2, title: 'Second Place in National Cyber Games 2022' }
  ]
});
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: flex;
  align-items: center;
}
</style>
