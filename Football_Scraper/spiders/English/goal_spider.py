import re
import scrapy


class GoalSpider(scrapy.Spider):
    name = "goal"
    start_urls = [
        'https://www.goal.com/en?ICID=HP',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'Football_Scraper.pipelines.CsvPipeline': 300,
        }
    }

    def parse(self, response):
        for title in response.css('h3::text').getall():
            yield {
                'title': re.sub(r'[^\w]', ' ', title).strip(),
            }
