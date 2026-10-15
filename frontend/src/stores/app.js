import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    nombre: 'Pasajes EC',
  }),
})
