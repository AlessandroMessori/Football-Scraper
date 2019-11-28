import re
import scrapy


class Min90Spider(scrapy.Spider):
    name = "oneFootball"
    start_urls = [
        'https://onefootball.com/en/top-news'
    ]

    def parse(self, response):
        for title in response.css('span.short-title::text').getall():
            yield {
                'title': re.sub(r'[^\w]', ' ', title).strip(),
            }
