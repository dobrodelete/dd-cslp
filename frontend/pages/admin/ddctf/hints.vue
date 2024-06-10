<template>
  <NuxtLayout :name="layout">
    <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-6">Управление подсказками для задач</h1>
    <button @click="newHint" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4">
      Добавить подсказку
    </button>
    <div class="overflow-x-auto">
      <table class="min-w-full bg-white">
        <thead class="bg-gray-200">
          <tr>
            <th class="px-4 py-2">Задача</th>
            <th class="px-4 py-2">Подсказка</th>
            <th class="px-4 py-2">Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="hint in hints" :key="hint.id" class="hover:bg-gray-100">
            <td class="border px-4 py-2">{{ hint.taskTitle }}</td>
            <td class="border px-4 py-2">{{ hint.content }}</td>
            <td class="border px-4 py-2">
              <button @click="editHint(hint)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded">
                Редактировать
              </button>
              <button @click="deleteHint(hint.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded">
                Удалить
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const hints = ref([
  { id: 1, taskTitle: 'SQL Injection Basics', content: 'Check for input validation.' },
  { id: 2, taskTitle: 'Cross-site Scripting', content: 'Look for unsanitized user input.' }
]);

const newHint = () => {
  // Logic to add a new hint
  console.log('Adding a new hint');
};

const editHint = (hint) => {
  // Logic to edit an existing hint
  console.log('Editing hint:', hint);
};

const deleteHint = (id) => {
  // Logic to delete a hint
  console.log('Deleting hint with ID:', id);
  hints.value = hints.value.filter(h => h.id !== id);
};

const layout = "admin-ctf"
</script>

<style>
.container {
  max-width: 1200px;
}
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
</style>