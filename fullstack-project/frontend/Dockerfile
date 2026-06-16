# Node.js 基础镜像
FROM node:18-alpine as build

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY package.json .

# 安装依赖
RUN npm install

# 复制前端代码
COPY . .

# 构建生产版本
RUN npm run build

# 使用 nginx 提供静态文件
FROM nginx:alpine

# 复制构建结果到 nginx
COPY --from=build /app/dist /usr/share/nginx/html

# 复制 nginx 配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 暴露端口
EXPOSE 80

# 启动 nginx
CMD ["nginx", "-g", "daemon off;"]