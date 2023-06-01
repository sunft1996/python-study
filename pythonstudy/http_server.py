from aiohttp import web

async def handle(request):
    return web.Response(text='Hello, World!')

async def run_server():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    # 创建应用程序运行器
    runner = web.AppRunner(app)
    # 初始化
    await runner.setup()
    # 运行器绑定8080端口
    site = web.TCPSite(runner, 'localhost', 8080)
    print('Server running at http://localhost:8080')
    # 启动
    await site.start()

if __name__ == '__main__':
    # import可以放在条件中执行
    import asyncio
    loop = asyncio.get_event_loop()
    # 协程放入事件循环中执行
    loop.run_until_complete(run_server())
    # 维持事件循环的执行
    loop.run_forever()