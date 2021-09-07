The purpose of this script is to help users sleep through 13:00 without illness or going out.
This script was tested in ubuntu 18.04 python 3.7 # 2020.2.15

# 注意：此脚本仅用于研究交流学习，使用请自行承担后果 #

Preparations:

1. 准备python环境 并建立一个工作文件夹
修改config.py中的平台账号密码
修改mail.py中的邮箱信息
将config.py automation.py mail.py复制到服务器工作文件夹下

2. 安装chrome驱动程序+chrome
sudo apt install chromium-chromedriver // 依赖chromium，会自动安装

3. 安装selenium自动化工具
pip install selenium

4. 测试脚本
python3 auto.py 1 // 晨检
python3 auto.py 2 // 午检
python3 auto.py 3 // 晚检
python3 auto-old.py // 除三次填报以外的每日打卡

5.使用crontab等部署定时任务即可
示例：
20 7 * * * python3 /root/sign/auto.py 1 > /root/sign/log.txt
20 12 * * * python3 /root/sign/auto.py 2 > /root/sign/log.txt
20 19 * * * python3 /root/sign/auto.py 3 > /root/sign/log.txt
20 5 * * * python3 /root/sign/auto-old.py > /root/sign/log.txt
