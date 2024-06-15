<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl font-bold mb-4">Категории заданий</h1>
        <div>
          <button @click="showModal" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4">
            Добавить категорию
          </button>
          <CategoryModal :initialData="{ name: '', description: '' }" :visible="isModalVisible" :isNew="true" @update:visible="isModalVisible = $event" @save-category="handleSave" />
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
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { useApi } from '@/composables/useApi';
import type { CategoryCreate, CategoryRead } from '@/types/category';
import CategoryModal from '@/components/admin/CategoryModal.vue';

const layout = ref("admin-ctf");
const categories = ref<CategoryRead[]>([]);

const { create, get, list, update, remove } = useApi<CategoryRead>('categories');

const fetchCategories = async () => {
  categories.value = await list();
};

const addCategory = async () => {
  const newCategory: CategoryCreate = {
    name: "Новая категория",
    description: "Пример описания категории"
  };
  const createdCategory = await create(newCategory);
  console.log("Category Created:", createdCategory);
  await fetchCategories();
};

const editCategory = async (id: number) => {
  const updatedCategory = await update(id, { name: "Обновленная категория", description: "Обновленное описание" });
  console.log("Category Updated:", updatedCategory);
  await fetchCategories();
};

const deleteCategory = async (id: number) => {
  await remove(id);
  console.log("Category Deleted:", id);
  await fetchCategories();
};

const isModalVisible = ref(false);

const showModal = () => {
  isModalVisible.value = true;
};

const handleSave = (categoryData) => {
  console.log('Saving category:', categoryData);
  // Здесь добавьте логику для сохранения данных категории через API
};

onMounted(fetchCategories);
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