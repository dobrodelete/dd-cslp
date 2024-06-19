<template>
  <NuxtLayout name="admin-panel">
    <div class="container mx-auto p-6">
      <h1 class="text-3xl font-bold mb-6">Настройки администратора</h1>
      <section class="mb-6">
        <h2 class="text-2xl font-bold mb-4">Безопасность</h2>
        <form @submit.prevent="updateSecuritySettings">
          <div class="mb-4">
            <label for="passwordPolicy" class="block text-gray-700 text-sm font-bold mb-2">Политика паролей:</label>
            <select id="passwordPolicy" v-model="settings.passwordPolicy" class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
              <option value="low">Низкая</option>
              <option value="medium">Средняя</option>
              <option value="high">Высокая</option>
            </select>
          </div>
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Сохранить настройки безопасности
          </button>
        </form>
      </section>
      <section class="mb-6">
        <h2 class="text-2xl font-bold mb-4">Управление пользователями</h2>
        <form @submit.prevent="updateUserSettings">
          <div class="mb-4">
            <label for="userRoles" class="block text-gray-700 text-sm font-bold mb-2">Роли пользователей:</label>
            <input type="text" id="userRoles" v-model="settings.userRoles" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
          </div>
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Обновить управление пользователями
          </button>
        </form>
      </section>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue';

const settings = ref({
  passwordPolicy: 'medium',
  userRoles: 'Админ, Пользователь, Гость'
});

const updateSecuritySettings = () => {
  console.log('Security settings updated:', settings.value.passwordPolicy);
};

const updateUserSettings = () => {
  console.log('User management settings updated:', settings.value.userRoles);
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
