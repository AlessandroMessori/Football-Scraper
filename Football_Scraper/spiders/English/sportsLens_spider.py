import re
import scrapy


class SportLensSpider(scrapy.Spider):
    name = "sportsLens"
    start_urls = [
        'https://sportslens.com',
        'https://sportslens.com/page/2/'
    ]

    def parse(self, response):
        for title in response.css('.title>a::text').getall():
            yield {
                'title': re.sub(r'[^\w]', ' ', title).strip(),
            }
