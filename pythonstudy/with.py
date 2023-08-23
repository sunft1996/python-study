"""Demo1: 打开文件传统操作"""

f = open('file.txt', 'r')
try:
    data = f.read()
    # 对读取到的数据进行处理
finally:
    # 手动关闭
    # 释放文件资源
    f.close()


"""Demo2: 使用with"""

with open('file.txt', 'r') as f:
    data = f.read()
    # 对读取到的数据进行处理
# 文件 f 在 with 语句块结束后自动关闭

# 语法：with 上下文管理器对象 as resource:
# 功能：with会自动调用 【上下文管理器对象】 的__enter__() 和 __exit__() 方法，从而完成所有预处理和后处理的工作
# open()返回文件对象，但是文件对象实现了上下文管理器协议，因此可以用with来管理
# 好处：使用 with 语句的好处是可以避免代码中忘记释放资源造成的内存泄漏

"""
    Demo3: 使用async with实现异步资源的自动释放
    写一个class，实现异步上下文管理器协议
"""

import aioredis
import asyncio

class RedisPool:
    # 实现异步上下文管理器的__aenter__方法
    # __aenter__返回资源
    async def __aenter__(self):
        self.pool = await aioredis.create_pool('redis://localhost')
        return self.pool

    # __aexit__释放资源
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.pool.close()
        await self.pool.wait_closed()

async def main():
    async with RedisPool() as redis:
        # 使用 Redis 连接池进行操作
        await redis.set('key', 'value')
        result = await redis.get('key')
        print(result)

asyncio.run(main())

