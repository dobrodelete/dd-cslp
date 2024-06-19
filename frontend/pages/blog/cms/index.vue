<template>
  <NuxtLayout name="blog">
    <div class="p-5">
      <h1 class="text-3xl font-bold mb-4">CMS Dashboard</h1>
      <nuxt-link to="/blog/cms/create" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-7">
        Добавить статью
      </nuxt-link>
      <div class="overflow-x-auto mt-5">
        <table class="min-w-full bg-white">
          <thead>
            <tr class="w-full bg-gray-200 text-left">
              <th class="px-4 py-2">Название</th>
              <th class="px-4 py-2">Автор</th>
              <th class="px-4 py-2">Дата публикации</th>
              <th class="px-4 py-2">Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="article in articles" :key="article.id" class="hover:bg-gray-100">
              <td class="border px-4 py-2">{{ article.title }}</td>
              <td class="border px-4 py-2">{{ article.author }}</td>
              <td class="border px-4 py-2">{{ article.publishedAt }}</td>
              <td class="border px-4 py-2">
                <button @click="editArticle(article.id)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                  Редактировать
                </button>
                <button @click="deleteArticle(article.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2">
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

const articles = ref([
  { id: 1, title: 'Путеводитель по Vue.js', author: 'Alice', publishedAt: '2023-06-01' },
  { id: 2, title: 'Развитие современных веб-технологий', author: 'Bob', publishedAt: '2023-06-05' }
]);

const addArticle = () => {
  console.log('Adding new article');
  
  // Logic to add a new article
};

const editArticle = (id) => {
  console.log('Editing article with ID:', id);
  // Logic to edit an existing article
};

const deleteArticle = (id) => {
  console.log('Deleting article with ID:', id);
  // Logic to delete an article
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
</style>