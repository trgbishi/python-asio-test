#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
同步模型，做server 回复client的消息用
'''
from socket import *
import time

host = ''
port = 12345
buffsize = 2048
ADDR = (host,port)

tctime = socket(AF_INET,SOCK_STREAM)
tctime.bind(ADDR)
tctime.listen(3)

while True:
    print('Wait for connection ...')
    tctimeClient,addr = tctime.accept()
    print("Connection from :",addr)

    while True:
        data = tctimeClient.recv(buffsize).decode()
        if not data:
            break
        print(data)
        time.sleep(1)
        tctimeClient.send(data.encode())
    tctimeClient.close()
tctimeClient.close()