import Home from './views/Home.vue'
import About from './views/About.vue'
import { createWebHistory, createRouter } from "vue-router"
import Vue from 'vue'

const routes = [
    {
    path: '/',
    component: Home
    },
    {
    path: '/about',
    component: About
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
    
