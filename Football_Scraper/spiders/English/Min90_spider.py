import re
import scrapy


class Min90Spider(scrapy.Spider):
    name = "90Min"
    start_urls = [
        'https://www.90min.in/top-stories?page=1',
        'https://www.90min.in/top-stories?page=2'
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'Football_Scraper.pipelines.EnglishCsvPipeline': 300,
        }
    }

    def parse(self, response):
        for title in response.css('a.feedpage-article__title::text').getall():
            yield {
                'title': re.sub(r'[^\w]', ' ', title).strip(),
            }
