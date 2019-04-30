from selenium import webdriver
import pymysql
import re
import json

driver = webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
source = []


# 打开数据库连接
# db = pymysql.connect("localhost", "root", "123456", "beedata")

# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

def getMovie():
    global source
    if len(source) == 0:
        driver.get('https://www.dybee.tv/')
        source = driver.find_elements_by_css_selector('.recent-article')
    # print(driver.page_source)
    arr = []
    for item in source:
        types = re.search(r'\w*\/', item.find_element_by_css_selector('.mod-tit a').get_attribute('innerHTML'),
                          re.I | re.M).group()
        for itemSon in item.find_elements_by_css_selector('.update_area_lists .i_list'):
            arr.append({
                'type': types,
                'title': re.search(r'《\w*》', itemSon.find_element_by_css_selector('h2').get_attribute('innerHTML'),
                                   re.I | re.M).group(),
                'videoId': re.search(r'\d+', itemSon.find_element_by_css_selector('a').get_attribute('href'),
                                     re.I | re.M).group()
            })
    return json.dumps(arr)

# 关闭数据库连接
# db.close()
