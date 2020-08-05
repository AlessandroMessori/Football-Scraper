import re
import scrapy


class GoalSpider(scrapy.Spider):
    name = "goal"
    start_urls = [
        'https://www.goal.com/en?ICID=HP',
    ]

    def parse(self, response):
        for title in response.css('h3::text').getall():
            yield {
                'title': re.sub(r'[^\w]', ' ', title).strip(),
            }
