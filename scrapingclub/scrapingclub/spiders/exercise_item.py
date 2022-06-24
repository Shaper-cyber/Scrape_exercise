from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse


class ExerciseItemSpider(CrawlSpider):
    name = 'exercise_item'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='card']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[contains(text(), 'Next')]"), follow=True),
    )

    @staticmethod
    def parse_item(response: HtmlResponse):
        item = {
            'name': response.xpath("//img[contains(@class, 'card-img-top')]/following-sibling::div/h3/text()").get(),
            'description': response.xpath(
                "//img[contains(@class, 'card-img-top')]/following-sibling::div/p/text()").get(),
            'image': response.urljoin(response.xpath("//img[contains(@class, 'card-img-top')]/@src").get()),
            'price': response.xpath("//img[contains(@class, 'card-img-top')]/following-sibling::div/h4/text()").get()}
        return item
