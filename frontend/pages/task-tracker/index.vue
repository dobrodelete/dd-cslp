<template>
  <NuxtLayout name="task-tracker">
    <div class="flex-1 justify-start">
      <BoardSwitcher />
      <div ref="container" class="kanban">
        <div v-for="status in statuses" :key="status" class="kanban-column">
          <h3 class="font-bold text-lg mb-2">{{ status }}</h3>
          <div :ref="setStatusRef">
            <div v-for="task in getTasksForStatus(status)" :key="task.id"
              class="kanban-item" @dblclick="editTask(task)">
              {{ task.title }}
            </div>
          </div>
        </div>
      </div>
    </div>

  </NuxtLayout>
</template>

<script setup>
import { onMounted, ref } from 'vue';
// import { Sortable } from '@shopify/draggable';
// import { BoardSwitcher } from "~/components/task-tracker/BoardSwitcher.vue"
import BoardSwitcher from '~/components/task-tracker/BoardSwitcher.vue'


if (process.client) {
  const { Sortable } = await import('@shopify/draggable');
}

const statuses = ['To Do', 'In Progress', 'Done'];
const tasks = ref([
  { id: 1, title: 'Задача 1', status: 'To Do' },
  { id: 2, title: 'Задача 2', status: 'In Progress' },
  { id: 3, title: 'Задача 3', status: 'Done' }
]);
const container = ref(null);

const getTasksForStatus = (status) => {
  return tasks.value.filter(task => task.status === status);
};

onMounted(() => {
  new Sortable(container.value, {
    draggable: '.kanban-item',
    delay: 0,
    onSort: (event) => {
      console.log(event.newIndex, event.oldIndex);
      // Update tasks array based on new index
    }
  });
});
</script>

<style>
.kanban { display: flex; }
.kanban-column { width: 33%; padding: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.kanban-item { padding: 8px; margin: 4px; background-color: white; cursor: pointer; }
</style>
