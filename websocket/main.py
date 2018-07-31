import aiohttp
import asyncio
import sys
sys.path.append('C:\\Users\\kdgz\\Desktop\\collector')
from comm.asio.websocket.ws_data_up import Data_Up
from comm.asio.protocol.json_data import Json_Data
from comm.asio.protocol.mon_data import MON_DATA

if __name__ == '__main__':
    # url = 'http://127.0.0.1:12345'
    url = 'http://192.168.106.51:10080'
    # url = 'http://192.168.106.49:12345'
    msg = Json_Data((MON_DATA(1,'1.1.1.1','metric','tags','2018-07-26',5.5,5).__list__())).__json__()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(Data_Up().chat(url,msg))
    loop.close()
