import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import HelloWorld from './components/HelloWorld.vue'
import Test from './components/Test.vue'



Vue.config.productionTip = false

Vue.use(VueRouter)


const router = new VueRouter({
  mode: 'history',
  routes: [{
    path: '/', component: HelloWorld 
  },{
    path:'/alignment', component: Test
  },{
    path:'/stats', component: Test
  },{
    path:'/skills', component: Test
  },{
    path:'/quests', component: Test
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
