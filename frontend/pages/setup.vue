<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-6">Начальная настройка системы</h1>
    <section class="mb-6">
      <h2 class="text-2xl font-bold mb-4">Настройка профиля администратора</h2>
      <form @submit.prevent="setupAdminProfile">
        <div class="mb-4">
          <label for="adminName" class="block text-gray-700 text-sm font-bold mb-2">Имя администратора:</label>
          <input type="text" id="adminName" v-model="adminProfile.name" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Введите ваше имя">
        </div>
        <div class="mb-4">
          <label for="adminEmail" class="block text-gray-700 text-sm font-bold mb-2">Email:</label>
          <input type="email" id="adminEmail" v-model="adminProfile.email" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Введите ваш email">
        </div>
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Сохранить профиль
        </button>
      </form>
    </section>
    <section class="mb-6">
      <h2 class="text-2xl font-bold mb-4">Общие настройки проекта</h2>
      <form @submit.prevent="setupProjectSettings">
        <!-- Пример поля для настройки -->
        <div class="mb-4">
          <label for="projectName" class="block text-gray-700 text-sm font-bold mb-2">Название проекта:</label>
          <input type="text" id="projectName" v-model="projectSettings.name" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Введите название проекта">
        </div>
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Сохранить настройки
        </button>
      </form>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const adminProfile = ref({
  name: '',
  email: ''
});

const projectSettings = ref({
  name: ''
});

const setupAdminProfile = () => {
  console.log('Admin profile saved:', adminProfile.value);
  // Добавьте логику отправки данных профиля администратора на сервер
};

const setupProjectSettings = () => {
  console.log('Project settings saved:', projectSettings.value);
  // Добавьте логику отправки общих настроек проекта на сервер
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
