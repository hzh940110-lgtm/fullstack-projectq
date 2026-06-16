<template>
  <div id="app">
    <header>
      <h1>全栈项目</h1>
      <nav>
        <router-link to="/">首页</router-link> |
        <router-link to="/users">用户管理</router-link> |
        <router-link to="/items">商品管理</router-link>
      </nav>
    </header>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background: #f5f5f5;
}

#app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  background: white;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
  margin-bottom: 15px;
  color: #333;
}

nav a {
  color: #42b983;
  text-decoration: none;
  padding: 0 10px;
}

nav a.router-link-active {
  font-weight: bold;
}

main {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
