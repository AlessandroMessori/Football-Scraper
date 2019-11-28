import re
import scrapy


class TeamTalkSpider(scrapy.Spider):
    name = "teamTalk"
    start_urls = [
        'https://www.teamtalk.com/',
    ]

    def parse(self, response):
        headersQuery = "*[self::h1 or self::h2 or self::h3]"
        for title in response.xpath('//'+headersQuery+'/text()').getall():
            yield {
                'title': re.sub(r'[^\w]', ' ', title).strip(),
            }
