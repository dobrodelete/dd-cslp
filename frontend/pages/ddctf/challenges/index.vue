<template>
  <NuxtLayout name="ddctf">
    <div class="p-5">
      <h1 class="text-3xl font-bold mb-6">Задания</h1>
      <div v-for="(tasks, category) in challenges" :key="category" class="mb-4">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">{{ category }}</h2>
        <div class="grid grid-cols-4 gap-4">
          <div v-for="task in tasks" :key="task.id"
               @click="openModal(task)"
               :class="[task.completed ? 'bg-green-100' : 'bg-slate-200', 'cursor-pointer rounded-lg shadow-lg p-4 relative max-w-80']">
            <h3 class="text-xl font-medium">{{ task.name }}</h3>
            <h4 class="text-xl font-medium">{{ task.points }} очков</h4>
            <!-- <p v-if="task.completed" class="absolute top-2 right-2 text-green-500 text-sm">Выполнено</p> -->
            <!-- <p v-else class="absolute top-2 right-2 text-red-500 text-sm">Не выполнено</p> -->
            <!-- <button @click="openModal(task)" class="mt-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded cursor-pointer">Подробнее</button> -->
          </div>
        </div>
      </div>
    </div>

    <!-- Модальное окно для задачи -->
    <div v-if="selectedTask" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full" @click.self="selectedTask = null">
      <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
        <h3 class="text-lg font-bold">{{ selectedTask.name }}</h3>
        <p class="mb-4">{{ selectedTask.description }}</p>
        <button class="bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded block w-full mb-2">Подсказка</button>
        <input type="text" placeholder="Введите флаг" class="p-2 border rounded w-full mb-4">
        <!-- <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded block w-full" @click="selectedTask = null">Закрыть</button> -->
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';

const challenges = ref({
  'Osint': [
    { id: 1, name: 'task1', points: 300, description: 'Описание задания 1 в категории Osint.', completed: true },
    { id: 2, name: 'task2', points: 500, description: 'Описание задания 2 в категории Osint.', completed: false },
    { id: 3, name: 'task2', points: 500, description: 'Описание задания 2 в категории Osint.', completed: false },
    { id: 4, name: 'task2', points: 500, description: 'Описание задания 2 в категории Osint.', completed: false },
    { id: 5, name: 'task2', points: 500, description: 'Описание задания 2 в категории Osint.', completed: false },
    { id: 6, name: 'task2', points: 500, description: 'Описание задания 2 в категории Osint.', completed: false },
    { id: 7, name: 'task2', points: 500, description: 'Описание задания 2 в категории Osint.', completed: false },
    { id: 8, name: 'task2', points: 500, description: 'Описание задания 2 в категории Osint.', completed: false },
  ],
  'Crypto': [
    { id: 3, name: 'task1', points: 250, description: 'Описание задания 1 в категории Crypto.', completed: false },
    { id: 4, name: 'task2', points: 450, description: 'Описание задания 2 в категории Crypto.', completed: true }
  ],
  'Reverse': [
    { id: 3, name: 'task1', points: 250, description: 'Описание задания 1 в категории Crypto.', completed: false },
    { id: 4, name: 'task2', points: 450, description: 'Описание задания 2 в категории Crypto.', completed: true }
  ]
});

const selectedTask = ref(null);

const openModal = (task) => {
  selectedTask.value = task;
};
</script>

<style>
/* Добавляем некоторые стили для улучшения внешнего вида */
</style>
