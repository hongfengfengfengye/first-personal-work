#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
import requests
import urllib.request
def main():
    cursor = "0"
    source = "1613549142009"
    num=10000
    for i in range(0, num):
        baseurl = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cursor + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=" + str(source)
        html = GetUrl(baseurl)  # 获取网页
        commentList = GetComment(html)  # 获取评论
        SaveComment(commentList)  # 保存评论
        findeCursor = re.compile(r'"last":"(.*?)"', re.S)  # 获取本页cursor码列表
        cursor = re.findall(findeCursor, html)[0]       # 获取下一页的cursor码
        source = int(source) + 1  # 获取下一页的source码

def GetComment(html):  # 爬取单页评论
    findeComment = re.compile(r'"content":"(.*?)"', re.S)
    comment = re.findall(findeComment, html)
    # print(comment)
    return comment

def GetUrl(url):  # 获取网页
    html = urllib.request.urlopen(url).read().decode("utf-8")
    return html

def SaveComment(datalist):
    with open("评论.txt", "a+", encoding="utf-8") as f:
        for i in datalist:
            i = i.replace("\n", "")
            f.write(i)
            f.write("\n")
if __name__ == '__main__':  # 当程序执行时调用函数
    main()
    print('爬取完成')

