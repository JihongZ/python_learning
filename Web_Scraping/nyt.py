from scrapy import Selector

import requests

url = "https://www.nytimes.com/"

html = requests.get( url ).content


sel = Selector( text=html )

h2_all = sel.xpath("//h2")
h2_all_css = sel.css("h2")
len(h2_all.extract())

len(h2_all_css.extract())


url_short = "https://datacamp.com/courses/web-scraping-with-python"

html = requests.get(url_short).content

sel = Selector( text = html)


chapter_blocks = sel.css('ol.chapters div.chapter__title-wrapper h4.chapter__title::text').extract()

h2_all = sel.xpath("//h2")
h2_all_css = sel.css("h2")
len(h2_all.extract())

len(h2_all_css.extract())
