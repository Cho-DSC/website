<template>
  <div class="tasks_container">
        <div class="tasks_content">
            <h1>Tasks</h1>
            <ul class="tasks_list">
                <li v-for="task in tasks">
                    <h2>{{ task.drwNo }} 회차</h2>
                    <p>{{ task.firstAccumamnt }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LottoPage',
    data() {
        return {
            tasks: []
        }
    },
    mounted() {
        this.get_Tasks();
    },
    methods: {
        get_Tasks() {
            axios({
                method: 'get',
                url: 'http://3.36.100.124:8000/lotto/num/',
            }).then(response => this.tasks = response.data);
        }
    }
}
</script>