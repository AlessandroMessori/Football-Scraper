import re
import scrapy


class OneFootballSpider(scrapy.Spider):
    name = "oneFootball"
    start_urls = [
        'https://onefootball.com/en/top-news'
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'Football_Scraper.pipelines.CsvPipeline': 300,
        }
    }

    def parse(self, response):
        for title in response.css('span.short-title::text').getall():
            yield {
                'title': re.sub(r'[^\w]', ' ', title).strip(),
            }
