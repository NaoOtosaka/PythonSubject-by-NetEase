# coding=UTF-8

# 题目：
# 统计字符串 str 中每个单词出现的次数，结果存入 dict 中，单词为 key，次数为 value，
# 并按照 value 由高到底排序，输出此 dict。

# 引入正则库
import re


def strNum(input_str):
    """
    统计字符串中单词出现次数并排序
    :param string input_str:需检测的字符串
    :return:
    """
    # 初始化字典
    dict = {}

    # 正则过滤标点符号以及换行符
    input_str = re.sub(r"[,.*'!\n-]", "", input_str)

    # 以空格为分界符载入列表
    strList = input_str.split(" ")

    for value in strList:
        dict[value] = dict.get(value, 0) + 1    # 计数

    # 删除对空格的统计
    del dict[""]

    # 降序排序
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    # 遍历输出
    for key in dict:
        print key[0]+"共出现"+key[1].__str__()+"次"


if __name__ == '__main__':
    str = """The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""

    strNum(str)
