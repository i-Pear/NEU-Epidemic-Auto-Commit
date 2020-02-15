本脚本的用途是帮助用户在没病也没出门的情况下睡过13:00
本脚本在 ubuntu18.04 python3.7 环境下测试通过 2020.2.15

准备工作：

1. 准备python环境 并建立一个工作文件夹
修改config.ini中的平台账号密码
将config.ini automation.py复制到服务器工作文件夹下

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
