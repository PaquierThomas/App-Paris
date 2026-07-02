<script setup>
defineProps(['match'])

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString('fr-FR', {
    day: '2-digit', month: 'long', year: 'numeric',
    hour: '2-digit', minute: '2-digit'
  })
}
</script>

<template>
  <div class="card">
    <div class="badge">{{ match.stage }}</div>
    <div class="teams">
      <span class="team">{{ match.equipe_domicile }}</span>
      <span class="vs">VS</span>
      <span class="team">{{ match.equipe_exterieure }}</span>
    </div>
    <p class="date">🗓 {{ formatDate(match.date) }}</p>
    <BetForm :match="match" />
  </div>
</template>

<style scoped>
.card {
  background: #141929;
  border: 1px solid #2a3050;
  border-radius: 12px;
  padding: 1.5rem;
  transition: transform 0.2s;
}
.card:hover {
  transform: translateY(-4px);
}
.badge {
  display: inline-block;
  background: #1e3a5f;
  color: #60a0ff;
  font-size: 0.7rem;
  padding: 0.3rem 0.7rem;
  border-radius: 20px;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.teams {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.8rem;
}
.team {
  font-size: 1rem;
  font-weight: bold;
  color: white;
  flex: 1;
  text-align: center;
}
.vs {
  color: #f0c040;
  font-weight: bold;
  padding: 0 0.5rem;
}
.date {
  color: #888;
  font-size: 0.85rem;
  text-align: center;
  margin-bottom: 1rem;
}
</style>