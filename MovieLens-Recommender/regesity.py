import asyncio
 
from wasp_eureka import EurekaClient
 
 
app_name = "recommend-service"    # 自定义
 
ip = "127.0.0.1"    # 本机IP
my_eureka_url = "http:localhost:8761"    # eureka服务所在IP及密码端口号
loop = asyncio.get_event_loop()  # 创建事件循环
# 创建eureka客户端 port为flask app指定的运行端口
eureka = EurekaClient(app_name=app_name, port=5000, ip_addr=ip, eureka_url=my_eureka_url, loop=loop)
 
async def main():
    result = await eureka.register()
    print("[Register Rureka] result: %s" % result)
 
    while True:
        await asyncio.sleep(60)
        await eureka.renew()
 
 
if __name__ == "__main__":
    loop.run_until_complete(main())