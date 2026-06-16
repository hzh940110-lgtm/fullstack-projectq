# Docker 部署指南

## 一键启动

在项目根目录 `fullstack-project/` 下执行：

```bash
docker-compose up -d
```

等待几分钟，所有服务启动后，访问 `http://localhost` 就能看到项目。

## 服务说明

| 服务 | 地址 | 说明 |
|------|------|------|
| 前端 | http://localhost | Vue 应用 |
| 后端 | http://localhost:8000 | FastAPI 接口 |
| 接口文档 | http://localhost:8000/docs | Swagger 文档 |
| MySQL | localhost:3306 | 数据库（账号 root / root123） |
| Redis | localhost:6379 | 缓存 |

## 常用命令

```bash
# 启动所有服务
docker-compose up -d

# 查看运行状态
docker-compose ps

# 查看日志
docker-compose logs -f

# 停止所有服务
docker-compose down

# 停止并删除数据
docker-compose down -v
```

## 修改代码后重新构建

```bash
# 后端改了代码
docker-compose up -d --build backend

# 前端改了代码
docker-compose up -d --build frontend

# 全部重新构建
docker-compose up -d --build
```

## 本地开发 vs Docker 部署

### 本地开发（不用 Docker）

```bash
# 后端
cd backend
venv\Scripts\activate
fastapi dev main.py --host 0.0.0.0

# 前端
cd frontend
npm run dev
```

前端：http://localhost:5173  
后端：http://localhost:8000

### Docker 部署

```bash
docker-compose up -d
```

前端：http://localhost  
后端：http://localhost:8000

数据库、Redis 都自动启动，不需要本机安装。

## 注意事项

1. **首次启动**需要等 MySQL 初始化完成（约 30 秒），后端才能连接
2. **数据持久化**：MySQL 数据存在 Docker 卷里，`docker-compose down` 不会删除数据，除非加 `-v` 参数
3. **端口占用**：确保 80、3306、6379、8000 端口没被占用

## 部署到服务器

把项目上传到服务器后，执行：

```bash
docker-compose up -d
```

就能在服务器上运行了。
