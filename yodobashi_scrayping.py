import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary 

driver = webdriver.Chrome()
driver.get("https://www.yodobashi.com/category/6353/6357/6407/6636/")

time.sleep(2)

product_list = driver.find_elements_by_css_selector("div.srcResultItem.spt_hznList.tileTypeList.js_productList.changeTile")
p = product_list[0]
product_name = p.find_elements_by_css_selector(".pName.fs14")
# print(product_name.text)
# maker = p.find_elements_by_css_selector(".pSubInfo.pcParts")
res = {}
i = 0
for pn in product_name:
    i = i+1
    list_product = pn.text.splitlines()
    d1 = {i: list_product}
    res.update(d1)

print(res) 


driver.quit()


#listContents > div.srcResultItem.spt_hznList.tileTypeList.js_productList.changeTile//*[@id="listContents"]/div[3]/div[1]/a/div[2]/p[1]