<template>
  <div v-if="visible" class="modal">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">{{ isNew ? 'Добавить категорию' : 'Редактировать категорию' }}</p>
        <button class="delete" aria-label="close" @click="close"></button>
      </header>
      <section class="m-3">
        <div>
          <label class="label">Название</label>
          <div class="control">
            <input class="input mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400"
                   type="text"
                   placeholder="Введите название категории"
                   v-model="category.name">
          </div>
        </div>
        <div>
          <label class="label">Описание</label>
          <div class="control">
            <input class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400"
                   placeholder="Введите описание категории"
                   v-model="category.description"/>
          </div>
        </div>
      </section>
      <footer class="modal-card-foot flex flex-row flex-wrap justify-around mt-3">
        <button class="bg-green-500 hover:bg-green-500 rounded-xl px-3 py-2" @click="save">Сохранить</button>
        <button class="bg-red-500 hover:bg-red-500 rounded-xl px-3 py-2" @click="close">Отмена</button>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect, defineProps, defineEmits } from 'vue';
import { useApi } from '@/composables/useApi';

const props = defineProps({
  visible: Boolean,
  isNew: Boolean,
  initialData: Object
});

const emit = defineEmits(['update:visible', 'refreshCategories']);
const category = ref({ ...props.initialData });

watchEffect(() => {
  category.value = { ...props.initialData };
});

const { create, update } = useApi('ddctf/categories');

const save = async () => {
  try {
    if (category.value.id) {
      await update(category.value.id, category.value);
    } else {
      await create(category.value);
    }
    emit('refreshCategories');
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
  position: absolute;
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

.modal-card-head {
  padding: 10px 20px;
  background: #f5f5f5;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-card-title {
  font-size: 1.5rem;
  color: #363636;
}

.delete {
  background: transparent;
  border: none;
  font-size: 1.5rem;
}

.modal-card-foot {
  display: flex;
  justify-content: flex-end;
  padding: 10px 20px;
  background: #f5f5f5;
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}

.button {
  border: none;
  color: white;
  padding: 10px 20px;
  margin: 0 10px;
  border-radius: 4px;
  cursor: pointer;
}

.button.is-success {
  background-color: #48c774;
}

.button:hover {
  opacity: 0.8;
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
