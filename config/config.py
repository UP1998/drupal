from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

def install(host):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome(r"D:/appdata/chromedriver.exe")

    driver.get(host)
    if "Choose language" in driver.page_source:
        print("start install!")
    s1 = Select(driver.find_element_by_id('edit-langcode'))  # 实例化Select
    s1.select_by_value("zh-hans")
    if "简体中文" in driver.page_source:
        driver.find_element_by_id("edit-submit").click()
    # 选择一种安装方式
    driver.find_element_by_id("edit-submit").click()
    print("installing...")
    time.sleep(220)
    # if "设置网站" in driver.page_source:
    #     print("edit")
    # elif :
    #     time.sleep(40)
    if "设置网站" in driver.page_source:
        print("edit")    
    # 站点名称
    driver.find_element_by_id("edit-site-name").send_keys("cmcc")
    # 站点的email地址
    driver.find_element_by_id("edit-site-mail").send_keys("cmcc@123.com")
    # 用户名
    driver.find_element_by_id("edit-account-name").send_keys("admin")
    # 密码
    driver.find_element_by_id("edit-account-pass-pass1").send_keys("adminpw")
    # 确认密码
    driver.find_element_by_id("edit-account-pass-pass2").send_keys("adminpw")
    # 电子邮件地址
    driver.find_element_by_id("edit-account-mail").send_keys("adminpw")
    # 自动检查更新取消
    driver.find_element_by_id("edit-enable-update-status-module").click()
    # 保存并退出
    driver.find_element_by_id("edit-submit").click()
    # 等待
    time.sleep(15)
    # 检测
    if "恭喜，您安装了 Drupal!" in driver.page_source:
        print("install success!")
    driver.close()

def config(host):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome(r"D:/appdata/chromedriver.exe")

    print("start config")
    # admin register
    driver.get(host + '/user/login')
    time.sleep(3)
    driver.find_element_by_id("edit-name").send_keys("admin")
    time.sleep(1)
    driver.find_element_by_id("edit-pass").send_keys("adminpw")
    time.sleep(1)
    driver.find_element_by_id("edit-submit").click()
    # goto 配置
    # driver.find_element_by_id("toolbar-link-system-admin_config").click()
    link = driver.find_element_by_id("toolbar-link-system-admin_config")
    url = link.get_attribute('href')
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/main/div[4]/div/div/div[2]/div[1]/div/ul/li/a").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/main/div[4]/div/form/details[4]/div/fieldset[1]/div/div/div[2]/label").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/main/div[4]/div/form/details[4]/div/div[1]/input").click()
    # submit
    driver.find_element_by_id("edit-submit").click()
    time.sleep(3)
    # 检测
    if "配置选项已保存" in driver.page_source:
        print("config success!")
    driver.close()

if __name__ == '__main__':
    # host = "http://192.168.56.101:8080"
    host = "http://web"
    # 安装
    time.sleep(5)
    install(host)
    # 新用户自行添加
    config(host)
