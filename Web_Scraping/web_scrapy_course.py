# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess


url_short = "https://datacamp.com/courses/web-scraping-with-python"

html = requests.get(url_short).content

sel = Selector(text=html)


chapter_blocks = sel.css(
    'ol.chapters div.chapter__title-wrapper h4.chapter__title::text').extract()

# Create the Spider class
class DC_Description_Spider(scrapy.Spider):
  name = "dc_chapter_spider"

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=url_short,
                         callback=self.parse_front)


  # First parsing method
  def parse_front(self, response):
    chapter_blocks = response.css('p.course__description ol.chapter')
    #chapter_exe = response.css('')
    dc_dict = chapter_blocks
    

# Initialize the dictionary **outside** of the Spider class
#dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Description_Spider)
process.start()

# Print a preview of courses
dc_dict
#previewCourses(dc_dict)

