#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

mail_host = "smtp.qq.com"
# SMTP服务器
mailPort = 465
# QQ邮箱的端口号


mail_user = "434317543@qq.com"
# 用户名
mail_pass = "xxxx"
# 授权密码，非登录密码
# 发送邮箱
receivers = '434317543@qq.com'


# 接收邮件，可设置为你的QQ邮箱或者其他邮箱

def sendMail(ifok: bool, msg: str):
    # 第三方 SMTP 服务

    # ifok为真发送成功邮件，失败发送失败邮件

    if ifok:
        # 成功邮件

        message = MIMEText('打卡成功!', 'plain', 'utf-8')
        # 正文
        message['From'] = formataddr(['海螺姑娘', mail_user])
        # 发送者
        message['to'] = formataddr(['公主大人', receivers])
        # 接受者
        message['Subject'] = '打卡成功了，公主大人！'
    else:
        # 发送邮件失败

        message = MIMEText('打卡失败了，公主大人呜呜，快来查看情况呀!\n', 'plain', 'utf-8')
        # 正文
        message['From'] = formataddr(['海螺姑娘', mail_user]) + msg
        # 发送者
        message['to'] = formataddr(['公主大人', receivers])
        # 接受者
        message['Subject'] = '打卡失败'

    print('邮件填写完毕')

    print('正在连接至服务器')
    ret = True
    try:
        smtpServer = smtplib.SMTP_SSL(mail_host, mailPort)

        print('服务器连接成功')

        smtpServer.login(mail_user, mail_pass)
        # 连接邮箱服务器,

        print('登录成功')

        smtpServer.sendmail(mail_user, [receivers, ], message.as_string())
        # 发送邮件

        print('邮件已发送')

        smtpServer.quit()
        # 关闭连接

        print('连接关闭')
    except Exception:
        ret = False
        smtpServer.quit()
    return ret


'''
if __name__ == '__main__':
    print('欢迎使用自动发送邮件系统')
    print('正在启动...')
    ret = famail(True)
    if ret:
        print('发送成功')
    else:
        print('发送失败')
    famail(False)
'''
