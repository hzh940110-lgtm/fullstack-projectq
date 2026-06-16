import redis

# Redis 配置
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
    db=0
)


def get_redis():
    """获取 Redis 客户端"""
    return redis_client


def set_cache(key: str, value: str, expire: int = 300):
    """设置缓存，默认过期时间300秒"""
    redis_client.setex(key, expire, value)


def get_cache(key: str):
    """获取缓存"""
    return redis_client.get(key)


def delete_cache(key: str):
    """删除缓存"""
    redis_client.delete(key)
