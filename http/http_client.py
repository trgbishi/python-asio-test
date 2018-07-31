import aiohttp
import asyncio
import ujson
class Http_Client:
    def __init__(self,session,url):
        self.session = session
        self.url = url

    #没有用上get
    async def do_get(self):
        print('do_get...')


    async def do_post(self,msg):
        print('send:' + str(msg))
        # print(len(msg))
        resp = await self.session.post(self.url, data = str(msg))#用json = msg传json格式，会给"加转义字符成\"，从而与content-length不符，server无法解析
        recv = await resp.text()
        print('recv: ' + recv)
        return recv


    async def close(self):
        await self.session.close()
        print('client closed')


