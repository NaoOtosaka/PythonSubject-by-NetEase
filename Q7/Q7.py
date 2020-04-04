# coding=utf-8

# 题目：
# 实现一段代码，访问 https://www.baidu.com/，将其页面中加载的所有 png 格式的图片
# 存储到本地
# 考察点：网络爬虫、文件操作

import bs4
import urllib2
import re


def getHttpContent(address, outHtml=False):
    """
    url内容获取模块
    :param address: 目标url
    :param outHtml: 是否输出html
    :return: url内容
    """
    # 建立请求
    request = urllib2.Request(address)

    # 添加头信息
    request.add_header("user-agent", "Mozilla/5.0")

    try:
        # 发送请求
        response = urllib2.urlopen(request)

        # print response.getcode()  # 返回状态码(调试用

        if response.getcode() == 200:
            # 获取内容
            content = response.read()

            if outHtml:
                # 输出html字符串
                content = bs4.BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

            return content
    except:
        print 'connection failed'


def urlManager(htmlContent, target):
    """
    url管理模块
    :param htmlContent: html格式url内容
    :param target:  目标html标签
    :return:    url列表
    """
    # 初始化url集合
    urls = set()

    # 根据tag和正则规则筛选出html字符串中的url
    data = htmlContent.find_all(target, src=re.compile(r'(\.png)'))

    # 遍历筛选出的url并进行格式化
    for value in data:
        value = 'http:' + value['src']
        # value = value['src']
        urls.add(value)     # add进url集合中

    # 转换集合为列表
    urls = list(urls)

    return urls


def downloadImg(urlList):
    """
    图片下载模块
    :param urlList: url列表
    :return:
    """
    # 图片序号tag
    tag = 1

    # 遍历url并进行操作
    for url in urlList:
        # 获取图片url内容
        img = getHttpContent(url)

        if img:     # 当内容存在时
            # 拼接文件名
            img_name = tag.__str__() + '.png'

            # 创建并写入内容
            with open(img_name, 'wb') as f:
                f.write(img)
                f.close()

            print 'Download success'

            tag += 1
        else:
            print 'Download failed'
            continue


def main(url):
    """
    爬虫主循环
    :param url: 目标url
    :return:
    """
    # 获取目标url的html内容
    links = getHttpContent(url, outHtml=True)

    print 'connection success'

    # 抓取img标签内的url
    urlList = urlManager(links, 'img')

    # 对图片url进行下载
    downloadImg(urlList)


if __name__ == '__main__':
    # 目标url设定
    address = 'http://www.baidu.com/'

    # 启动爬虫
    main(address)