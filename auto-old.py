# coding:utf-8

"""
Made by @i.Pear 2020/04/14
"""

import os
import time
import traceback

from config import stuID, platfromPassword
from selenium import webdriver
from mail import sendMail
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

logText = ""


def printLog(msg):
    global logText
    print(msg)
    logText = logText + msg + '\n'


def run():
    driver.get('https://ehall.neu.edu.cn/infoplus/form/JKXXSB/start')
    time.sleep(1)

    WebDriverWait(driver, 10).until(lambda x: len(x.find_elements_by_xpath('//*[@id="un"]')) > 0)
    in1 = driver.find_element_by_xpath('//*[@id="un"]')
    in1.click()
    in1.clear()
    in1.send_keys(stuID)

    WebDriverWait(driver, 10).until(lambda x: len(x.find_elements_by_xpath('//*[@id="pd"]')) > 0)
    in2 = driver.find_element_by_xpath('//*[@id="pd"]')
    in2.click()
    in2.clear()
    in2.send_keys(platfromPassword)

    WebDriverWait(driver, 10).until(lambda x: len(x.find_elements_by_xpath('//*[@id="index_login_btn"]')) > 0)
    driver.find_element_by_xpath('//*[@id="index_login_btn"]').click()
    time.sleep(1)
    WebDriverWait(driver, 60).until(lambda x: len(x.find_elements_by_xpath('//*[@id="app"]/main/div/form')) > 0)
    printLog('Platfrom logined successfully.')
    # 平台登陆完成

    # 开始填写信息
    time.sleep(5)
    WebDriverWait(driver, 60).until(lambda x: len(
        x.find_elements_by_xpath(
            '//*[@id="app"]/main/div/form/div[1]/table/tbody/tr/td[1]/div/div/div/label[1]/span[1]/span')) > 0)
    driver.find_element_by_xpath(
        '//*[@id="app"]/main/div/form/div[1]/table/tbody/tr/td[1]/div/div/div/label[1]/span[1]/span').click()

    time.sleep(5)
    WebDriverWait(driver, 60).until(lambda x: len(x.find_elements_by_xpath(
        '//*[@id="app"]/main/div/form/div[3]/div[2]/table/tbody/tr/td/div/div/div/label[1]/span[1]/span')) > 0)
    driver.find_element_by_xpath(
        '//*[@id="app"]/main/div/form/div[3]/div[2]/table/tbody/tr/td/div/div/div/label[1]/span[1]/span').click()

    time.sleep(5)
    WebDriverWait(driver, 60).until(lambda x: len(x.find_elements_by_xpath(
        '//*[@id="app"]/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span')) > 0)
    driver.find_element_by_xpath(
        '//*[@id="app"]/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span').click()

    time.sleep(5)
    WebDriverWait(driver, 60).until(lambda x: len(x.find_elements_by_xpath(
        '//*[@id="app"]/main/div/form/div[6]/button')) > 0)
    driver.find_element_by_xpath('//*[@id="app"]/main/div/form/div[6]/button').click()
    
    
    
    
    
    
    time.sleep(5)
    driver.save_screenshot('1.png')
    time.sleep(5)

    windows = driver.window_handles
    print('#debug: windows count=', len(windows))
    WebDriverWait(driver, 30).until(
        lambda x: len(x.find_elements_by_xpath('//*[@id="app"]/main/div/div/div/div/div[1]')) > 0)
    if driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/div/div[1]').text != "上报成功":
        raise Exception("Unknown ERROR")
    printLog(driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/div/div[1]').text)
    # 填写信息结束


if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    printLog('\n' + '#' * 60)
    printLog(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    printLog('Chrome driver loaded successfully.')

    printLog('Using stuID = ' + stuID + ' PWD = ' + platfromPassword + ' to login...')
    printLog('Starting operation...\n')

    ifSuccess = False
    tryTimes = 0

    while (not ifSuccess) and tryTimes < 20:
        try:
            tryTimes += 1
            printLog('Trying ' + str(tryTimes) + ' times...')
            run()
            time.sleep(1)
            printLog('\nActions successfully done.\n')
            ifSuccess = True
        except Exception as ex:
            printLog('ERROR : ' + traceback.format_exc())
            time.sleep(200)

    driver.quit()

    if ifSuccess:
        sendMail(True, "")
    else:
        sendMail(False, logText)