import asyncio
import sys
sys.path.append('C:\\Users\\kdgz\\Desktop\\collector')
from comm.asio.tcp.tcp_client import Tcp_Client
class Data_Up:
    async def chat_recv(self,socket,loop,ip,port):
        while True:
            try:
                #有异常就直接进入异常处理，断开重连
                echo = await socket.recv()
            except (ConnectionResetError,ConnectionAbortedError) as e:
                try:
                    socket.close()
                    reader, writer = await asyncio.open_connection(ip,port, loop=loop)
                    socket = Tcp_Client(reader,writer)
                except ConnectionRefusedError:
                    continue
                print('errrrrrrrrrrrr'+str(e))
            if echo is '':
                #连接中断，但是不报异常的时候，就会不断'收到'空值，这时定时发送 '心跳',重连上后，server会应答
                await asyncio.sleep(1)
                await socket.send('conecting')
                continue
            else :
                print ("rcv: "+echo)
                await socket.send(echo)
    async def chat_send(self,socket,msg):
        await socket.send(msg)

    async def chat(self,ip,port,loop,msg):
        while True:
            print('a')
            try:
                print('b')
                reader, writer = await asyncio.open_connection(ip, port, loop=loop)
                print('c')
                break
            except ConnectionRefusedError:
                print('d')
                continue
        client = Tcp_Client(reader, writer)
        tasks = [self.chat_recv(client,loop,ip,port), self.chat_send(client,msg)]
        await asyncio.wait(tasks)