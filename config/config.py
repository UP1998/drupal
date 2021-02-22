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
    while (1):
        if "Choose language" in driver.page_source:
            print("start install translation...")
            break
        else:
            time.sleep(10) 
            driver.refresh()
    s1 = Select(driver.find_element_by_id('edit-langcode'))  # 实例化Select
    s1.select_by_value("zh-hans")
    if "简体中文" in driver.page_source:
        driver.find_element_by_id("edit-submit").click()
    # 选择一种安装方式
    driver.find_element_by_id("edit-submit").click()
    print("installing translation files...")
    time.sleep(100) 
    while (1):
        if "导入了一个翻译文件。" in driver.page_source:
            print("start edit web attributes...")
            break
        else:
            print("sorry, haven't been completed! please wait for another 50s...")
            time.sleep(50)

    # if "设置网站" in driver.page_source:
    #     print("edit")
    # elif :
    #     time.sleep(40)
    # if "导入了一个翻译文件。" in driver.page_source:
    #     print("start edit web attributes...")    
    # 站点名称
    driver.find_element_by_id("edit-site-name").send_keys("和飞信社区")
    # 站点的email地址
    driver.find_element_by_id("edit-site-mail").send_keys("admin@123.com")
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
    time.sleep(5)
    # 检测
    while (1):
        if "恭喜，您安装了 Drupal!" in driver.page_source:
            print("install success!")
            break
        else:
            time.sleep(5)
    driver.close()

def config(host):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome(r"D:/appdata/chromedriver.exe")

    print("start config")
    # register config
    print("change the user register ways")
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
        print("register changed")

    # change logo
    print("change logo")
    time.sleep(5)
    # 点击主菜单的外观
    link=driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/nav/div[1]/ul/li[3]/a")
    url=link.get_attribute('href')  #提取a标签内的链接，注意这里提取出来的链接是字符串
    driver.get(url)
    # 点击外观中设置
    driver.find_element_by_xpath("/html/body/div[2]/header/div/div/div[2]/nav/nav/ul/li[2]/a").click()
    # 点击取消使用主题提供的logo
    driver.find_element_by_id("edit-default-logo").click()
    time.sleep(1)
    # 填写自定义标志的路径
    driver.find_element_by_id("edit-logo-path").clear()
    driver.find_element_by_id("edit-logo-path").send_keys("logo.png")
    driver.find_element_by_id("edit-submit").click()
    time.sleep(3)    
    # 检测
    if "配置选项已保存" in driver.page_source:
        print("logo changed")
    
    # add blogs
    print("add blogs")
    time.sleep(5)
    # 点击主菜单的外观
    link=driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/nav/div[1]/ul/li[1]/a")
    url=link.get_attribute('href')  #提取a标签内的链接，注意这里提取出来的链接是字符串
    driver.get(url)
    # 点击添加内容-文章
    driver.find_element_by_xpath("/html/body/div[2]/div/main/div[4]/div[1]/ul/li/a").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/main/div[4]/div/ul/li[1]/a").click()
    # 创建文章
    driver.find_element_by_id("edit-title-0-value").send_keys("欢迎来到和飞信社区！")
    driver.find_element_by_id("edit-body-0-value").send_keys("尊敬的用户你好，这里是和飞信社区，请大家畅所欲言！如有问题，请联系管理员：admin@123.com，感谢您的使用！")
    driver.find_element_by_id("edit-submit").click()
    time.sleep(3)
    # 点击主菜单的外观
    link=driver.find_element_by_xpath("/html/body/div[1]/nav/div[2]/div/nav/div[1]/ul/li[1]/a")
    url=link.get_attribute('href')  #提取a标签内的链接，注意这里提取出来的链接是字符串
    driver.get(url)
    # 点击添加内容-文章
    driver.find_element_by_xpath("/html/body/div[2]/div/main/div[4]/div[1]/ul/li/a").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/main/div[4]/div/ul/li[1]/a").click()
    # 创建文章
    driver.find_element_by_id("edit-title-0-value").send_keys("【重要通知】和飞信社区版块调整及规范通知")
    driver.find_element_by_id("edit-body-0-value").send_keys("尊敬的和飞信社区用户：您好！为规范社区发帖内容，即日起将永久下架“其他”版块。再次感谢大家对社区规则秩序的遵守，希望大家多体验产品，多发布与产品相关的攻略、建议或问题等，我们一起努力共同建设和维护好和飞信社区大家庭。")
    driver.find_element_by_id("edit-submit").click()
    time.sleep(3)
    # 检测
    if "文章" in driver.page_source and "已创建。" in driver.page_source:
        print("add blogs success!")
        print("config success!")
    driver.close()

if __name__ == '__main__':
    # host = "http://192.168.56.106:8080"
    host = "http://web"
    # 安装
    install(host)
    # 新用户自行添加
    config(host)
