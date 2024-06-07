<template>
  <select v-model="selected" @change="onChange" class="p-2 border rounded">
    <option disabled value="">{{ placeholder }}</option>
    <option v-for="option in options" :key="option.value" :value="option.value">
      {{ option.text }}
    </option>
  </select>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';

const props = defineProps({
  options: Array,
  placeholder: String
});

const selected = ref('');

const emit = defineEmits(['change']);

const onChange = () => {
  emit('change', selected.value);
};

watch(() => props.options, (newVal) => {
  if (!newVal.find(option => option.value === selected.value)) {
    selected.value = '';
  }
}, { immediate: true });
</script>
