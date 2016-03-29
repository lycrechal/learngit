#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a socket example which send echo message to server.'

import socket
from twisted.internet import task
from twisted.internet import reactor
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
#print s.recv(1024)
def printtime():
    s.send(time.strftime("%H:%M:%S"))
    print s.recv(1024)
t=task.LoopingCall(printtime)
t.start(5.0)
reactor.run()
#for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    #s.send(data)
    #print s.recv(1024)
s.send('exit')
s.close()
