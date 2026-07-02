<script setup>
const { data: matchs } = await useFetch('http://localhost:8000/prochains_matchs', {
  lazy: true
})
</script>

<template>
  <main class="container">
    <header class="header">
      <h1>⚽ Coupe du Monde 2026</h1>
      <p>Pariez sur vos matchs favoris</p>
    </header>
    <div class="grid" v-if="matchs">
      <MatchCard v-for="match in matchs" :key="match.id" :match="match" />
    </div>
    <p v-else class="loading">Chargement des matchs...</p>
  </main>
</template>

<style scoped>
body{
  background: #0a0f1e;
  margin: 0;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Segoe UI', sans-serif;
  min-height: 100vh;
  color: white;
}
.header {
  text-align: center;
  margin-bottom: 2rem;
}
.header h1 {
  font-size: 2.5rem;
  color: #f0c040;
}
.header p {
  color: #aaa;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}
.loading {
  text-align: center;
  color: #aaa;
}
</style>