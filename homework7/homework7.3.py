# -*- encoding: utf-8 -*-
'''
@File : homework7.3.py
@Time : 2020/05/27 08:51:19
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# 给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  
# 请大家写一个爬虫，将里面的英语节目MP3，都下载下来；

import requests
import subprocess
from urllib.parse import quote
import r


def get_source():
     head = {'User-Agent':
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/81.0.4044.122 Safari/537.36'}
     try:
          # 爬取网页
          url = "http://www.listeningexpress.com/studioclassroom/ad/"
          html = requests.get(url, headers=head, timeout=30)
          html.raise_for_status()
          html.encoding = html.apparent_encoding
          text = html.text
          # 匹配mp3格式文件
          rec = re.compile(r"sc-ad\s\d{4}-\d{2}-\d{2}\s.*?\.mp3")
          mp3_link = rec.findall(text)
          for mp3 in mp3_link:
               # 去除转义字符
               mp3 = mp3.replace('\\', '')
               # 拼接命令
               # 命令需要根据本机情况修改，否则会出现调用问题
               com = "Wget -P D:\\doc\\python-practice\\homework7\\mp3 " + url + quote(mp3)
               # 通过shell调用命令
               subprocess.Popen(com, cwd="D:\\doc\\", shell=True)
     except WindowsError as we:
          print("控制台指令有误！请根据本机情况修改。")
     except Exception as e:
          print(e)


if __name__ == '__main__':
     get_source()