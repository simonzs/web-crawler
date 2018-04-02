# 一张图片下载
from urllib.request import urlopen, Request
import re
from bs4 import BeautifulSoup
def downloadimg(link, name):
    # link为图片链接，name为图片名字
    try:
        data = urlopen(link, timeout=100)
        # 打开连接
        tname = name + ".jpg"
        # 给图片命名
        with open(tname, "wb") as code:
            # 打开文件并保存数据
            code.write(data.read())
            print(tname + " is done.")
            # 打印提示文字
    except BaseException as e:
        print(type(e))

#图集下载 某一个人
def downloaditem(link,):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
               'Connection':'keep-alive'}
    try:
        req = Request(url=link, headers=headers)
        html = urlopen(req,timeout=100)# 打开连接
        bsObj = BeautifulSoup(html,"html.parser")#用bs解析html
        img = bsObj.find("img", "IMG_show")
        index = re.search(r'(.*)_(.*)', link).group(2)
        downloadimg(img.attrs['src'], index)
        curPage = bsObj.find("span","cur-page")
        next = curPage.next_sibling
        if next is not None:
            next_link = next.attrs['href']
            downloaditem(next_link)
    except BaseException as e:
        print(type(e))
downloaditem("http://www.youzi4.cc/mm/4172/4172_1.html",)# 下载图集
