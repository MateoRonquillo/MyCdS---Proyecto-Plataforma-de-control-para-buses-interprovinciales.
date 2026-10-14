<script setup>
import { ref } from 'vue'
import { useAppStore } from '../../stores/app'
const app = useAppStore()
const menuAbierto = ref(false)
</script>

<template>
  <div class="layout-publico">
    <header class="site-header">
      <div class="site-topline">Rutas interprovinciales · Ecuador <span>Tu próximo destino comienza aquí</span></div>
      <div class="header-inner">
        <RouterLink to="/" class="brand" @click="menuAbierto = false" :aria-label="`${app.nombre} - Inicio`">
          <span class="brand-symbol" aria-hidden="true">↗</span>
          <span class="brand-text">Rutas<span>Ecuador</span><small>Viaja más fácil</small></span>
        </RouterLink>
        <button class="menu-toggle" type="button" :aria-expanded="menuAbierto" aria-controls="nav-publica" @click="menuAbierto = !menuAbierto">
          <span aria-hidden="true">☰</span> Menú
        </button>
        <nav id="nav-publica" class="site-nav" :class="{ abierta: menuAbierto }" aria-label="Navegación principal">
          <RouterLink to="/" @click="menuAbierto = false">Inicio</RouterLink>
          <RouterLink to="/viajes" @click="menuAbierto = false">Buscar viajes</RouterLink>
          <RouterLink class="nav-cta" to="/viajes" @click="menuAbierto = false">Explorar rutas <span aria-hidden="true">→</span></RouterLink>
        </nav>
      </div>
    </header>
    <main id="contenido" class="public-main"><RouterView /></main>
    <footer class="site-footer">
      <div class="footer-inner">
        <div><strong>↗ RutasEcuador</strong><p>Una mejor forma de planificar tus viajes por Ecuador.</p></div>
        <div class="footer-links"><RouterLink to="/">Inicio</RouterLink><RouterLink to="/viajes">Buscar viajes</RouterLink></div>
      </div>
      <div class="footer-bottom">Sistema de Gestión y Venta de Pasajes Interprovinciales del Ecuador · Proyecto académico</div>
    </footer>
  </div>
</template>
