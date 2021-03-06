import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'


const app = createApp(App).use(router).mount('#app')
app.config.globalProperties.$axios = axios;
app.mount('#app')
