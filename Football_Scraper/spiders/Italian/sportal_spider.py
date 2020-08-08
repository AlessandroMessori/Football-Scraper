import re
import scrapy


class SportalSpider(scrapy.Spider):
    name = "sportal"
    start_urls = [
        'https://www.sportal.it/calcio',
        'https://www.sportal.it/calcio/page/2'
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'Football_Scraper.pipelines.CsvPipeline': 300,
        }
    }

    def parse(self, response):
        headersQuery = ["h5 a::text","h6 a::text"]
        
        for header in headersQuery:
            for title in response.css(header).getall():
                yield {
                    'title': re.sub(r'[^\w]', ' ', title).strip(),
                }
