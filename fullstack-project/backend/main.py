from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user, item
from database import engine
import models

app = FastAPI(title="全栈项目API", version="1.0.0")

# 配置CORS，必须在路由注册之前
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 开发环境允许所有来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(user.router, prefix="/api/users", tags=["用户管理"])
app.include_router(item.router, prefix="/api/items", tags=["商品管理"])

# 创建数据库表
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "欢迎使用全栈项目API", "docs": "/docs"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
