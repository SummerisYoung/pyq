import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import modal from '../src/plugins/modal/index';
import animate from 'animate.css'

Vue.use(modal)
Vue.prototype.axios = axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
