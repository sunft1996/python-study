# 协程学习
import asyncio


# Demo1: 获取协程返回的值
# async def add(x, y):
#     await asyncio.sleep(2)
#     result = x + y
#     return result


# if __name__ == "__main__": 
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(add(1,3))
#     loop.run_until_complete(task)
#     # 获取协程返回的值
#     print(task.result())
#     loop.close()

# Demo2: 多个协程的调用

async def add(x, y):
    await asyncio.sleep(2)
    result = x + y
    print('add done, result:', result)

async def sub(x, y):
    result = x - y
    print('sub done, result:', result)

if __name__ == "__main__": 
    loop = asyncio.get_event_loop()

    # 任务一：Task对象是包含执行状态的，也可以不创建Task，直接用loop.run_until_complete执行协程任务（即：add(1,3)），但外部拿不到任务状态
    task1 = loop.create_task(add(1,3))
    # 任务二
    task2 = loop.create_task(sub(100, 99))

    # 调用方式一：任务一个个执行，无法利用事件循环的优势：
    # run_until_complete是阻塞式的
    # loop.run_until_complete(task1)
    # loop.run_until_complete(task2)

    # 调用方式二：任务在事件循环中并发执行，阻塞即切换下一个
    # asyncio.wait会自动将协程任务包装成Task对象，并放入事件循环中
    loop.run_until_complete(asyncio.wait([add(1,3), sub(100, 99)]))

    loop.close()
