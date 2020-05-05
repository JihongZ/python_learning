from scrapy import Selector
import requests

# 游戏区三日内排行
url = "https://search.bilibili.com/all?keyword=%E6%9C%80%E7%BB%88%E5%B9%BB%E6%83%B3"  # 全站榜

html_bb = requests.get(url).content
sel = Selector(text=html_bb)

title_list = sel.xpath("//a[@class='title']").extract()





up_list = sel.css("div.rank-body a span.data-box::text ").extract()


## Top 10
for x in range(10):
    print(x+1, ".", up_list[x], ":",title_list[x])

