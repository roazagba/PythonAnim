import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Developpeur from '@/views/Developpeur.vue'
import Contact from '@/views/Contact.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {title: 'Accueil'}
  },
  {
    path: '/excution/code',
    name: 'programmer',
    component: Developpeur,
    meta: {title: 'Animation d\'algorithme'}
  },
  {
    path: '/contact',
    name: 'contact',
    component: Contact,
    meta: {title: 'Contact'}
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title+' | '+import.meta.env.VITE_APP_NAME
  next()
})

export default router
