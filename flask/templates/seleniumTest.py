from selenium import webdriver
import json
from bs4 import BeautifulSoup

# 使用webkit无界面浏览器
# 如果路径为 exe 启动程序的路径，那么该路径需要加一个 r
driver = webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# 获取指定网页的数据  start_urls
# driver.implicitly_wait(5)
driver.get('http://www.dybee.co/')

dom = driver.find_element_by_tag_name('body')
cla = driver.find_elements_by_css_selector('.col-2 .intro h3')
print(cla[0].text)
# print(driver.forward())
# soup = driver.execute_script("return document.documentElement.outerHTML")
# resource = BeautifulSoup(soup, 'lxml')
# dom = resource.find(name='nav')
# print(dom.string)
driver.close()
