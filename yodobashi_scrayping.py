import time
import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary 

url = "https://www.yodobashi.com/category/6353/6357/6407/6636/" # 初期ページのURLを格納
# url = "https://www.yodobashi.com/category/6353/6357/6407/500000185000/"
res = [["#", "メーカー", "商品名"]] # 結果格納用
i = 0 # 結果ID用
driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)

# 初期ページ
product_list = driver.find_elements_by_css_selector("div.srcResultItem.spt_hznList.tileTypeList.js_productList.changeTile")

p = product_list[0]
product_name = p.find_elements_by_css_selector(".pName.fs14")


for pn in product_name:
    i = i+1
    list_product = pn.text.splitlines()
    d1 = [i, list_product[0], list_product[1]]
    res.append(d1)

print(res) 

# 2ページ以降
page_num = 1
while True:
    try:
        page_num =page_num + 1 
        url1 = url + "p" + str(page_num)
        driver.get(url1)
        product_list = driver.find_elements_by_css_selector("div.srcResultItem.spt_hznList.tileTypeList.js_productList.changeTile")
        p = product_list[0]
        product_name = p.find_elements_by_css_selector(".pName.fs14")

        for pn in product_name:
            i = i+1
            list_product = pn.text.splitlines()
            d1 = [i, list_product[0], list_product[1]]
            res.append(d1)
        print(res)

    except:
        driver.quit()
        break

f = open('out.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerows(res)
f.close()
