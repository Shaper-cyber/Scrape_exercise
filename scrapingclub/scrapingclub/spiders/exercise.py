import scrapy
from scrapy.http import HtmlResponse


class ExerciseSpider(scrapy.Spider):
    name = 'exercise'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    def parse(self, response: HtmlResponse):
        link_item = response.xpath("//div[@class='card']/a/@href").get()
        if link_item:
            press_link_item = response.urljoin(link_item)
            yield scrapy.Request(
                url=press_link_item,
                callback=self.parse
            )
