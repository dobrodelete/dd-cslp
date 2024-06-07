<template>
  <NuxtLayout :name="layout">
    <div>
      <h1 class="text-3xl font-bold mb-4">Список пользователей</h1>
      <div class="overflow-x-auto">
        <table class="min-w-full bg-white">
          <thead>
            <tr class="w-full bg-gray-200 text-left">
              <th class="px-4 py-2">Имя</th>
              <th class="px-4 py-2">Email</th>
              <th class="px-4 py-2">Роль</th>
              <th class="px-4 py-2">Статус</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id" class="hover:bg-gray-100">
              <td class="border px-4 py-2">{{ user.name }}</td>
              <td class="border px-4 py-2">{{ user.email }}</td>
              <td class="border px-4 py-2">{{ user.role }}</td>
              <td class="border px-4 py-2">{{ user.status }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const users = ref([
  { id: 1, name: 'Alice Smith', email: 'alice@example.com', role: 'Admin', status: 'Active' },
  { id: 2, name: 'Bob Johnson', email: 'bob@example.com', role: 'User', status: 'Inactive' },
  { id: 3, name: 'Charlie Lee', email: 'charlie@example.com', role: 'User', status: 'Active' },
  { id: 4, name: 'Dana Bailey', email: 'dana@example.com', role: 'Moderator', status: 'Active' }
]);
const layout = "ddctf-admin"
</script>

<style>
table {
  border-collapse: collapse;
  width: 100%;
}
th, td {
  border: solid 1px #ddd;
  padding: 8px;
}
thead {
  background-color: #f9fafb;
}
tr:hover {
  background-color: #f1f1f1;
}
</style>