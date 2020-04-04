# coding=UTF-8

import socket
import time


def tcp_link(sock, addr):
    sock.send('Welcome!')   # 发送连接响应
    while True:
        data = sock.recv(1024)      # 接收tcp数据
        time.sleep(1)
        if data == 'over':  # 接收over时跳出循环
            break
        print '来自%s:%s的源数据：%s 返回：%s' % (addr[0], addr[1], data, data[::-1])
        sock.send(data[::-1])   # 发送接收数据的反转
    sock.close()    # 关闭连接
    print "%s:%s 链接已关闭" % addr


def main():
    # 地址、端口设定
    host = ('127.0.0.1', 9999)

    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址
    s.bind(host)

    # 设置监听数量
    s.listen(1)

    print '等待连接...'

    # 循环等待客户端链接
    while True:
        sock, addr = s.accept()  # 接受并返回连接
        print "链接自%s:%s" % (addr[0], addr[1])   # 打印客户端地址
        tcp_link(sock, addr)    # 处理tcp连接


if __name__ == '__main__':
    main()

