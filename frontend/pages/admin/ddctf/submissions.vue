<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl font-bold mb-6">Управление ответами на задачи CTF</h1>
        <button @click="newAnswer" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4">
          Добавить ответ
        </button>
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white">
            <thead class="bg-gray-200">
              <tr>
                <th class="px-4 py-2">Задача</th>
                <th class="px-4 py-2">Ответ</th>
                <th class="px-4 py-2">Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="answer in answers" :key="answer.id" class="hover:bg-gray-100">
                <td class="border px-4 py-2">{{ answer.taskTitle }}</td>
                <td class="border px-4 py-2">{{ answer.content }}</td>
                <td class="border px-4 py-2">
                  <button @click="editAnswer(answer)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded">
                    Редактировать
                  </button>
                  <button @click="deleteAnswer(answer.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded">
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

const answers = ref([
  { id: 1, taskTitle: 'SQL Injection Basics', content: 'admin' },
  { id: 2, taskTitle: 'Cross-site Scripting', content: "xss" }
]);

const newAnswer = () => {
  // Logic to add a new answer
  console.log('Adding a new answer');
};

const editAnswer = (answer) => {
  // Logic to edit an existing answer
  console.log('Editing answer:', answer);
};

const deleteAnswer = (id) => {
  // Logic to delete an answer
  console.log('Deleting answer with ID:', id);
  answers.value = answers.value.filter(a => a.id !== id);
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
