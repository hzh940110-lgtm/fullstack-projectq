<template>
  <div class="home">
    <h2>欢迎使用全栈项目</h2>
    <p>这是一个 Vue + FastAPI + MySQL 的示例项目</p>
    <div class="features">
      <div class="feature-card">
        <h3>📝 用户管理</h3>
        <p>增删改查用户信息</p>
        <router-link to="/users">前往 →</router-link>
      </div>
      <div class="feature-card">
        <h3>🛒 商品管理</h3>
        <p>管理商品信息</p>
        <router-link to="/items">前往 →</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.home {
  text-align: center;
}

h2 {
  color: #42b983;
  margin-bottom: 10px;
}

.features {
  display: flex;
  gap: 20px;
  margin-top: 40px;
  justify-content: center;
}

.feature-card {
  background: #f9f9f9;
  padding: 30px;
  border-radius: 8px;
  width: 250px;
  transition: transform 0.3s;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-card h3 {
  margin-bottom: 10px;
}

.feature-card a {
  display: inline-block;
  margin-top: 15px;
  color: #42b983;
  text-decoration: none;
  font-weight: bold;
}
</style>
