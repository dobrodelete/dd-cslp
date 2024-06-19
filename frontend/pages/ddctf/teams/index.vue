<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-xl font-bold text-gray-900 mb-4">Команды CTF</h1>
        <div class="mb-4 flex gap-2">
          <input v-model="searchQuery" type="text" placeholder="Поиск команд" class="p-2 border rounded">
          <button @click="fetchTeams" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700">Поиск</button>
        </div>
        <div class="bg-white shadow rounded-lg p-4">
          <ul>
            <li v-for="team in teams" :key="team.id" class="py-2 border-b">
              <nuxt-link :to="`/ctf/teams/${team.id}`" class="text-blue-500 hover:text-blue-700">{{ team.name }}</nuxt-link>
              - {{ team.score }} points
            </li>
          </ul>
          <!-- Пагинация -->
          <div class="py-4">
            <button @click="previousPage" class="bg-gray-300 text-gray-700 px-3 py-1 rounded mr-2" :disabled="currentPage <= 1">Назад</button>
            <button @click="nextPage" class="bg-gray-300 text-gray-700 px-3 py-1 rounded" :disabled="currentPage >= totalPages">Вперед</button>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import CTFNavbar from '~/components/ddctf/CTFNavbar.vue';

const layout = "ddctf"
const teams = ref([]);
const searchQuery = ref('');
const currentPage = ref(1);
const totalPages = ref(0);

const fetchTeams = () => {
  console.log('Fetching teams with search query:', searchQuery.value);
  teams.value = [{ id: 1, name: 'Team Alpha', score: 300 }];
  totalPages.value = 2; // Пример количества страниц
};

const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    fetchTeams();
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
    fetchTeams();
  }
};

onMounted(fetchTeams);
</script>
