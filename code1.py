#一张图片下载
from urllib.request import urlopen
def downloadimg(link, name):
# link为图片链接，name为图片名字
  data = urlopen(link, timeout=100)
    # 打开连接
  tname = name+".jpg"
    # 给图片命名
  with open(tname, "wb") as code:
    # 打开文件并保存数据
    code.write(data.read())
    print(tname+" is done.")
     # 打印提示文字
downloadimg("http://res.youzi4.cc/photo_files/news/20150527/1e415521-8721-4a89-8ed7-0b88431b5e5e.jpg","code_1")
     #根据图片URL下载图片