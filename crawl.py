import sys
import os
from scrapy.crawler import CrawlerProcess

from Football_Scraper.spiders.Italian import *
from Football_Scraper.spiders.English import *

spiders = dict(english=[GoalSpider, SoccerNewsSpider, Min90Spider, SportLensSpider, TeamTalkSpider, OneFootballSpider],
               italian=[CalcioMercatoSpider, CalcioWebSpider, GazzettaSpider, SportalSpider])

if __name__ == "__main__":

    arg = sys.argv[1]
    path = sys.argv[2]

    if arg in spiders:

        write_file_path = path + arg + '.csv'

        if os.path.exists(write_file_path):
            os.remove(write_file_path)

        selected_spiders = spiders[arg]
        process = CrawlerProcess()

        print("crawling " + arg + " websites...")

        for spider in selected_spiders:
            process.crawl(spider)

        process.start()

    else:
        print("invalid language argument")
