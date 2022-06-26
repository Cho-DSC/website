import Home from './views/Home.vue'
import About from './views/About.vue'
import Lotto from './views/Lotto.vue'
import NotFound from './views/NotFound.vue'
import { createWebHistory, createRouter } from "vue-router"

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
        path: '/lotto',
        component: Lotto,
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
    
