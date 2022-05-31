import Home from './views/Home.vue'
import About from './views/About.vue'
import NotFound from './views/NotFound.vue'
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
    {
        path: '/:catchAll(.*)',
        component: NotFound
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
    
