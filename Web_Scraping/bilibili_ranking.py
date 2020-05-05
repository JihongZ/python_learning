from scrapy import Selector
import requests

# 游戏区三日内排行
url = "https://www.bilibili.com/ranking/all/0/0/3" #全站榜

html_bb = requests.get(url).content


sel = Selector(text=html_bb)

title_list = sel.css("div.rank-body div.info > a.title::text").extract()

up_list = sel.css("div.rank-body a span.data-box::text ").extract()


## Top 10
for x in range(10):
    print(x+1, ".", up_list[x], ":",title_list[x])

