import asyncio
import sys
import aiohttp
import ujson
sys.path.append('C:\\Users\\kdgz\\Desktop\\collector')
from comm.asio.http.http_client import Http_Client
class Data_Up:
    async def post_req(self,socket,msg):
        while True:
            await asyncio.sleep(1)
            try:
                #有异常就直接进入异常处理，断开重连
                echo = await socket.do_post(msg)
            except (aiohttp.client_exceptions.ClientOSError,aiohttp.client_exceptions.ServerDisconnectedError) as e:
                socket.close()
                session = aiohttp.ClientSession()
                socket = Http_Client(session,self.__url) 
                
                print(str(e))
                continue
            if echo is None:
                #连接中断，但是不报异常的时候，就会不断'收到'空值，这时定时发送 'heartbeat/reconnecting',重连上后，server会应答
                try :
                    socket.close()
                    session = aiohttp.ClientSession()
                    #TODO:发送重连request请求，收到正确回复则表示连接重新建立.当前不实现，了解一下
                except aiohttp.client_exceptions.ClientConnectorError as e:
                    print(e)
                continue
            else :
                tmp_dict = eval(echo)
                for k,v in tmp_dict.items():
                    print(k + ' ' + str(v))
                return tmp_dict
                #当消息发送成功，并成功解析，退出true循环,并退出函数。这样每次进入该函数，顺利的话，只会发送一次req，并解析resp
                #具体看业务逻辑

    async def chat_send(self,socket,msg):
        await self.post_req(socket,msg)

    #长轮询，获取server发的request
    async def chat_recv(self,socket,):
        while True:
            resp = await self.post_req(socket,'{"test":"getRequest"}')
            print('recv: ' + str(resp))
    


    async def chat(self,url,msg,loop):
        session = aiohttp.ClientSession()
        #http连接是基于session，而不是基于ip\port,所以这里并不是进行连接，自然没有重连的需求
        self.__url = url
        client = Http_Client(session,self.__url)
        tasks = [self.chat_recv(client), self.chat_send(client,msg)]
        await asyncio.wait(tasks)