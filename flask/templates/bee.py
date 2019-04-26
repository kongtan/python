from selenium import webdriver
import json

driver = webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
source = []


def getMovie():
    global source
    if len(source) == 0:
        driver.get('https://www.dybee.tv/')
        source = driver.find_elements_by_css_selector('.recent-article')
    # print(driver.page_source)
    arr = []
    for item in source:
        arr.append(item.get_attribute('innerHTML'))
    return json.dumps(arr)
