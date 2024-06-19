<template>
  <div v-if="visible" class="modal">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">{{ isNew ? 'Добавить событие' : 'Редактировать событие' }}</p>
        <button class="delete" aria-label="close" @click="close"></button>
      </header>
      <section class="m-3">
        <div>
          <label class="label">Название</label>
          <div class="control">
            <input class="input mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400"
                   type="text"
                   placeholder="Введите название события"
                   v-model="eventData.name">
          </div>
        </div>
        <div>
          <label class="label">Описание</label>
          <div class="control">
            <input class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400"
                   placeholder="Введите описание события"
                   v-model="eventData.description"/>
          </div>
        </div>
        <div>
          <label class="label">Время начала</label>
          <input type="datetime-local" lang="ru-RU" class="input mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm"
                 v-model="eventData.start_time">
        </div>
        <div>
          <label class="label">Время окончания</label>
          <input type="datetime-local" lang="ru-RU" class="input mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm"
                 v-model="eventData.end_time">
        </div>
        <div class="flex items-center mt-2">
          <input type="checkbox" id="active" v-model="eventData.active">
          <label for="active" class="ml-2 text-sm text-gray-700">Активно</label>
        </div>
      </section>
      <footer class="modal-card-foot flex justify-end space-x-4">
        <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="close">Отмена</button>
        <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" @click="save">Сохранить</button>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect, defineProps, defineEmits } from 'vue';
import { format, parseISO } from 'date-fns';
import { useApi } from '@/composables/useApi';

const props = defineProps({
  visible: Boolean,
  isNew: Boolean,
  initialData: Object
});

const emit = defineEmits(['update:visible', 'refreshEvents']);
// Преобразование дат при инициализации
const eventData = ref({
  ...props.initialData,
  start_time: props.initialData.start_time ? format(parseISO(props.initialData.start_time), "yyyy-MM-dd'T'HH:mm") : '',
  end_time: props.initialData.end_time ? format(parseISO(props.initialData.end_time), "yyyy-MM-dd'T'HH:mm") : ''
});

watchEffect(() => {
  // Обновление дат при изменении props
  eventData.value = {
    ...props.initialData,
    start_time: props.initialData.start_time ? format(parseISO(props.initialData.start_time), "yyyy-MM-dd'T'HH:mm") : '',
    end_time: props.initialData.end_time ? format(parseISO(props.initialData.end_time), "yyyy-MM-dd'T'HH:mm") : ''
  };
});

const { create, update } = useApi('ddctf/ctf_event');

const save = async () => {
  try {
    let dataToSave = {
      ...eventData.value,
      start_time: parseISO(eventData.value.start_time),  // Парсинг обратно в формат ISO для отправки на сервер
      end_time: parseISO(eventData.value.end_time)
    };
    if (eventData.value.id) {
      await update(eventData.value.id, dataToSave);
    } else {
      await create(dataToSave);
    }
    emit('refreshEvents');
    emit('update:visible', false);
  } catch (error) {
    console.error('Ошибка API:', error.message);
  }
};

const close = () => {
  emit('update:visible', false);
};
</script>

<style scoped>
.modal {
  position: fixed;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  animation: fadeIn 0.3s;
}

.modal-background {
  position:absolute;
  background-color: rgba(10, 10, 10, 0.86);
  width: 100%;
  height: 100%;
  animation: fadeBackgroundIn 0.3s;
}

.modal-card {
  position: relative;
  background: white;
  border-radius: 5px;
  padding: 20px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.2);
  animation: scaleIn 0.3s;
  overflow: hidden;
}

.delete {
  background: transparent;
  border: none;
  font-size: 1.5rem;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeBackgroundIn {
  from { background-color: rgba(10, 10, 10, 0); }
  to { background-color: rgba(10, 10, 10, 0.86); }
}

@keyframes scaleIn {
  from { transform: scale(0.7); }
  to { transform: scale(1); }
}
</style>
