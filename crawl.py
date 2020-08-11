import sys
import os
from scrapy.crawler import CrawlerProcess

from Football_Scraper.spiders.English import *
from Football_Scraper.spiders.Italian import *

spiders = dict(english=[GoalSpider, SoccerNewsSpider, Min90Spider, SportLensSpider, TeamTalkSpider, OneFootballSpider],
               italian=[CalcioMercatoSpider, CalcioWebSpider, GazzettaSpider, SportalSpider])

if __name__ == "__main__":

    arg = sys.argv[1]

    if arg in spiders:

        write_file_path = '/home/alessandro/Scrivania/data/' + arg + '.csv'

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
