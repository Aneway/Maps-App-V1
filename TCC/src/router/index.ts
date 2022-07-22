import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  {
    path: '',
    component: () => import('../views/LoginScreen.vue')
  },
  {
    path: '/home',
    component: () => import('../views/HomePage.vue')
  },
  {
    path: '/verify',
    component: () => import('../views/RegisterFindEDVScreen.vue')
  },
  {
    path: '/register',
    component: () => import('../views/RegisterScreen.vue')
  },
  {
    path: '/map',
    component: () => import('../views/MapPage.vue')
  },
  {
    path: '/information',
    component: () => import('../views/InformationScreen.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
