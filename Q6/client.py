# coding=UTF-8

# 题目：
# 实现一个 tcp 的 client 和 server，client 给 server 发送随机的字符串内容，server 收到后
# 都将其倒序返回给 client，当客户端输入'over'（不区分大小写），则客户端结束发送，程序
# 退出；如：client 发送'12345'，server 返回'54321'
# 考察点：socket 编程

import socket


def client():
    # 地址、端口设定
    host = ('127.0.0.1', 9999)

    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 建立连接
    s.connect(host)

    print s.recv(1024)  # 打印server连接响应

    while True:
        data = raw_input()  # 输入字符串
        s.send(data)    # 发送数据
        if data == 'over':  # 发送over时跳出循环
            break
        print s.recv(1024)  # 打印server响应

    s.close()   # 关闭连接
    print '链接已关闭'


if __name__ == '__main__':
    client()