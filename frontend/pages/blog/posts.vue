<template>
  <div class="container mx-auto p-6">
    <div class="mb-6">
      <h1 class="text-3xl font-bold">Мои посты</h1>
      <button @click="newPost" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4">
        Создать новый пост
      </button>
    </div>
    <div>
      <ul>
        <li v-for="post in posts" :key="post.id" class="mb-4 p-4 bg-white shadow rounded">
          <h2 class="text-xl font-semibold">{{ post.title }}</h2>
          <p class="text-gray-600">{{ post.excerpt }}</p>
          <div class="flex space-x-4 mt-4">
            <button @click="editPost(post.id)" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
              Редактировать
            </button>
            <button @click="deletePost(post.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
              Удалить
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const posts = ref([
  { id: 1, title: 'Пост о Vue.js', excerpt: 'Краткое описание моего поста о Vue.js...' },
  { id: 2, title: 'Пост о Nuxt.js', excerpt: 'Краткое описание моего поста о Nuxt.js...' }
]);

const newPost = () => {
  console.log('Redirect to new post creation page');
  // Logic to redirect to the post creation form
};

const editPost = (id) => {
  console.log('Redirect to edit page of post with ID:', id);
  // Logic to redirect to the post editing form
};

const deletePost = (id) => {
  console.log('Deleting post with ID:', id);
  // Logic to delete the post
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin-bottom: 1rem;
}
</style>
