import asyncio
import sys
sys.path.append('C:\\Users\\kdgz\\Desktop\\collector')
from comm.asio.tcp.tcp_data_up import Data_Up
from comm.asio.protocol.json_data import Json_Data
from comm.asio.protocol.mon_data import MON_DATA
if __name__ == "__main__":
    # lock ip/port
    # ip = '192.168.106.51'
    # port = 10080

    # #my op/port
    ip = '127.0.0.1'
    port = 12345


    #封装mon_data
    msg = Json_Data((MON_DATA(1,'1.1.1.1','metric','tags','2018-07-26',5.5,5).dict())).json()
    print(msg)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Data_Up().chat(ip,port,loop,msg))
    loop.close()




