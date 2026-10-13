<script setup>
import { reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const busqueda = reactive({ origen: String(route.query.origen || ''), destino: String(route.query.destino || ''), fecha: String(route.query.fecha || '') })
const fechaMin = new Date().toLocaleDateString('en-CA')
const aviso = ref('')
function consultar() {
  aviso.value = busqueda.origen && busqueda.destino && busqueda.fecha
    ? 'La búsqueda de horarios y disponibilidad se habilitará al integrar el backend.'
    : 'Completa los campos antes de buscar.'
}
</script>
<template>
  <div class="trips page-container">
    <div class="page-heading"><RouterLink class="breadcrumb" to="/">← Volver al inicio</RouterLink><span class="section-kicker">ENCUENTRA TU PRÓXIMO DESTINO</span><h1>Buscar viajes</h1><p>Elige la ciudad de salida, el destino y la fecha en que deseas viajar.</p></div>
    <div class="trips-layout">
      <section class="trips-form-card"><div class="trips-card-head"><span class="benefit-icon">⌕</span><div><h2>Personaliza tu búsqueda</h2><p>Completa la información de tu viaje.</p></div></div><form class="trips-form" @submit.prevent="consultar"><label class="field">Ciudad de origen<input v-model.trim="busqueda.origen" placeholder="Ej. Ambato" required /></label><label class="field">Ciudad de destino<input v-model.trim="busqueda.destino" placeholder="Ej. Quito" required /></label><label class="field">Fecha de salida<input v-model="busqueda.fecha" :min="fechaMin" type="date" required /></label><button class="search-submit" type="submit">Consultar viajes →</button></form><p v-if="aviso" class="information-note" role="status">{{ aviso }}</p></section>
      <section class="results-placeholder"><div class="empty-illustration" aria-hidden="true">↗</div><span class="section-kicker">PRÓXIMAMENTE</span><h2>Tu próxima aventura comienza aquí</h2><p>Esta es la interfaz inicial de búsqueda. Cuando se incorpore el servicio de viajes, aquí aparecerán horarios, cooperativas y disponibilidad.</p><span class="coming-soon">Sin resultados reales por el momento</span></section>
    </div>
  </div>
</template>
