<template>
  <div class="users">
    <h2>用户管理</h2>

    <!-- 搜索框 -->
    <div class="search-bar">
      <input v-model="keyword" placeholder="搜索用户名或邮箱" @input="searchUsers" />
      <button @click="searchUsers">搜索</button>
      <button @click="clearSearch" class="cancel-btn">清空</button>
    </div>
    <div class="add-form">
      <h3>添加用户</h3>
      <input v-model="newUser.username" placeholder="用户名" />
      <input v-model="newUser.email" placeholder="邮箱" />
      <input v-model="newUser.password" type="password" placeholder="密码" />
      <button @click="addUser">添加</button>
    </div>

    <!-- 编辑弹窗 -->
    <div v-if="editingUser" class="modal-overlay">
      <div class="modal">
        <h3>编辑用户</h3>
        <input v-model="editingUser.username" placeholder="用户名" />
        <input v-model="editingUser.email" placeholder="邮箱" />
        <div class="modal-btns">
          <button @click="saveEdit">保存</button>
          <button @click="editingUser = null" class="cancel-btn">取消</button>
        </div>
      </div>
    </div>

    <!-- 用户列表 -->
    <div class="user-list">
      <h3>用户列表</h3>
      <div v-if="loading">加载中...</div>
      <div v-else-if="users.length === 0">暂无用户</div>
      <table v-else>
        <thead>
          <tr>
            <th>ID</th>
            <th>用户名</th>
            <th>邮箱</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>
              <button @click="startEdit(user)" class="edit-btn">编辑</button>
              <button @click="deleteUser(user.id)" class="delete-btn">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import api from '../api'

export default {
  name: 'Users',
  data() {
    return {
      users: [],
      loading: false,
      keyword: '',
      newUser: { username: '', email: '', password: '' },
      editingUser: null
    }
  },
  mounted() {
    this.fetchUsers()
  },
  methods: {
    async fetchUsers() {
      this.loading = true
      try {
        this.users = await api.get('/users/', { params: { keyword: this.keyword } })
      } catch (error) {
        alert('获取用户失败: ' + error.message)
      } finally {
        this.loading = false
      }
    },
    async searchUsers() {
      this.fetchUsers()
    },
    clearSearch() {
      this.keyword = ''
      this.fetchUsers()
    },
    async addUser() {
      if (!this.newUser.username || !this.newUser.email || !this.newUser.password) {
        alert('请填写完整信息')
        return
      }
      const emailReg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!emailReg.test(this.newUser.email)) {
        alert('邮箱格式不正确，例如：example@qq.com')
        return
      }
      try {
        await api.post('/users/', this.newUser)
        this.newUser = { username: '', email: '', password: '' }
        this.fetchUsers()
        alert('添加成功')
      } catch (error) {
        alert('添加失败: ' + error.message)
      }
    },
    startEdit(user) {
      this.editingUser = { ...user }
    },
    async saveEdit() {
      try {
        await api.put(`/users/${this.editingUser.id}`, {
          username: this.editingUser.username,
          email: this.editingUser.email
        })
        this.editingUser = null
        this.fetchUsers()
        alert('修改成功')
      } catch (error) {
        alert('修改失败: ' + error.message)
      }
    },
    async deleteUser(id) {
      if (!confirm('确定删除吗？')) return
      try {
        await api.delete(`/users/${id}`)
        this.fetchUsers()
        alert('删除成功')
      } catch (error) {
        alert('删除失败: ' + error.message)
      }
    }
  }
}
</script>

<style scoped>
.users {
  max-width: 800px;
  margin: 0 auto;
}

.search-bar {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
  align-items: center;
}

.search-bar input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 250px;
}

.add-form {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.add-form h3 {
  margin-bottom: 15px;
}

.add-form input {
  padding: 10px;
  margin-right: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 150px;
}

button {
  padding: 10px 20px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover { background: #35a372; }

.edit-btn {
  background: #3498db;
  padding: 5px 15px;
  margin-right: 5px;
}

.edit-btn:hover { background: #2980b9; }

.delete-btn {
  background: #e74c3c;
  padding: 5px 15px;
}

.delete-btn:hover { background: #c0392b; }

.cancel-btn {
  background: #999;
  margin-left: 10px;
}

.cancel-btn:hover { background: #777; }

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th { background: #f5f5f5; font-weight: bold; }
tr:hover { background: #f9f9f9; }

.modal-overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
}

.modal {
  background: white;
  padding: 30px;
  border-radius: 8px;
  min-width: 350px;
}

.modal h3 { margin-bottom: 15px; }

.modal input {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.modal-btns { display: flex; justify-content: flex-end; }
</style>
