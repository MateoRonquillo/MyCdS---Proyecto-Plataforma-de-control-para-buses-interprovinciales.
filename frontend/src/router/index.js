import { createRouter, createWebHistory } from 'vue-router'
import PublicLayout from '../components/cliente/PublicLayout.vue'
import adminRoutes from './admin.routes.js'

const routes = [
  {
    path: '/',
    component: PublicLayout,
    children: [
      {
        path: '',
        name: 'inicio',
        component: () => import('../views/cliente/InicioView.vue'),
      },
      {
        path: 'viajes',
        name: 'viajes',
        component: () => import('../views/cliente/ViajesView.vue'),
      },
    ],
  },
  ...adminRoutes,
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
