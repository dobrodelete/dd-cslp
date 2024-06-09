<template>
  <NuxtLayout name="admin">
    <div class="p-5">
      <h1 class="text-3xl font-bold mb-6">Административная панель блога</h1>
      <div class="grid grid-cols-3 gap-4">
        <div class="bg-white p-4 shadow rounded-lg">
          <h2 class="text-xl font-semibold mb-4">Модерация постов</h2>
          <ul>
            <li v-for="post in postsToModerate" :key="post.id" class="mb-2">
              <p class="font-semibold">{{ post.title }}</p>
              <p class="text-sm text-gray-600">{{ post.excerpt }}</p>
              <div class="mt-2">
                <button @click="approvePost(post.id)" class="bg-green-500 hover:bg-green-700 text-white font-bold py-1 px-3 rounded">Одобрить</button>
                <button @click="rejectPost(post.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded">Отклонить</button>
              </div>
            </li>
          </ul>
        </div>
        <div class="bg-white p-4 shadow rounded-lg">
          <h2 class="text-xl font-semibold mb-4">Жалобы и репорты</h2>
          <ul>
            <li v-for="report in reports" :key="report.id" class="mb-2">
              <p class="font-semibold">{{ report.reason }}</p>
              <p class="text-sm text-gray-600">{{ report.details }}</p>
              <div class="mt-2">
                <button @click="resolveReport(report.id)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded">Решить</button>
              </div>
            </li>
          </ul>
        </div>
        <div class="bg-white p-4 shadow rounded-lg">
          <h2 class="text-xl font-semibold mb-4">Статистика</h2>
          <p>Количество постов: {{ totalPosts }}</p>
          <p>Количество жалоб: {{ totalReports }}</p>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';

const postsToModerate = ref([
  { id: 1, title: 'Новый пост о Vue.js', excerpt: 'Введение в новые возможности Vue.js...' },
  { id: 2, title: 'Исследование по кибербезопасности', excerpt: 'Анализ последних трендов в кибербезопасности...' }
]);

const reports = ref([
  { id: 1, reason: 'Спам', details: 'Пост содержит множество ссылок на внешние сайты.' },
  { id: 2, reason: 'Оскорбления', details: 'Комментарий содержит нецензурную брань.' }
]);

const totalPosts = ref(postsToModerate.value.length);
const totalReports = ref(reports.value.length);

const approvePost = (id) => {
  console.log('Approving post with ID:', id);
  // Logic to approve a post
};

const rejectPost = (id) => {
  console.log('Rejecting post with ID:', id);
  // Logic to reject a post
};

const resolveReport = (id) => {
  console.log('Resolving report with ID:', id);
  // Logic to resolve a report
};
</script>
