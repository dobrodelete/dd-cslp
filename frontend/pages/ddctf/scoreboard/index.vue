<template>
  <NuxtLayout name="ddctf">
    <div class="p-5">
      <h1 class="text-3xl font-bold text-center mb-6">Рейтинг CTF</h1>
      <div class="max-w-6xl mx-auto">
        <h2 class="text-2xl font-semibold mb-4">Топ команд</h2>
        <ul class="mb-8">
          <li v-for="(team, index) in teams" :key="team.id" class="flex items-center justify-between mb-2">
            <span>{{ index + 1 }}. {{ team.name }}</span>
            <span class="font-bold">{{ team.points }} pts</span>
            <svg width="200" height="10">
              <rect width="200" height="10" fill="#ddd"></rect>
              <rect :width="team.points / maxTeamPoints * 200" height="10" fill="#4caf50"></rect>
            </svg>
          </li>
        </ul>
        <h2 class="text-2xl font-semibold mb-4">Рейтинг игроков</h2>
        <ul>
          <li v-for="(player, index) in players" :key="player.id" class="flex items-center justify-between mb-2">
            <span>{{ index + 1 }}. {{ player.name }}</span>
            <span class="font-bold">{{ player.points }} pts</span>
            <svg width="200" height="10">
              <rect width="200" height="10" fill="#ddd"></rect>
              <rect :width="player.points / maxPlayerPoints * 200" height="10" fill="#2196f3"></rect>
            </svg>
          </li>
        </ul>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed } from 'vue';

const teams = ref([
  { id: 1, name: 'Team Alpha', points: 150 },
  { id: 2, name: 'Team Beta', points: 120 },
  { id: 3, name: 'Team Gamma', points: 100 }
]);

const players = ref([
  { id: 1, name: 'Alice', points: 88 },
  { id: 2, name: 'Bob', points: 75 },
  { id: 3, name: 'Charlie', points: 60 }
]);

const maxTeamPoints = computed(() => Math.max(...teams.value.map(team => team.points)));
const maxPlayerPoints = computed(() => Math.max(...players.value.map(player => player.points)));
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
svg {
  margin-left: auto;
}
</style>
