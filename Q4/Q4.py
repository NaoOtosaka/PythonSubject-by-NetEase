# coding=UTF-8

# 题目:
# 给邮箱 qa_2020@163.com 发送邮件，主题为自己的姓名，正文为"hello world"
# 考察点：邮件操作

# 引入smtp模块和email模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendEmail(mail_host, from_addr, to_addr, subject, msg, coding='utf-8', sub_Type='plain', mail_user=None, mail_pw=None, server_port=25):
    """
    邮件发送功能
    :param mail_host:邮件服务器
    :param from_addr:发件地址
    :param to_addr:收件地址
    :param subject:邮件主题
    :param msg:邮件正文
    :param coding:邮件内容编码（默认utf-8）
    :param sub_Type:邮件文本格式（默认plain）
    :param mail_user:邮件服务器用户名（服务器为localhost可缺省）
    :param mail_pw:邮件服务器口令（服务器为localhost可缺省）
    :param server_port:邮件服务器端口（默认25）
    :return:
    """
    debug = 0   # 调试模式（0关闭，1打开）

    # 邮件构造
    message = MIMEText(msg, sub_Type, coding)   # 正文
    message['From'] = Header(from_addr)     # 发件人
    message['To'] = Header(to_addr)     # 收件人
    message['Subject'] = Header(subject, coding)    # 主题

    try:
        if mail_host == 'localhost' or mail_host == '127.0.0.1':    # 当服务器为本地时
            smtpObj = smtplib.SMTP(mail_host)
            smtpObj.set_debuglevel(debug)
        else:    # 当服务器为第三方SMTP服务器时
            smtpObj = smtplib.SMTP()
            smtpObj.set_debuglevel(debug)
            smtpObj.connect(mail_host, server_port)
            smtpObj.login(mail_user, mail_pw)

        # 发送
        smtpObj.sendmail(from_addr, to_addr, message.as_string())
        print '发送成功'
    except smtplib.SMTPException:
        print '发送失败'


if __name__ == '__main__':
    # 基础信息设置
    host = 'smtp.qq.com'
    user = 'xxxxxxxxx@qq.com'
    password = 'xxxxxxxxxxx'
    port = 25

    From = 'xxxxxxxxx@qq.com'
    To = 'xxxxxxxxx@126.com'

    title = ''
    content = 'hello world'

    # 发送
    sendEmail(host, From, To, title, content, mail_user=user, mail_pw=password, server_port=port)