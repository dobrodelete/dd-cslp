<template>
  <NuxtLayout name="ddctf">
    <div class="p-5">
      <h1 class="text-3xl font-bold text-center mb-6">Уведомления</h1>
      <div class="max-w-4xl mx-auto">
        <ul class="space-y-4">
          <li v-for="notification in notifications" :key="notification.id" class="bg-white rounded-md shadow p-4">
            <div class="flex justify-between items-start">
              <div>
                <h3 class="font-semibold text-lg">{{ notification.title }}</h3>
                <p class="text-gray-600 mt-1">{{ notification.message }}</p>
              </div>
              <button class="text-gray-400 hover:text-gray-500" @click="dismissNotification(notification.id)">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            <div class="text-right text-sm text-gray-500 mt-2">{{ notification.date }}</div>
          </li>
        </ul>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';

const notifications = ref([
  { id: 1, title: 'Добро пожаловать', message: 'Спасибо за регистрацию на нашем сайте!', date: '2023-06-01' },
  { id: 2, title: 'Обновление системы', message: 'Мы обновили условия использования.', date: '2023-06-02' },
  { id: 3, title: 'Новая задача', message: 'Новая задача Crypto Challenge теперь доступна.', date: '2023-06-03' }
]);

const dismissNotification = (id) => {
  notifications.value = notifications.value.filter(n => n.id !== id);
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

li {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

button {
  background: none;
  border: none;
  cursor: pointer;
}

h3 {
  margin-top: 0;
}

p {
  margin-bottom: 0;
}
</style>