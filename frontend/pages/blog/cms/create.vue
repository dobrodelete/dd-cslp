<template>
  <NuxtLayout name="blog">
    <div class="container mx-auto p-6">
      <h1 class="text-3xl font-bold mb-6">Создание нового поста</h1>
      <form @submit.prevent="submitPost">
        <div class="mb-6">
          <label for="title" class="block text-gray-700 text-sm font-bold mb-2">Заголовок</label>
          <input type="text" id="title" v-model="post.title" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" required>
        </div>
        <div class="mb-6">
          <label for="content" class="block text-gray-700 text-sm font-bold mb-2">Контент</label>
          <textarea id="content" v-model="post.content" rows="10" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" required></textarea>
        </div>
        <div class="mb-6">
          <label for="image" class="block text-gray-700 text-sm font-bold mb-2">Изображение</label>
          <input type="file" id="image" @change="handleFileUpload" class="block w-full text-sm text-gray-500
            file:mr-4 file:py-2 file:px-4
            file:rounded-full file:border-0
            file:text-sm file:font-semibold
            file:bg-violet-50 file:text-violet-700
            hover:file:bg-violet-100
          "/>
        </div>
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Опубликовать</button>
      </form>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';

const post = ref({
  title: '',
  content: '',
  image: null
});

const submitPost = () => {
  console.log('Submitting post:', post.value);
  // Logic to submit the post to the server
};

const handleFileUpload = (event) => {
  post.value.image = event.target.files[0];
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
