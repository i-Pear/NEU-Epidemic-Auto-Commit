"""
Made by @i.Pear 2020/02/15
"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

stuID = ""
firstPassword = ""


def run():
    driver.get('http://stuinfo.neu.edu.cn/')
    time.sleep(2)
    in1 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/div[2]/div[1]/input')
    in1.click()
    in1.clear()
    in1.send_keys(stuID)
    in2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/div[2]/div[2]/div/input')
    in2.click()
    in2.clear()
    in2.send_keys(firstPassword)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/button').click()
    time.sleep(2)
    print('Platfrom logined successfully.')
    # 平台登陆完成

    # 转向疫情页面
    driver.get('http://stuinfo.neu.edu.cn/#/studentPort/serveAdmin')
    time.sleep(2)
    print('Getting to the info site...')
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/section/section/section/main/div[1]/div[1]/div/div[2]/div/div/div').click()
    time.sleep(3)
    # 重定向完成

    # 开始填写信息
    driver.switch_to.window(driver.window_handles[1])
    box = driver.find_element_by_name('sfgcyiqz')
    box = Select(box)
    box.select_by_value('否')

    submit = driver.find_element_by_tag_name('button')
    submit.click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    # 填写信息结束


if __name__ == '__main__':

    lines = []
    with open("config.ini", encoding='UTF-8') as f:
        for line in f: lines.append(line)
    stuID = lines[1][:-1]
    firstPassword = lines[3][:-1]

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    print('\n' + '#' * 60)
    print('Chrome driver loaded successfully.')

    print('Using stuID = ' + stuID + ' PWD = ' + firstPassword + ' to login...')
    print('Starting operation...')
    run()

    time.sleep(2)

    driver.close()
    print('\nActions successfully done.\n')
