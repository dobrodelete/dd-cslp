<template>
  <aside class="bg-gray-200 w-64 h-full">
    <ul class="space-y-2 p-4">
      <li v-for="board in boards" :key="board.id" @click="selectBoard(board)" class="cursor-pointer p-2 hover:bg-gray-300 rounded">
        {{ board.name }}
      </li>
    </ul>
  </aside>
</template>

<script setup>
import { ref } from 'vue';

const boards = ref([
  { id: 1, name: 'Доска 1' },
  { id: 2, name: 'Доска 2' },
  { id: 3, name: 'Доска 3' }
]);

const selectBoard = (board) => {
  console.log('Board selected:', board);
  // Handle board selection logic
};
</script>
