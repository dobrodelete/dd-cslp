<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-xl font-bold text-gray-900 mb-4">Пользователи CTF</h1>
        <div class="mb-4 flex gap-2">
          <DropdownFilter :options="options" placeholder="Сортировать по" @change="handleDropdownChange" />
          <template>
            <UInput
              icon="i-heroicons-magnifying-glass-20-solid"
              size="sm"
              color="white"
              trailing
              placeholder="Поиск"
            />
          </template>

          <input v-model="searchQuery" type="text" placeholder="Поиск пользователей" class="p-2 border rounded">
          <button @click="fetchUsers" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700">Поиск</button>
        </div>
        <div class="bg-white shadow rounded-lg p-4">
          <DynamicTable :items="tableItems" :headers="tableHeaders" />
          <!-- <ul>
            <li v-for="user in users" :key="user.id" class="py-2 border-b">
              <nuxt-link :to="`/ctf/users/${user.id}`" class="text-blue-500 hover:text-blue-700">{{ user.nickname }}</nuxt-link>
              - {{ user.score }} points - {{ user.team }}
            </li>
          </ul> -->
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

<script setup>
import { ref } from 'vue';
import DynamicTable from '~/components/ddctf/DynamicTable.vue';
import DropdownFilter from '~/components/ddctf/DropdownFilter.vue';

const layout = "ddctf"
const users = ref([]);
const searchQuery = ref('');
const currentPage = ref(1);
const totalPages = ref(0);

const options = [{ text: 'Баллам', value: '1' }, { text: 'Имени', value: '2' }];
const tableHeaders = ['name', 'team', 'score'];
const tableItems = [
  { id: 1, name: 'John Doe', team: "Red", score: 100 },
  { id: 2, name: 'Jane Doe', team: "Blue", score: 200 }
];

const handleDropdownChange = (value) => {
  console.log('Selected:', value);
};

const handleSearch = (query) => {
  console.log('Search for:', query);
};


// Функции для загрузки данных, пока просто заглушки
const fetchUsers = () => {
  console.log('Fetching users with search query:', searchQuery.value);
  // Тут будет реализация API запроса
  users.value = [{ id: 1, nickname: 'CTFMaster', score: 250, team: 'Alpha' }];
  totalPages.value = 3; // Пример количества страниц
};

const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    fetchUsers();
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
    fetchUsers();
  }
};

onMounted(fetchUsers);
</script>
