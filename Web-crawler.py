#http://www.youzi4.cc/

import socket

from urllib.request import urlopen, Request

import re

import os

import time
from bs4 import BeautifulSoup


forbidchar = r'<|>|/|\\|\||:|"|\*|\?'  # 系统禁止用作文件名的字符，正则表达式

#一张图片下载
def downloadimg(link, name):            # link为图片链接，name为图片名字

    try:
        data = urlopen(link, timeout=100)    # 打开连接

        tname = name+".jpg"                 # 给图片命名

        with open(tname, "wb") as code:     # 以追加二进制模式打开文件，并保存数据

            code.write(data.read())

        print('                                                 ' + tname+" is done.")            # 打印提示文字

    except BaseException as e:

        print(type(e))

#图集下载 某一个人
def downloaditem(link,):


    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
               'Connection':'keep-alive'}

    req = Request(url=link, headers=headers)

    try:

        html = urlopen(req,timeout=100)# 打开连接

        bsObj = BeautifulSoup(html,"html.parser")#用bs解析html

        img = bsObj.find("img", "IMG_show")

        index = re.search(r'(.*)_(.*)', link).group(2)

        downloadimg(img.attrs['src'], index)

        curPage = bsObj.find("span","cur-page")

        next = curPage.next_sibling

        if next is not None:

            next_link = next.attrs['href']

            downloaditem(next_link)###########################################################################

    except BaseException as e:

        print(type(e))

#获取不同人的图集链接
def downloadpersons(link):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
               'Connection':'keep-alive'}

    req = Request(url=link, headers=headers)

    try:

        html = urlopen(req,timeout=100)# 打开连接

        bsObj = BeautifulSoup(html,"html.parser")#用bs解析html

        div = bsObj.find("div","MeinvTuPianBox")

        for a in div.find_all('a','tit'):

            name = a.attrs['title']

            name = re.split(forbidchar, name)

            name = '.'.join(name)  # 跟图片文件名原理一样，替换被禁止的字符

            if not os.path.exists(name):  # 检查这个人的文件夹之前有没有创建

                os.mkdir(name)  # 如果没有就创建一个

            PATHtmp = os.getcwd()                      # PATHtmp是这一层人名文件夹的路径

            os.chdir(name)  # 进入这个目录

            print('                      (pictures_one_person)' + name + 'starting')

            downloaditem(a.attrs['href'],)# 下载图集

            print('                      (pictures_one_person) this gril is finished')
            print('                      -----------------------------------------------')
            os.chdir(PATHtmp)  # 回到上一层目录，这里用的绝对路径，避免中途被打断导致后面的下载也出现错误

            #break################################################################################################

        curPage = bsObj.find("span","cur-page")

        next = curPage.next_sibling

        if next is not None:

            next_link = next.attrs['href']

            downloadpersons(next_link)########################################################################

    except Exception as e:

        print(type(e))  # catched

if __name__ == "__main__":

    name = "img"

    if not os.path.exists(name):  # 检查这个人的文件夹之前有没有创建

        os.mkdir(name)  # 如果没有就创建一个

    PATHtmp = os.getcwd()  # PATHtmp是这一层人名文件夹的路径

    os.chdir(name)  # 进入这个目录

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
               'Connection':'keep-alive'}

    req = Request(url="http://www.youzi4.cc/", headers=headers)

    html = urlopen(req,timeout=100)# 打开连接

    bsObj = BeautifulSoup(html, "html.parser")            # bs解析

    Navigation = bsObj.find('a',title='美女导航')

    div = Navigation.parent.find("div")

    for index in range(0,3):

        index = index * 2 + 1

        link = div.contents[index]

        alt = link.get_text()

        if not os.path.exists(alt):  # 检查这个人的文件夹之前有没有创建

            os.mkdir(alt)  # 如果没有就创建一个

        PATHtmp = os.getcwd()  # PATHtmp是这一层人名文件夹的路径

        os.chdir(alt)  # 进入这个目录

        print('[class]' + alt + 'is starting')

        downloadpersons(link.attrs['href'])

        print('[class]' + alt + 'is finished')
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

        os.chdir(PATHtmp)  # 回到上一层目录，这里用的绝对路径，避免中途被打断导致后面的下载也出现错误

    os.chdir(PATHtmp)  # 回到上一层目录，这里用的绝对路径，避免中途被打断导致后面的下载也出现错误