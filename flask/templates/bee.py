from selenium import webdriver
import pymysql
import re
import json

service_args=[]
service_args.append('--load-images=no')  ##关闭图片加载
service_args.append('--disk-cache=yes')  ##开启缓存
service_args.append('--ignore-ssl-errors=true') ##忽略https错误

driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe',service_args=service_args)
# driver.implicitly_wait(10)        ##设置超时时间
# driver.set_page_load_timeout(10)  ##设置超时时间
source = []


# 打开数据库连接
# db = pymysql.connect("localhost", "root", "123456", "beedata")

# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

# def getMovie():
#     global source
#     if len(source) == 0:
#         driver.get('https://www.dybee.tv/')
#         source = driver.find_elements_by_css_selector('.recent-article')
#     # print(driver.page_source)
#     arr = []
#     for item in source:
#         types = re.search(r'\w*\/', item.find_element_by_css_selector('.mod-tit a').get_attribute('innerHTML'),
#                           re.I | re.M).group()
#         for itemSon in item.find_elements_by_css_selector('.update_area_lists .i_list'):
#             arr.append({
#                 'type': types,
#                 # 'title': re.search(r'《\w*》', itemSon.find_element_by_css_selector('h2').get_attribute('innerHTML'),
#                 #                    re.I | re.M).group(),
#                 'videoId': re.search(r'\d+', itemSon.find_element_by_css_selector('a').get_attribute('href'),
#                                      re.I | re.M).group()
#             })
#     return json.dumps(arr)

def getMovie():
    global source
    if len(source) == 0:
        driver.get('https://www.iqiyi.com/')
        source = driver.find_elements_by_css_selector('.recent-article')
    # print(driver.page_source)

    return json.dumps(driver.page_source)

# 退出浏览器
# driver.quit();

# 关闭数据库连接
# db.close()
