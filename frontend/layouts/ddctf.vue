<template>
  <NuxtLayout name="base">
    <div>
      <CTFNavbar />
      <slot />
    </div>
  </NuxtLayout>
</template>


<script lang="ts" setup>
import CTFNavbar from '~/components/ddctf/CTFNavbar.vue'

</script>

<style>

</style>
