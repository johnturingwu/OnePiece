首先，漫画网址：
https://one-piece.cn/comic/

我们查看一下网站的信息





我们看到和之国篇章正好id=“chapter12“，那我们的正则表达式就专门处理chapter12里面的<a>标签了。


首先制作获取chapter12里面的所有内容：


url = "https://one-piece.cn"
response = requests.get(url+"/comic")
pattern = re.compile('<div id="chapter12" class="chapter"'
                     '.*?<a href="(.+)" target="_blank"', re.S)
result = pattern.findall(response.text)




获取好之后在当前的结果里将漫画内容链接的页面获取过来，这时候我们要在第一次匹配的结果上再去匹配url：

pattern2 = re.compile('<a href="(.*?)"', re.S)
result = pattern2.findall(result[0])


结果：





我们可以看到所有漫画的部分url已经获取到了。

这个时候我们只需要在原来url做拼接就可以了。
url = "https://one-piece.cn"
comic_page = requests.get(url + chapter)


进入这个页面之后我们要获取当前集数的所有漫画图片：


我们随便选一集，来看看图片是如何获取的：



首先我们需要通过正则表达式匹配图片的URL：
我们看到规律，所有的图片都在<img>标签下，我们只需要获取标签里面的src属性里面的内容就好了。

pattern = re.compile('<img alt=".*?" src="(.*?)"', re.S)


这样一个正则表达式就能解决页面上的图片，获取内容如下：




我们需要将这个图片地址转化成图片保存下来，这时候我们就需要用到urlretrieve这个方法了。

因为我们要获取当前页面上的所有图片，所以我们需要遍历下载这些图片：

for pic in range(len(com_url)):
    urlretrieve(com_url[pic], './海贼王{}集/{}.jpg'.format(dir[-3], pic))
urlretrieve这个方法有两个参数，第一个是获取图片的地址，第二个是存放的路径。
