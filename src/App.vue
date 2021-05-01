<template>
  <div id="app">
    <div id="nav-bar">
      <router-link to="/" exact><img alt="logo" class="logo" src="./assets/logo.png"></router-link>
      <router-link to="/alignment">alignment</router-link>
      <router-link to="/stats">stats</router-link>
      <router-link to="/skills">skills</router-link>
      <router-link to="/quests">quests</router-link>
      <router-link to="/inventory">inventory</router-link>
      <router-link to="/bestiary">bestiary</router-link>
      <router-link to="/codex">codex</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>
  body {
    margin: 0;
  }
  #nav-bar {
    width: 100vw;
    display: flex;
    justify-content: space-between;
    background-color: #1f1f1f;
  }

  .logo {
    max-height: 200px;
    max-width: 200px;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background-color: #1a1919e8;
    text-align: center;
    color: #e7e43b;
    min-height: 100vh;
    min-width: 100vw;
  }
</style>
