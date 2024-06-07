<template>
  <table class="min-w-full divide-y divide-gray-200">
    <thead class="bg-gray-50">
      <tr>
        <th v-for="header in headers" :key="header" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider text-black">
          {{ header }}
        </th>
      </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-200">
      <tr v-for="item in items" :key="item.id">
        <td v-for="(header, index) in headers" :key="index" class="px-6 py-4 whitespace-nowrap text-black">
          {{ item[header] }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
const props = defineProps({
  items: Array,
  headers: Array
});
</script>
