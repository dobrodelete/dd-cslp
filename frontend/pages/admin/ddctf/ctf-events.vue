<template>
  <NuxtLayout :name="layout">
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl font-bold mb-4">CTF Events</h1>
        <div class="mb-4">
          <button @click="openAddEventModal" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4">
            Add New Event
          </button>
          <EventModal :initialData="selectedEvent" :visible="isModalVisible" :isNew="isNew" @update:visible="isModalVisible = $event" @refreshEvent="fetchEvents" />
        </div>
        <div v-if="events.length > 0" class="overflow-x-auto">
          <table class="min-w-full bg-white">
            <thead>
              <tr class="w-full bg-gray-200 text-left">
                <th class="px-4 py-2">Название</th>
                <th class="px-4 py-2">Описание</th>
                <th class="px-4 py-2">Начало</th>
                <th class="px-4 py-2">Конец</th>
                <th class="px-4 py-2">Активно</th>
                <th class="px-4 py-2">Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="event in events" :key="event.id">
                <td class="border px-4 py-2">{{ event.name }}</td>
                <td class="border px-4 py-2">{{ event.description }}</td>
                <td class="border px-4 py-2">{{ event.start_time }}</td>
                <td class="border px-4 py-2">{{ event.end_time }}</td>
                <td class="border px-4 py-2">{{ event.active }}</td>
                <td class="border px-4 py-2">
                  <button @click="openEditEventModal(event)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Редактировать</button>
                  <button @click="deleteEvent(event.id)" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2">Удалить</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else-if="events.length === 0" class="text-center py-4">
          Нет событий.
        </div>
        <div v-if="totalEvents > pageSize" class="pagination">
          <button @click="changePage(currentPage - 1)" :disabled="currentPage.value <= 1">Назад</button>
          <span>Страница {{ currentPage }} из {{ totalPages }}</span>
          <button @click="changePage(currentPage + 1)" :disabled="currentPage.value >= totalPages.value">Вперед</button>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script>
import { ref, onMounted, computed, nextTick } from 'vue';
import EventModal from '@/components/admin/EventModal.vue';
import { useApi } from '~/composables/useApi';

export default {
  components: {
    EventModal
  },
  setup() {
    const layout = ref("admin-ctf");
    const events = ref([]);
    const isModalVisible = ref(false);
    const selectedEvent = ref({});
    const isNew = ref(true);
    const api = useApi("ddctf/ctf_event");
    const currentPage = ref(1);
    const pageSize = ref(10);
    const totalEvents = ref(0);
    const totalPages = computed(() => Math.ceil(totalEvents.value / pageSize.value));

    const fetchEvents = async (page = currentPage.value) => {
      const skip = (page - 1) * pageSize.value;
      const limit = pageSize.value;
      try {
        const { events: fetchedEvents, total } = await api.list({ skip, limit });
        events.value = fetchedEvents;
        totalEvents.value = total;
        await nextTick();
        console.log(events)
      } catch (error) {
        console.error("Error fetching events:", error);
      }
    };

    const openAddEventModal = () => {
      selectedEvent.value = { name: '', description: '', start_time: '', end_time: '', active: false };
      isNew.value = true;
      isModalVisible.value = true;
    };

    const openEditEventModal = (event) => {
      selectedEvent.value = { ...event };
      isNew.value = false;
      isModalVisible.value = true;
    };

    const deleteEvent = async (id) => {
      await api.remove(id);
      await fetchEvents(currentPage.value);
    };

    const changePage = (page) => {
      if (page < 1 || page > totalPages.value) return;
      currentPage.value = page;
      fetchEvents(page);
    };

    onMounted(() => {
      fetchEvents(currentPage.value);
    });

    return { 
      layout,
      events,
      isModalVisible,
      selectedEvent,
      isNew,
      fetchEvents,
      openAddEventModal,
      openEditEventModal,
      deleteEvent,
      currentPage,
      totalPages,
      changePage,
      pageSize,
      totalEvents
    };
  }
};
</script>

<style>

</style>