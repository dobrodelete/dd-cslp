<template>
  <NuxtLayout name="admin-task-tracker">
    <div class="container mx-auto p-6">
      <h1 class="text-3xl font-bold mb-6">Task Tracker</h1>
      <div class="mb-6">
        <button @click="newTask" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
          Добавить задачу
        </button>
      </div>
      <div class="overflow-x-auto">
        <table class="min-w-full bg-white">
          <thead class="bg-gray-200">
            <tr>
              <th class="px-4 py-2">Задача</th>
              <th class="px-4 py-2">Описание</th>
              <th class="px-4 py-2">Статус</th>
              <th class="px-4 py-2">Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="task in tasks" :key="task.id" class="hover:bg-gray-100">
              <td class="border px-4 py-2">{{ task.name }}</td>
              <td class="border px-4 py-2">{{ task.description }}</td>
              <td class="border px-4 py-2">{{ task.status }}</td>
              <td class="border px-4 py-2">
                <button @click="editTask(task.id)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                  Редактировать
                </button>
                <button @click="deleteTask(task.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
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

<script setup>
import { ref } from 'vue';

const tasks = ref([
  { id: 1, name: 'Frontend Bug Fix', description: 'Исправить ошибку в слайдере на главной странице.', status: 'Открыта' },
  { id: 2, name: 'Add New Feature', description: 'Добавить новую функциональность в профиль пользователя.', status: 'В работе' }
]);

const newTask = () => {
  console.log('Redirect to new task creation form');
  // Redirect to task creation form
};

const editTask = (id) => {
  console.log('Redirect to edit task form for task with ID:', id);
  // Redirect to task editing form
};

const deleteTask = (id) => {
  console.log('Deleting task with ID:', id);
  // Logic to delete a task
};
</script>

<style scoped>
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
