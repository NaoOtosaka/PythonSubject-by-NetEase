# coding=utf-8

# 题目：
# 写一段代码，遍历输出 C:\Program Files (x86)目录下，这一层所有文件夹名称（仅限这一
# 层）
# PS：如果是 Linux 系统，则输出/home 目录下的所有文件夹名称；如果是 Mac 系统，则
# 输出/Users/xxx 目录下的所有文件夹名称（xxx 是你自己的用户名）；如果这些目录你都没
# 有，则随意选取一个非空目录进行输出。
# 考察点：文件夹操作

import platform
import os
import getpass


def searchDirectory():
    """
    根据不同系统遍历输出指定目录下文件夹
    :return:
    """
    # 初始化路径及OS名称
    path = ''
    OSName = platform.system()

    # 根据不同系统拼接路径
    if OSName == 'Windows':
        path = 'C:\Program Files (x86)'
    elif OSName == 'Linux':
        path = '/home'
    elif OSName == 'Darwin':
        path = '/Users/' + getpass.getuser()    # 获取用户名

    # 遍历输出
    for value in os.listdir(path):
        print value


if __name__ == '__main__':
    searchDirectory()
