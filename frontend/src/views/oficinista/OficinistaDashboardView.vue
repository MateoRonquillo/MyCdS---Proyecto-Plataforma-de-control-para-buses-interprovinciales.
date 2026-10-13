<script setup>
import { ref } from 'vue'
import AdminSidebar from '../../components/admin/AdminSidebar.vue'

const tareasOficina = ref([
  {
    id: 'M06',
    titulo: 'Revisión de Comprobantes y Pagos',
    descripcion: 'Validación de transferencias, depósitos y aprobación/rechazo de pagos pendientes.'
  },
  {
    id: 'M08-A',
    titulo: 'Gestión de Reservas',
    descripcion: 'Consulta de reservas en estado PENDIENTE, PAGO_EN_REVISION y CONFIRMADA.'
  },
  {
    id: 'M08-B',
    titulo: 'Venta Presencial en Ventanilla',
    descripcion: 'Registro directo de pasajeros, asignación de asientos y emisión de boletos con QR.'
  }
])
</script>

<template>
  <div class="oficina-layout">
    <AdminSidebar rol="OFICINISTA" />

    <main class="oficina-main">
      <header class="oficina-header">
        <div>
          <h1>Panel de Oficinista</h1>
          <p class="subtitle">Control de Reservas, Aprobación de Pagos y Ventas Presenciales</p>
        </div>
        <span class="badge-oficina">Rol: Oficinista</span>
      </header>

      <section class="oficina-grid">
        <article v-for="tarea in tareasOficina" :key="tarea.id" class="oficina-card">
          <span class="task-tag">{{ tarea.id }}</span>
          <h2>{{ tarea.titulo }}</h2>
          <p>{{ tarea.descripcion }}</p>
        </article>
      </section>
    </main>
  </div>
</template>

<style scoped>
.oficina-layout {
  display: flex;
  min-height: 100vh;
  background-color: #f8fafc;
  font-family: system-ui, -apple-system, sans-serif;
}
.oficina-main {
  flex: 1;
  padding: 2rem;
}
.oficina-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e2e8f0;
}
.subtitle {
  color: #64748b;
  margin-top: 0.25rem;
}
.badge-oficina {
  background-color: #0f766e;
  color: #ffffff;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
}
.oficina-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}
.oficina-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 1.5rem;
}
.task-tag {
  font-weight: 700;
  color: #0f766e;
  font-size: 0.85rem;
}
</style>