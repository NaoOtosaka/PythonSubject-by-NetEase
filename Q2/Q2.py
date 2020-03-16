# coding=UTF-8

# 题目:
# 获取当前的系统时间，写入到指定的文件 time.txt 中，时间格式为 year-month-day
# hh:mm:ss，如 2019-11-27 21:40:02

# 引入时间库
import time


def RecordingTime():
    """
    获取当前时间并写入time.txt文件中
    :return:
    """
    # 本地时间获取
    localtime = time.localtime(time.time())

    # 格式化时间戳
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", localtime)

    # 以附加模式打开time.txt，若不存在则创建
    fileObj = open("time.txt", "a+")

    # 写入并反馈
    fileObj.write(timeStr + "\n")
    print "写入成功"

    # 关闭文件资源
    fileObj.close()


if __name__ == '__main__':
    RecordingTime()
