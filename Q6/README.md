实现一个 tcp 的 client 和 server，client 给 server 发送随机的字符串内容，server 收到后 都将其倒序返回给 client，当客户端输入'over'（不区分大小写），则客户端结束发送，程序 退出；

如：client 发送'12345'，server 返回'54321' 

考察点：socket 编程

