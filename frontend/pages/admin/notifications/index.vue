<template>
  <NuxtLayout name="admin-panel">
    <div class="container mx-auto p-6">
      <h1 class="text-3xl font-bold mb-6">Рассылка уведомлений</h1>
      <form @submit.prevent="sendNotifications">
        <div class="mb-4">
          <label for="message" class="block text-gray-700 text-sm font-bold mb-2">Сообщение:</label>
          <textarea id="message" v-model="notification.message" rows="4" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" placeholder="Введите ваше сообщение здесь..."></textarea>
        </div>
        <div class="mb-4">
          <label for="userGroup" class="block text-gray-700 text-sm font-bold mb-2">Группа пользователей:</label>
          <select id="userGroup" v-model="notification.userGroup" class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
            <option value="all">Все пользователи</option>
            <option value="admins">Администраторы</option>
            <option value="users">Пользователи</option>
          </select>
        </div>
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Отправить уведомление
        </button>
      </form>
    </div>
    </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';

const notification = ref({
  message: '',
  userGroup: 'all'
});

const sendNotifications = () => {
  console.log('Sending notifications to:', notification.value.userGroup);
  console.log('Message:', notification.value.message);
  // Здесь добавьте логику отправки уведомлений через ваш сервер или API
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
