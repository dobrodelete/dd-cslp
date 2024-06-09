<template>
  <div class="group p-4 bg-white rounded shadow">
    <h3 class="font-bold text-lg">{{ group.name }}</h3>
    <ul>
      <li v-for="task in group.tasks" :key="task.id" @click="openTaskModal(task)">
        {{ task.title }}
      </li>
    </ul>
    <button @click="newTask" class="mt-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded">
      Добавить задачу
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import TaskModal from './TaskModal.vue';

const group = ref({
  name: 'Пример группы',
  tasks: [
    { id: 1, title: 'Задача 1' },
    { id: 2, title: 'Задача 2' }
  ]
});

const openTaskModal = (task) => {
  // Логика открытия модального окна
};

const newTask = () => {
  // Логика добавления новой задачи
};
</script>
