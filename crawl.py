import sys
import os
import shutil
from scrapy.crawler import CrawlerProcess

from Football_Scraper.spiders.English import *
from Football_Scraper.spiders.Italian import *

spiders = dict(english=[GoalSpider, SoccerNewsSpider, Min90Spider, SportLensSpider, TeamTalkSpider, OneFootballSpider],
               italian=[CalcioMercatoSpider, CalcioWebSpider, GazzettaSpider, SportalSpider])

if __name__ == "__main__":

    arg = sys.argv[1]

    if arg in spiders:

        shutil.rmtree('./data', ignore_errors=True)
        os.mkdir("./data")

        selected_spiders = spiders[arg]
        process = CrawlerProcess()

        print("crawling " + arg + " websites...")

        for spider in selected_spiders:
            process.crawl(spider)

        process.start()

    else:
        print("invalid language argument")
