import os
import requests


# 下载图片
class Downloader(object):
    def __init__(self):
        pass

    @staticmethod
    def download_image(img_url, path):
        url = "http:" + img_url
        image_response = requests.get(url, timeout=5)
        if image_response.status_code == 200:
            open(path + img_url[25:], "wb").write(image_response.content)
            print("download image success url is :[" + url + "]")
