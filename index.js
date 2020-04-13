import Vue from 'vue';
import VueRouter from 'vue-router';

import Policies from '../components/Policies.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/policies',
    name: 'Policies',
    component: Policies,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
