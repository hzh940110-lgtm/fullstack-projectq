# 全栈项目 - Vue + FastAPI + MySQL + Redis

一个简单的全栈项目，演示前后端如何与数据库交互。

## 项目结构

```
fullstack-project/
├── backend/                # 后端 FastAPI
│   ├── main.py            # 主入口
│   ├── database.py        # MySQL 配置
│   ├── redis_client.py    # Redis 配置
│   ├── models.py          # 数据模型
│   ├── routers/           # 接口路由
│   │   ├── user.py        # 用户接口
│   │   └── item.py        # 商品接口
│   └── requirements.txt   # Python 依赖
│
└── frontend/              # 前端 Vue
    ├── src/
    │   ├── views/         # 页面
    │   ├── App.vue        # 主组件
    │   ├── api.js         # API 配置
    │   └── router.js      # 路由配置
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## 快速开始

### 1. 准备数据库

在 Navicat 或终端创建数据库：

```sql
CREATE DATABASE fullstack_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

### 2. 启动 Redis

```bash
redis-server
```

### 3. 后端启动

```bash
# 进入后端目录
cd fullstack-project/backend

# 安装依赖
pip install -r requirements.txt

# 修改 database.py 的密码（第6行）
# DATABASE_URL = "mysql+pymysql://root:你的密码@localhost:3306/fullstack_db"

# 启动后端
fastapi dev main.py --host 0.0.0.0
```

后端地址：`http://localhost:8000`
接口文档：`http://localhost:8000/docs`

### 4. 前端启动

```bash
# 新开一个终端，进入前端目录
cd fullstack-project/frontend

# 安装依赖
npm install

# 启动前端
npm run dev
```

前端地址：`http://localhost:5173`

## 功能演示

### 用户管理
- 添加用户（数据存入 MySQL）
- 查看用户列表（使用 Redis 缓存）
- 删除用户

### 商品管理
- 添加商品（数据存入 MySQL）
- 查看商品列表
- 删除商品

## 数据流程

```
用户在浏览器操作
    ↓
Vue 前端 (http://localhost:5173)
    ↓ 调用 API
FastAPI 后端 (http://localhost:8000/api)
    ↓ 存取数据
MySQL 数据库 (数据持久化)
Redis 缓存 (加速查询)
```

## 接口列表

### 用户接口
- `GET /api/users/` - 获取所有用户
- `GET /api/users/{id}` - 获取单个用户
- `POST /api/users/` - 创建用户
- `DELETE /api/users/{id}` - 删除用户

### 商品接口
- `GET /api/items/` - 获取所有商品
- `GET /api/items/{id}` - 获取单个商品
- `POST /api/items/` - 创建商品
- `PUT /api/items/{id}` - 更新商品
- `DELETE /api/items/{id}` - 删除商品

## 技术栈

**后端**
- FastAPI - Web 框架
- SQLAlchemy - ORM
- PyMySQL - MySQL 驱动
- Redis - 缓存

**前端**
- Vue 3 - 前端框架
- Vue Router - 路由
- Axios - HTTP 客户端
- Vite - 构建工具

## 常见问题

### 1. 后端启动失败
- 检查 MySQL 是否启动
- 检查 `database.py` 的密码是否正确
- 检查数据库 `fullstack_db` 是否创建

### 2. 前端无法访问后端
- 检查后端是否用 `--host 0.0.0.0` 启动
- 检查 CORS 配置（已在 `main.py` 配置好）

### 3. Redis 相关错误
- 确保 Redis 已启动
- 如果不想用 Redis，可以注释掉 `user.py` 里的缓存代码
