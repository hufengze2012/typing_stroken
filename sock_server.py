# -*- coding:utf-8 -*-
import socket
if __name__ == '__mian__':
    print '~~~'
    sock = socket.socket(socket.AF_INFET,socket.SOCK_SOCK_STREAM)
    sock.bind(('localhos',8001))
    sock.liseten(10)
    while True:
        connection,address = sock.accept()
        try:
            connection.settmeout(5)
            buf = connection.recv(1024)
            if buf == '1':
                connection.send('welcome to server!')
            else:
                connection.send('please go out!')
        except socket.timeout:
            print 'time out'
        connection.close()
