import os
from redis import Redis
from throttled.fastapi import IPLimiter, TotalLimiter
from throttled.models import Rate
from throttled.storage.memory import MemoryStorage
from throttled.storage.redis import RedisStorage
from dotenv import load_dotenv

load_dotenv()

memory_storage = MemoryStorage()
redis_storage = RedisStorage(client=Redis.from_url(os.getenv("RedisHost")))

total_limiter = TotalLimiter(limit=Rate(100, 60), storage=memory_storage)
ip_limiter=IPLimiter(limit=Rate(10, 60), storage=redis_storage)
