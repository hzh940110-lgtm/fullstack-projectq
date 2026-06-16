<template>
  <div class="items">
    <h2>商品管理</h2>

    <!-- 添加商品表单 -->
    <div class="add-form">
      <h3>添加商品</h3>
      <input v-model="newItem.title" placeholder="商品名称" />
      <input v-model="newItem.description" placeholder="商品描述" />
      <input v-model="newItem.price" type="number" placeholder="价格" />
      <input v-model="newItem.user_id" type="number" placeholder="用户ID" />
      <button @click="addItem">添加</button>
    </div>

    <!-- 商品列表 -->
    <div class="item-list">
      <h3>商品列表</h3>
      <div v-if="loading">加载中...</div>
      <div v-else-if="items.length === 0">暂无商品</div>
      <table v-else>
        <thead>
          <tr>
            <th>ID</th>
            <th>名称</th>
            <th>描述</th>
            <th>价格</th>
            <th>用户ID</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.title }}</td>
            <td>{{ item.description }}</td>
            <td>¥{{ item.price }}</td>
            <td>{{ item.user_id }}</td>
            <td>
              <button @click="deleteItem(item.id)" class="delete-btn">删除</button>
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
  name: 'Items',
  data() {
    return {
      items: [],
      loading: false,
      newItem: {
        title: '',
        description: '',
        price: 0,
        user_id: 1
      }
    }
  },
  mounted() {
    this.fetchItems()
  },
  methods: {
    async fetchItems() {
      this.loading = true
      try {
        this.items = await api.get('/items/')
      } catch (error) {
        alert('获取商品失败: ' + error.message)
      } finally {
        this.loading = false
      }
    },
    async addItem() {
      if (!this.newItem.title || !this.newItem.description) {
        alert('请填写完整信息')
        return
      }
      try {
        await api.post('/items/', this.newItem)
        this.newItem = { title: '', description: '', price: 0, user_id: 1 }
        this.fetchItems()
        alert('添加成功')
      } catch (error) {
        alert('添加失败: ' + error.message)
      }
    },
    async deleteItem(id) {
      if (!confirm('确定删除吗？')) return
      try {
        await api.delete(`/items/${id}`)
        this.fetchItems()
        alert('删除成功')
      } catch (error) {
        alert('删除失败: ' + error.message)
      }
    }
  }
}
</script>

<style scoped>
.items {
  max-width: 1000px;
  margin: 0 auto;
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

button:hover {
  background: #35a372;
}

.delete-btn {
  background: #e74c3c;
  padding: 5px 15px;
}

.delete-btn:hover {
  background: #c0392b;
}

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

th {
  background: #f5f5f5;
  font-weight: bold;
}

tr:hover {
  background: #f9f9f9;
}
</style>
