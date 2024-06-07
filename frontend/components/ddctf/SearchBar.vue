<template>
  <div class="flex space-x-2">
    <input v-model="searchQuery" :placeholder="placeholder" class="p-2 border rounded flex-grow">
    <button @click="onSearch" class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded">Поиск</button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps({
  placeholder: String
});

const searchQuery = ref('');

const emit = defineEmits(['search']);

const onSearch = () => {
  emit('search', searchQuery.value);
};
</script>
