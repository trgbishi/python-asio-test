import asyncio
import aiohttp
import sys
sys.path.append('C:\\Users\\kdgz\\Desktop\\collector')
class Data_Up:
    async def chat_recv(self,ws,url):
        while True:
            await asyncio.sleep(1)
            print('recving...')
            try:
                #有异常就直接进入异常处理，断开重连
                echo = await ws.receive()
            except (aiohttp.client_exceptions.ClientOSError,aiohttp.client_exceptions.ServerDisconnectedError) as e:
                ws.close()
                ws = await aiohttp.ClientSession().ws_connect(url)
            if echo is None:
                #连接中断，但是不报异常的时候，就会不断'收到'空值，这时定时发送 '心跳',重连上后，server会应答
                try:
                    ws.close()
                    ws = await aiohttp.ClientSession().ws_connect(url)
                except aiohttp.client_exceptions.ClientConnectorError as e:
                    print(e)
                continue
            else :
                tmp_dict = eval(echo)
                for k,v in tmp_dict.items():
                    print(k + ' ' + str(v))
                return tmp_dict

    async def chat_send(self,ws,msg):
        await ws.send_str(msg)
        print('send success??')

    async def chat(self,url,msg):
        print('0')
        while True:
            print('01')
            try:
                print('02')
                session = aiohttp.ClientSession()
                print('022')
                ws = await session.ws_connect(url)
                print('03')
                # break
            except aiohttp.client_exceptions.ClientConnectorError as e:
                print(e)
                continue
        print('1')
        tasks = [self.chat_recv(ws,url), self.chat_send(ws,msg)]
        print('2')
        await asyncio.wait(tasks)
        print('3')