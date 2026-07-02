<script setup>
const props = defineProps(['match'])

const pseudo = ref('')
const choix = ref('')
const mise = ref(0)
const success = ref(false)
const error = ref(false)

async function submitBet() {
  success.value = false
  error.value = false
  try {
    await $fetch('http://localhost:8000/bets', {
      method: 'POST',
      body: {
        pseudo: pseudo.value,
        match_id: props.match.id,
        choix: choix.value,
        mise: mise.value
      }
    })
    success.value = true
    pseudo.value = ''
    choix.value = ''
    mise.value = 0
  } catch {
    error.value = true
  }
}
</script>

<template>
  <div class="form">
    <h4>🎯 Votre pari</h4>
    <input v-model="pseudo" placeholder="Votre pseudo" />
    <select v-model="choix">
      <option value="">Choisir le gagnant</option>
      <option :value="match.equipe_domicile">{{ match.equipe_domicile }}</option>
      <option :value="match.equipe_exterieure">{{ match.equipe_exterieure }}</option>
    </select>
    <input v-model.number="mise" type="number" placeholder="Mise (€)" min="1" />
    <button @click="submitBet">Parier</button>
    <p class="success" v-if="success">✅ Pari enregistré !</p>
    <p class="error" v-if="error">❌ Erreur, réessayez.</p>
  </div>
</template>

<style scoped>
.form {
  border-top: 1px solid #2a3050;
  padding-top: 1rem;
  margin-top: 1rem;
}
.form h4 {
  color: #f0c040;
  margin-bottom: 0.8rem;
}
input, select {
  width: 100%;
  padding: 0.6rem;
  margin-bottom: 0.6rem;
  background: #0d1220;
  border: 1px solid #2a3050;
  border-radius: 8px;
  color: white;
  font-size: 0.9rem;
  box-sizing: border-box;
}
button {
  width: 100%;
  padding: 0.7rem;
  background: #f0c040;
  color: #0a0f1e;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s;
}
button:hover {
  background: #ffd700;
}
.success { color: #4caf50; margin-top: 0.5rem; }
.error { color: #f44336; margin-top: 0.5rem; }
</style>