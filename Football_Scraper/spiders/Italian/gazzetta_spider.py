import re
import scrapy


class SportalSpider(scrapy.Spider):
    name = "gazzetta"
    start_urls = ["https://www.gazzetta.it/Calcio/"]

    def parse(self, response):
        headersQuery = ["a.has-text-black::text"]
        
        for header in headersQuery:
            for title in response.css(header).getall():
                yield {
                    'title': re.sub(r'[^\w]', ' ', title).strip(),
                }
