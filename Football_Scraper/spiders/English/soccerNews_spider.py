import re
import scrapy


class SoccerNewsSpider(scrapy.Spider):
    name = "soccerNews"
    postsLength = 40
    minPostChars = 35
    start_urls = ['https://www.soccernews.com/headlines/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'Football_Scraper.pipelines.CsvPipeline': 300,
        }
    }

    def parse(self, response):
        titles = filter( lambda x: (len(x) > self.minPostChars)  , response.css('a::text').getall())
        titles = list(titles)[:self.postsLength]
        print(titles)
        for title in titles:
            yield {
                'title': re.sub(r'[^\w]', ' ', title).strip(),
            }
