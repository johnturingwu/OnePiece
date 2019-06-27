import os
os.makedirs('./image/', exist_ok=True)
IMAGE_URL = 'http://wx3.sinaimg.cn/large/83940082gy1g3kfbnl4ynj20nm11iaeo.jpg'
"""
保存图片的三种方法
"""
def urllib_download():
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './image/img1.png')     

def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./image/img2.png', 'wb') as f:
        f.write(r.content)                      

def chunk_download():
    import requests
    r = requests.get(IMAGE_URL, stream=True)    
    with open('./image/img3.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

urllib_download()
print('download img1')
request_download()
print('download img2')
chunk_download()
print('download img3')
