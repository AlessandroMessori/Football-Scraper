import re
import scrapy


class GazzettaSpider(scrapy.Spider):
    name = "gazzetta"
    start_urls = ["https://www.gazzetta.it/Calcio/"]
    custom_settings = {
        'ITEM_PIPELINES': {
            'Football_Scraper.pipelines.CsvPipeline': 300,
        }
    }

    def parse(self, response):
        headersQuery = ["a.has-text-black::text"]
        
        for header in headersQuery:
            for title in response.css(header).getall():
                yield {
                    'title': re.sub(r'[^\w]', ' ', title).strip(),
                }
