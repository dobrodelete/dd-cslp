<template>
    <transition name="fade">
      <div v-if="visible" :class="`bg-${type}-500 text-white px-4 py-2 rounded`" @click="hide">
        {{ message }}
      </div>
    </transition>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const props = defineProps({
    type: {
      type: String,
      default: 'info' // 'info', 'success', 'error'
    },
    message: String,
    duration: {
      type: Number,
      default: 3000
    }
  });
  
  const visible = ref(false);
  
  const show = () => {
    visible.value = true;
    setTimeout(() => {
      visible.value = false;
    }, props.duration);
  };
  
  const hide = () => {
    visible.value = false;
  };
  
  watch(() => props.message, (newVal) => {
    if (newVal) {
      show();
    }
  });
  </script>
  
  <style>
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  </style>
  