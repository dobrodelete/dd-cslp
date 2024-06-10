<template>
  <NuxtLayout name="admin-blog">
    <div class="container mx-auto p-6">
      <article class="bg-white p-6 shadow rounded-lg">
        <header>
          <h1 class="text-3xl font-bold mb-4">{{ post.title }}</h1>
        </header>
        <section v-html="post.content" class="mb-6"></section>
        <footer class="flex justify-between">
          <button @click="approvePost(post.id)" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
            Одобрить
          </button>
          <button @click="rejectPost(post.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
            Отклонить
          </button>
        </footer>
      </article>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';

const post = ref({
  id: 1,
  title: 'Пример поста для предварительного просмотра',
  content: '<p>Текст поста с детальным описанием и анализом. Включает изображения, ссылки и другие элементы форматирования, которые нужно проверить перед публикацией.</p>'
});

const approvePost = (id) => {
  console.log('Approving post with ID:', id);
  // Add logic to approve the post
};

const rejectPost = (id) => {
  console.log('Rejecting post with ID:', id);
  // Add logic to reject the post
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
