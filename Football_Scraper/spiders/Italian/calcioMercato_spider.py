import re
import scrapy


class CalcioMercatoSpider(scrapy.Spider):
    name = "calcioMercato"
    start_urls = [
        'https://www.calciomercato.com/',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'Football_Scraper.pipelines.CsvPipeline': 300,
        }
    }

    def parse(self, response):
        headersQuery = ["div.prima-pagina-articles__title::text","a.news-item__title::text","a.news-item-100min__title::text"]
        
        for header in headersQuery:
            for title in response.css(header).getall():
                yield {
                    'title': re.sub(r'[^\w]', ' ', title).strip(),
                }
