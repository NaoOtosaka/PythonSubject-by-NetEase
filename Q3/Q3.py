# coding=UTF-8

# 有 10 个游戏的初始账号，需要给这 10 个账号生成 10 个随机的密码，密码要求 8 位，只
# 能包含数字 0-9、小写字母 a-z 以及大写字母 A-Z，每个密码中没有重复的字符。
# 考察点：循环处理、字符串操作

# 引入随机数库
import random
# 引入字符库
import string


def password(length):
    """
    生成随机密码
    :param length:  密码长度
    :return:密码字典
    """
    # 初始化密码字典
    pwDict = {}
    # 拼接字符集列表
    strList = string.digits + string.ascii_letters

    for x in range(10):
        pwList = random.sample(strList, length)     # 不重复随机从字符集列表中取length个值
        pwStr = "".join(pwList)     # 转化为字符串
        pwDict[x] = pwStr       # 载入字典
        print "第"+(x+1).__str__()+"个账号的密码为："+pwStr

    return pwDict


if __name__ == '__main__':
    print password(8)
