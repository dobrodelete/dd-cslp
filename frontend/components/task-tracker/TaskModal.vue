<template>
  <div v-if="show" class="modal">
    <div class="modal-content">
      <span @click="closeModal" class="close">&times;</span>
      <h2>{{ task.title }}</h2>
      <p>Детали задачи...</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const show = ref(false);
const task = ref({ title: 'Задача 1' });

const closeModal = () => {
  show.value = false;
};
</script>

<style scoped>
  .modal { /* Стили для модального окна */ }
  .modal-content { /* Стили для содержимого модального окна */ }
  .close { /* Стили для кнопки закрытия */ }
</style>
