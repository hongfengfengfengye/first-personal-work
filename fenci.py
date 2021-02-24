#!/usr/bin/env python
# coding: utf-8

# In[5]:


import jieba
import json
txt = open('C:/Users/Shinelon/评论.txt','r', encoding = 'utf-8').read()
txt = jieba.lcut(txt)
counts = {}
wdic = {}
diclist = []
for word in txt:
    if len(word) == 1:
        continue
    else:
        rword = word
        counts[rword] = counts.get(rword,0) + 1             
li = list(counts.items())
li.sort(key=lambda x:x[1], reverse=True)
for i in range(len(li)):
    dlist = {}
    dlist["name"] = li[i][0]
    dlist["value"] = li[i][1]
    diclist.append(dlist)
wdic["data"] = diclist
with open("termFrequency.json","w",encoding='utf-8') as file:
    json.dump(wdic,file,ensure_ascii=False, indent=4)


# In[ ]:




