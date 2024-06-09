<template>
  <NuxtLayout name="blog">
    <div class="container mx-auto p-6">
    <header class="mb-8">
      <h1 class="text-4xl font-bold">Блог</h1>
    </header>
    <div class="grid grid-cols-3 gap-4">
      <div v-for="post in posts" :key="post.id" class="bg-white rounded overflow-hidden shadow-lg">
        <img :src="post.image" alt="Post image" class="w-full h-48 object-cover">
        <div class="p-4">
          <h2 class="font-bold text-xl mb-2">{{ post.title }}</h2>
          <p class="text-gray-700 text-base">{{ post.excerpt }}</p>
          <nuxt-link :to="`/blog/post/${post.id}`" class="inline-block bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4">
            Читать далее
          </nuxt-link>
        </div>
      </div>
    </div>
  </div>
  </NuxtLayout>
</template>

<script setup>
const layout = "blog"
const posts = ref([
  { 
    id: 1, 
    title: 'Новости о кибербезопасности', 
    excerpt: 'Последние новости о кибербезопасности и что это значит для вас...',
    image: 'https://via.placeholder.com/400x300'
  },
  { 
    id: 2, 
    title: 'Глубокое погружение в Vue.js', 
    excerpt: 'Изучите углубленные аспекты Vue.js через эту детальную статью...',
    image: 'https://via.placeholder.com/400x300'
  },
  { 
    id: 3, 
    title: 'Будущее веб-разработки', 
    excerpt: 'Какие технологии определят следующее десятилетие в веб-разработке?',
    image: 'https://via.placeholder.com/400x300'
  }
]);
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style>
