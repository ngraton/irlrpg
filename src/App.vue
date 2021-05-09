<template>
  <div id="app">
    <div id="nav-bar">
      <router-link to="/" exact><img alt="logo" class="logo" src="./assets/logo.png"></router-link>
      <div class="nav-box">
        <div class="nav-links">
          <router-link class="nav-link" to="/alignment">alignment</router-link>
          <router-link class="nav-link" to="/stats">stats</router-link>
          <router-link class="nav-link" to="/skills">skills</router-link>
          <router-link class="nav-link" to="/quests">quests</router-link>
        </div>
        <div class="nav-links">
          <router-link class="nav-link" to="/allies">allies</router-link>
          <router-link class="nav-link" to="/inventory">inventory</router-link>
          <router-link class="nav-link" to="/bestiary">bestiary</router-link>
          <router-link class="nav-link" to="/codex">codex</router-link>
        </div>
      </div>
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

  .nav-box {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }

  .nav-links {
    display: flex;
    flex-grow: 1;
    padding: 0 32px;
    justify-content: space-between;
  }

  .nav-link {
    align-self: center;
    font-size: 32px;
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
