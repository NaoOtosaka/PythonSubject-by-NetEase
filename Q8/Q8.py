# coding=utf-8

# 题目
# 将附件 csv 中的内容，写入到 json 中，csv 中的 ID 列为 key，其他列为 value。
# csv 数据见 Q8.csv，json 数据示例见 Q8_example.json（缩进无需关注，保证结果正确即可）。
# 考察点：csv、json 文件的处理

import csv
import json
import collections


def csvIntoJson(csvPath):
    """
    csv文件写入json
    :param csvPath: csv文件路径
    :return:
    """
    # 声明有序字典
    dict = collections.OrderedDict()

    # 定义除key外列标签元组
    keyList = ('RaceID', 'ModelID', 'IconID', 'Name', 'Description', 'ColorationID')

    # 打开csv文件
    with open(csvPath, 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        for i in reader:
            # 声明key值有序字典
            dict[i['ID']] = collections.OrderedDict()
            # 遍历列标签，写入字段
            for value in keyList:
                dict[i['ID']][value] = i[value]
        # 关闭文件流
        csvFile.close()

    # 字典转json
    jsonInfo = json.dumps(dict, ensure_ascii=False)

    # 写入json至文件
    with open('data.json', 'wb') as jsonFile:
        jsonFile.write(jsonInfo)
        jsonFile.close()


if __name__ == '__main__':
    # 声明目标文件路径
    path = "Q8.csv"

    csvIntoJson(path)