# -*- coding: utf-8 -*-
# @Project : APITestModel
# @File    : EmailDelivery.py
# @Author  : 朱宽
# @upTime    : 2024/6/17 14:20
# @Software: Win10 / Python3 / Pycharm# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)
'''
邮件发送给   田天赐  qq邮箱
'''
import yagmail

def send_email(report):
    yag = yagmail.SMTP(user="1798218285@qq.com", password="rtyykhfkhkmtcceb", host="smtp.qq.com"
                       )
    subject="自动化测试报告-附件"
    contents = "测试用例请查看附件"
    yag.send('1798218285@qq.com',subject=subject,contents=[contents, report])  #report附件

    print("email has been sent")

if __name__ == '__main__':
    html_report_path = '../../testreport/自动化测试报告-2024-06-13-16-44-22.html'
    send_email(html_report_path)

