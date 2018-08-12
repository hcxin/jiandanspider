import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from com.chen.downloader import *
import queue
import pymysql

# 指定下载文件夹
path = "D:\\images_dir\\"
homepage_url = "http://jandan.net/ooxx"
homepage_response = requests.get(homepage_url, timeout=5)
homepage_html = BeautifulSoup(homepage_response.text, "html.parser")
current_elements = homepage_html.select(".current-comment-page")
start_page = eval(current_elements[0].text[1: len(current_elements[0].text) - 1]) + 1
print("总页数为: " + str(start_page))
prefix_url = "http://jandan.net/ooxx/page-"
page_num = eval(input("请输入下载页数:"))
suffix_url = "#comments"
# webdriver chrome
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
browser = webdriver.Chrome("D:\software\python\Scripts\chromedriver.exe", chrome_options=option)

if not os.path.exists(path):
    os.makedirs(path)

for page in range(page_num):
    request_url = '%s%s%s' % (prefix_url, start_page, suffix_url)
    try:
        browser.get(request_url)
    except:
        print("..........网络异常，正在重新连接..........")
        continue
    html = BeautifulSoup(browser.page_source, "html.parser")
    images = html.select(".view_img_link")
    image_path = path + str(start_page)+"\\"
    os.makedirs(image_path)
    for item in images:
        img_url = item["href"]
        try:
            downloader = Downloader()
            downloader.download_image(img_url, image_path)
        except:
            print("..........网络异常，正在重新连接..........")
            continue
    start_page -= 1
print("下载结束，保存路径为: " + path)
print("-------------------------------------------")
print("作者辛海臣，QQ：953899919")
input("----------------按回车鍵退出----------------")
