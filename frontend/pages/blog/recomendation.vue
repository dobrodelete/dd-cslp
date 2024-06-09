<template>
  <NuxtLayout name="blog">
    <div class="container mx-auto p-6">
      <header class="mb-8">
        <h1 class="text-4xl font-bold">Рекомендуем:</h1>
      </header>
      <div class="flex">
        <main class="flex-grow pr-4">
          <ul>
            <li v-for="post in posts" :key="post.id" class="mb-6">
              <nuxt-link :to="`/blog/post/${post.id}`" class="text-2xl font-semibold hover:text-blue-500">
                {{ post.title }}
              </nuxt-link>
              <p class="text-gray-600">{{ post.excerpt }}</p>
            </li>
          </ul>
        </main>
        <aside class="w-1/4">
          <div class="sticky top-4">
            <input type="text" placeholder="Поиск..." class="w-full p-2 mb-4 border rounded">
            <h3 class="font-bold mb-2">Может быть интересно:</h3>
            <ul>
              <li v-for="popular in popularPosts" :key="popular.id" class="mb-2">
                <nuxt-link :to="`/blog/post/${popular.id}`" class="hover:text-blue-500">
                  {{ popular.title }}
                </nuxt-link>
              </li>
            </ul>
          </div>
        </aside>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
const layout = "blog"
const posts = [
  { id: 1, title: 'Новости о кибербезопасности', excerpt: 'Последние новости о кибербезопасности и что это значит для вас...' },
  { id: 2, title: 'Глубокое погружение в Vue.js', excerpt: 'Изучите углубленные аспекты Vue.js через эту детальную статью...' },
  { id: 3, title: 'Будущее веб-разработки', excerpt: 'Какие технологии определят следующее десятилетие в веб-разработке?' }
];

const popularPosts = [
  { id: 1, title: 'Введение в Nuxt.js' },
  { id: 2, title: 'Руководство по кибербезопасности' },
  { id: 3, title: 'Советы по производительности Vue' }
];
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style>
