import os
import requests
import re
import time
from urllib.request import urlretrieve


def get_page(url):
    response = requests.get(url + "/comic")
    pattern = re.compile('<div id="chapter12" class="chapter"'
                         '.*?<a href="(.+)" target="_blank"', re.S)
    pattern2 = re.compile('<a href="(.*?)"', re.S)
    result = pattern.findall(response.text)
    result = pattern2.findall(result[0])
    return result


def get_pic(chapter):
    dir = chapter.replace("/", "")
    print("url = ", url + chapter)
    comic_page = requests.get(url + chapter)
    pattern = re.compile('<img alt=".*?" src="(.*?)"', re.S)
    com_url = pattern.findall(comic_page.text)
    print(com_url)
    # 创建目录
    os.makedirs('./海贼王{}集/'.format(dir[-3]), exist_ok=True)
    # 获取当前页面漫画上的所有图片
    for pic in range(len(com_url)):
        urlretrieve(com_url[pic], './海贼王{}集/{}.jpg'.format(dir[-3], pic))
    print("海贼王和之国篇, 爬取第{}篇结束.....".format(dir[-3:]))


url = "https://one-piece.cn"
result = get_page(url)
print(result)
for chapter in result:
    time.sleep(2)
    get_pic(chapter)


# url = "https://one-piece.cn"
# response = requests.get(url+"/comic")
# pattern = re.compile('<div id="chapter12" class="chapter".*?<a href="(.+)" target="_blank"', re.S)
# pattern2 = re.compile('<a href="(.*?)"', re.S)
# result = pattern.findall(response.text)
# result = pattern2.findall(result[0])
# print(result)
#
#
# for chapter in result:
#     time.sleep(2)
#     dir = chapter.replace("/", "")
#     print("url = ", url + chapter)
#     comic_page = requests.get(url + chapter)
#     pattern = re.compile('<img alt=".*?" src="(.*?)"', re.S)
#     com_url = pattern.findall(comic_page.text)
#     print(com_url)
#     # 创建目录
#     os.makedirs('./{}/'.format(dir), exist_ok=True)
#     for pic in range(len(com_url)):
#         urlretrieve(com_url[pic], './{}/{}.jpg'.format(dir, pic))
#
#     print("海贼王和之国篇, 第{}篇章结束.....".format(dir))

