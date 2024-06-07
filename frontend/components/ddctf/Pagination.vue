<template>
  <div class="flex items-center justify-between border-t border-gray-200 bg-white px-4 py-3 sm:px-6">
    <div class="flex-1 flex justify-between sm:hidden">
      <button @click="onPrev" :disabled="currentPage <= 1" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
        Назад
      </button>
      <button @click="onNext" :disabled="currentPage >= totalPages" class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
        Вперед
      </button>
    </div>
    <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
      <div>
        <p class="text-sm text-gray-700">
          Страница <span class="font-medium">{{ currentPage }}</span> из <span class="font-medium">{{ totalPages }}</span>
        </p>
      </div>
      <div>
        <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
          <button @click="onPrev" :disabled="currentPage <= 1" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
            <span class="sr-only">Previous</span>
            <!-- Heroicons name: solid/chevron-left -->
            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 010 1.414L9.414 9.5l2.879 2.793a1 1 0 11-1.414 1.414L7.293 10.207a1 1 0 010-1.414l3.586-3.586a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
          </button>
          <!-- Current Page indicator and inter-page links can be added here if needed -->
          <button @click="onNext" :disabled="currentPage >= totalPages" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
            <span class="sr-only">Next</span>
            <!-- Heroicons name: solid/chevron-right -->
            <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M7.707 14.707a1 1 0 010-1.414L10.586 10.5 7.707 7.707a1 1 0 011.414-1.414l3.586 3.586a1 1 0 010 1.414l-3.586 3.586a1 1 0 01-1.414 0z" clip-rule="evenodd" />
            </svg>
          </button>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  currentPage: Number,
  totalPages: Number
});

const emit = defineEmits(['update:currentPage']);

const onPrev = () => {
  if (props.currentPage > 1) {
    emit('update:currentPage', props.currentPage - 1);
  }
};

const onNext = () => {
  if (props.currentPage < props.totalPages) {
    emit('update:currentPage', props.currentPage + 1);
  }
};
</script>

<style>
/* Optional: Add your styles here */
</style>
