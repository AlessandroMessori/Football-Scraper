import re
import scrapy


class CalcioWebSpider(scrapy.Spider):
    name = "calcioWeb"
    start_urls = ['https://www.calcioweb.eu/']

    def parse(self, response):
        headersQuery = ["h4.side-title-post a::text"]
        
        for header in headersQuery:
            for title in response.css(header).getall():
                yield {
                    'title': re.sub(r'[^\w]', ' ', title).strip(),
                }
