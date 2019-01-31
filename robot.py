import requests
import  json
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
chrome_options=Options()
#设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
# webservice url
url ="http://yourwebserviceip/getcustomer"
# 发起连接
result=requests.post(url)
print(result.text)
if result.text!="":
    cusdata = json.loads(result.text)
    print(cusdata['city'])
    print(cusdata)   # 输出返回信息，可以获知有那些method可以调用
    #  登录然后开始录入数据
    # 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
    browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver",chrome_options=chrome_options)
    # 2.通过浏览器向服务器发送URL请求
    browser.get("https://www.56linked.com/login.html")
    sleep(5)
    # 3.刷新浏览器
    browser.refresh()
    # 4.设置浏览器的大小
    browser.set_window_size(800, 600)
    # 5.登录
    element1 = browser.find_element_by_name("username")
    element1.clear()
    element1.send_keys("username")
    element2 = browser.find_element_by_name("password")
    element2.clear()
    element2.send_keys("password")
    btn = browser.find_element_by_id("enter")
    btn.click()
    sleep(5)
    browser.get("https://www.56linked.com/zPViO4B8.html")
    sleep(5)
    browser.refresh()
    sleep(5)
    browser.find_element_by_id("customerNew").click() #新增
    sleep(5)
    browser.find_element_by_id("customerEdit_name").send_keys(cusdata['name'])
    browser.find_element_by_id("customerEdit_fromProvince").send_keys(cusdata['province'])
    browser.find_element_by_id("customerEdit_fromCity").send_keys(cusdata['city'])
    browser.find_element_by_id("customerEdit_address").send_keys(cusdata['addr'])
    Select(browser.find_element_by_id("companyBusiGroupId")).select_by_value("5243")
    sleep(2)
    browser.find_element_by_id("submitButton").click()
    sleep(2)
    browser.quit()
else:
    # webservice url
    url = "http://yourwebserviceip/home/getaddress"
    # 发起连接
    result = requests.post(url)
    print(result.text)
    if result.text != "":
        cusdata = json.loads(result.text)
        print(cusdata['city'])
        print(cusdata)  # 输出返回信息，可以获知有那些method可以调用
        #  登录然后开始录入数据
        # 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
        browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver",chrome_options=chrome_options)
        # 2.通过浏览器向服务器发送URL请求
        browser.get("https://www.56linked.com/login.html")
        sleep(5)
        # 3.刷新浏览器
        browser.refresh()
        # 4.设置浏览器的大小
        browser.set_window_size(800, 600)
        # 5.登录
        element1 = browser.find_element_by_name("username")
        element1.clear()
        element1.send_keys("username")
        element2 = browser.find_element_by_name("password")
        element2.clear()
        element2.send_keys("password")
        btn = browser.find_element_by_id("enter")
        btn.click()
        sleep(5)
        browser.get("https://www.56linked.com/JIzXnZG1.html")
        sleep(5)
        browser.refresh()
        sleep(5)
        browser.find_element_by_id("add").click()  # 新增
        sleep(5)
        browser.find_element_by_id("locationWarehouseIndexDetailPage_name").send_keys(cusdata['code'])
        browser.find_element_by_id("locationWarehouseIndexDetailPage_byname").send_keys(cusdata['name'])
        browser.find_element_by_id("locationWarehouseIndexDetailPage_fromProvince").send_keys(cusdata['province'])
        browser.find_element_by_id("locationWarehouseIndexDetailPage_fromCity").send_keys(cusdata['city'])
        check1 = browser.find_element_by_name("locationWarehouseIndexDetailPage_beConsignee")
        sleep(5)
        check1.click()
        assert (check1.is_selected(), u"收货人复选框未被选中！")
        browser.find_element_by_id("locationWarehouseIndexDetailPage_longitude").send_keys(cusdata['longitude'])
        browser.find_element_by_id("locationWarehouseIndexDetailPage_latitude").send_keys(cusdata['latitude'])
        browser.find_element_by_id("locationWarehouseIndexDetailPage_address").send_keys(cusdata['addr'])
        sleep(2)
        browser.find_element_by_id("locationWarehouseIndexDetailPage_confirm").click()
        sleep(2)
        browser.quit()




