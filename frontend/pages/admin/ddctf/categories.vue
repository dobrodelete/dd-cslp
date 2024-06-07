<template>
  <NuxtLayout :name="layout">
    <div>
      <h1 class="text-3xl font-bold mb-4">Категории заданий</h1>
      <div class="mb-4">
        <button @click="addCategory" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
          Добавить категорию
        </button>
      </div>
      <div class="overflow-x-auto">
        <table class="min-w-full bg-white">
          <thead>
            <tr class="w-full bg-gray-200 text-left">
              <th class="px-4 py-2">Категория</th>
              <th class="px-4 py-2">Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="category in categories" :key="category.id" class="hover:bg-gray-100">
              <td class="border px-4 py-2">{{ category.name }}</td>
              <td class="border px-4 py-2">
                <button @click="editCategory(category.id)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                  Редактировать
                </button>
                <button @click="deleteCategory(category.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2">
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

const categories = ref([
  { id: 1, name: 'Web Security' },
  { id: 2, name: 'Binary Exploitation' },
  { id: 3, name: 'Cryptography' }
]);

const addCategory = () => {
  console.log('Adding a new category');
  // Here you would add logic to create a new category
};

const editCategory = (id) => {
  console.log('Editing category with ID:', id);
  // Here you would add logic to edit an existing category
};

const deleteCategory = (id) => {
  console.log('Deleting category with ID:', id);
  // Here you would add logic to delete a category
};
const layout = "ddctf-admin"
</script>

<style>
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
tr:hover {
  background-color: #f1f1f1;
}
</style>