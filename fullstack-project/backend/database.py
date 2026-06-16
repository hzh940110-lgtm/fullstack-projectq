from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# MySQL 数据库配置 - 优先使用环境变量（Docker），否则用本地
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:123456@localhost:3306/fullstack_db")

# 创建数据库引擎
engine = create_engine(DATABASE_URL, echo=True)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#创建基类
Base = declarative_base()


#依赖注入函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()