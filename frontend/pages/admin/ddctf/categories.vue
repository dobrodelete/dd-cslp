<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl font-bold mb-4">Категории заданий</h1>
        <div class="mb-4">
          <button @click="openAddCategoryModal" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4">
            Добавить категорию
          </button>
          <CategoryModal :initialData="selectedCategory" :visible="isModalVisible" :isNew="isNew" @update:visible="isModalVisible = $event" @refreshCategories="fetchCategories" />
        </div>
        <div v-if="categories.length > 0" class="overflow-x-auto">
          <table class="min-w-full bg-white">
            <thead>
              <tr class="w-full bg-gray-200 text-left">
                <th class="px-4 py-2">Категория</th>
                <th class="px-4 py-2">Описание</th>
                <th class="px-4 py-2">Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="category in categories" :key="category.id" class="hover:bg-gray-100">
                <td class="border px-4 py-2">{{ category.name }}</td>
                <td class="border px-4 py-2">{{ category.description }}</td>
                <td class="border px-4 py-2">
                  <button @click="openEditCategoryModal(category)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
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
        <div v-else-if="categories.length === 0" class="text-center py-4">
          Нет доступных категорий.
        </div>
        <div v-if="totalCategories > pageSize" class="pagination">
          <button @click="changePage(currentPage - 1)" :disabled="currentPage.value <= 1">Назад</button>
          <span>Страница {{ currentPage }} из {{ totalPages }}</span>
          <button @click="changePage(currentPage + 1)" :disabled="currentPage.value >= totalPages.value">Вперед</button>
        </div>
        <!-- <div v-else-if="categories.length === 0" class="text-center py-4">
          Нет доступных категорий.
        </div> -->
      </div>
    </div>
  </NuxtLayout>
</template>


<script>
import { ref, onMounted, computed, nextTick } from 'vue';
import CategoryModal from '@/components/admin/CategoryModal.vue';
import { useApi } from '~/composables/useApi';

export default {
  components: {
    CategoryModal
  },
  setup() {
    const layout = ref("admin-ctf");
    const categories = ref([]);
    const isModalVisible = ref(false);
    const selectedCategory = ref({});
    const isNew = ref(true);
    const api = useApi('ddctf/categories');
    let currentPage = ref(1);
    let pageSize = ref(10);
    let totalCategories = ref(0);
    let totalPages = computed(() => Math.ceil(totalCategories.value / pageSize.value));

    const fetchCategories = async (page = currentPage.value) => {
      const skip = (page - 1) * pageSize.value;
      const limit = pageSize.value;
      try {
        const response = await api.list({ skip, limit });
        categories.value = response.categories;
        totalCategories.value = response.total;
        await nextTick();
        totalPages.value = Math.ceil(totalCategories.value / pageSize.value); // Убедитесь, что это вычисление выполняется правильно
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    };

    const openAddCategoryModal = () => {
      selectedCategory.value = { name: '', description: '' };
      isNew.value = true;
      isModalVisible.value = true;
    };

    const openEditCategoryModal = (category) => {
      selectedCategory.value = { ...category };
      isNew.value = false;
      isModalVisible.value = true;
    };

    const deleteCategory = async (id) => {
      await api.remove(id);
      await fetchCategories(currentPage.value);
    };

    const changePage = (page) => {
      if (page < 1 || page > totalPages.value) return;
      currentPage.value = page;
      fetchCategories(page);
    };

    onMounted(() => {
      fetchCategories(1);
    });

    return { 
      layout,
      categories,
      isModalVisible,
      selectedCategory,
      isNew,
      fetchCategories,
      openAddCategoryModal,
      openEditCategoryModal,
      deleteCategory,
      currentPage,
      totalPages,
      changePage,
      pageSize,
      totalCategories
     };
  }
};
</script>

<style scoped>
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
.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
}
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
