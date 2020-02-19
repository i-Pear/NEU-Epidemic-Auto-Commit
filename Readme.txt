The purpose of this script is to help users sleep through 13:00 without illness or going out.
This script was tested in ubuntu 18.04 python 3.7 # 2020.2.15

# 注意：此脚本仅用于研究交流学习，使用请自行承担后果 #

Preparations:

1. 准备python环境 并建立一个工作文件夹
修改config.py中的平台账号密码
修改mail.py中的邮箱信息
将config.py automation.py mail.py复制到服务器工作文件夹下

2. 安装chrome
wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

3. 安装selenium自动化工具
pip install selenium

4. 安装chrome驱动程序
wget -c https://cdn.npm.taobao.org/dist/chromedriver/80.0.3987.16/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv chromedriver /usr/bin/

5. 测试脚本
python automation.py

6.使用crontab等部署定时任务即可
