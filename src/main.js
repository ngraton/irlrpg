import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import HelloWorld from './components/HelloWorld.vue'
import Test from './components/Test.vue'
import Stats from './components/Stats.vue'
import Alignment from './components/Alignment.vue'


Vue.config.productionTip = false

Vue.use(VueRouter)


const router = new VueRouter({
  mode: 'history',
  routes: [{
    path: '/', component: HelloWorld 
  },{
    path:'/alignment', component: Alignment
  },{
    path:'/stats', component: Stats
  },{
    path:'/skills', component: Test
  },{
    path:'/quests', component: Test
  },{
    path:'/allies', component: Test
  },{
    path:'/inventory', component: Test
  },{
    path:'/bestiary', component: Test
  },{
    path:'/codex', component: Test
  }]
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
