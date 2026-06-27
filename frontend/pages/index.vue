<script setup>
const { data, status, error } = await useFetch('http://localhost:8000/', {
  lazy: true
})

</script>

<template>
  <main>
    <h1>Mon App</h1>
    <p v-if="status === 'pending'">Chargement…</p>
    <p v-else-if="error">Erreur : {{ error?.message }}</p>
    <p v-else>{{ data?.message }}</p>
  </main>
</template>