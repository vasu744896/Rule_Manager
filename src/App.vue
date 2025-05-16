<template>
  <div id="app">
    <RuleManager />
  </div>
</template>

<script>
import RuleManager from './components/RuleManager.vue';

export default {
  name: "App",
  components: { RuleManager }
};
</script>

<style>
html, body, #app {
  margin: 0;
  height: 100%;
  background-color: #e8ecf7;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
