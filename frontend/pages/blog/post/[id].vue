<template>
  <div class="container mx-auto p-6">
    <article>
      <header class="mb-6">
        <h1 class="text-4xl font-bold mb-2">{{ post.title }}</h1>
        <div class="text-gray-600 mb-4">
          <span>Опубликовано {{ post.date }}</span>
        </div>
      </header>
      <section v-html="post.content" class="post-content mb-6"></section>
      <div class="flex items-center mb-6">
        <button @click="likePost" class="mr-2">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3 12.75l7.5 6 10.5-11.25m0 0H9.75m3-8.25h-3v7.5h3V3.75z" />
          </svg>
          <span>{{ likes }}</span>
        </button>
        <button @click="dislikePost">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3 12.75l7.5-6 10.5 11.25m0 0H9.75m3 8.25h-3v-7.5h3v7.5z" />
          </svg>
          <span>{{ dislikes }}</span>
        </button>
      </div>
      <pre class="bg-gray-100 p-4 rounded"><code>{{ post.codeBlock }}</code></pre>
      <section class="comments mt-8">
        <h2 class="text-2xl font-semibold mb-4">Комментарии</h2>
        <ul>
          <li v-for="comment in post.comments" :key="comment.id" class="mb-4">
            <strong>{{ comment.author }}</strong> <span class="text-gray-600">{{ comment.date }}</span>
            <p>{{ comment.text }}</p>
          </li>
        </ul>
      </section>
    </article>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const post = ref({
  id: 1,
  title: 'Глубокое погружение в Vue.js',
  date: '2023-06-01',
  content: '<p>Детальный обзор возможностей и примеры использования Vue.js в реальных проектах.</p>',
  codeBlock: 'console.log("Hello, Vue!");',
  comments: [
    { id: 1, author: 'Alice', date: '2023-06-02', text: 'Отличная статья!' },
    { id: 2, author: 'Bob', date: '2023-06-03', text: 'Жду продолжения!' }
  ]
});

const likes = ref(10);
const dislikes = ref(3);

const likePost = () => {
  likes.value++;
};

const dislikePost = () => {
  dislikes.value++;
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
.post-content p {
  margin-bottom: 1rem;
}
.comments ul {
  list-style: none;
  padding: 0;
}
</style>
