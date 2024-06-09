<template>
  <NuxtLayout name="admin">
    <!-- <UVerticalNavigation :links="links" /> -->
    <div class="p-5">
      <h1 class="text-3xl font-bold mb-6">Административная панель</h1>
      <div class="grid grid-cols-2 gap-4">
        <div class="bg-white p-4 shadow rounded-lg">
          <h2 class="text-xl font-semibold mb-4">Управление модулями</h2>
          <ul class="list-none">
            <li><nuxt-link to="/admin/ddctf" class="text-blue-500 hover:text-blue-700">DDCTF</nuxt-link></li>
            <li><nuxt-link to="/admin/blog" class="text-blue-500 hover:text-blue-700">Blog</nuxt-link></li>
            <li><nuxt-link to="/admin/task-tracker" class="text-blue-500 hover:text-blue-700">Task Tracker</nuxt-link></li>
          </ul>
        </div>
        <div class="bg-white p-4 shadow rounded-lg">
          <h2 class="text-xl font-semibold mb-4">Действия администратора</h2>
          <button @click="sendNewsletter" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">Сделать рассылку</button>
        </div>
      </div>
    </div>
    
  </NuxtLayout>
</template>

<script setup>
const sendNewsletter = () => {
  console.log('Рассылка отправлена');
};

const route = useRoute()

const links = [{
  label: 'ddCTF',
  icon: 'arcticons--nethack',
  to: '/admin/ddctf'
}, {
  label: 'Blog',
  icon: 'carbon--blog',
  to: '/admin/blog'
}, {
  label: 'Task Tracker',
  icon: 'material-symbols--task',
  to: '/admin/task-tracker'
}]

</script>

<style scoped>
ul {
  padding: 0;
}
li {
  margin-bottom: 1rem;
}
</style>
