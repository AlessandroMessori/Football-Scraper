import json
import os
import shutil
from scrapy.crawler import CrawlerProcess

from Football_Scraper.spiders.Italian import *
from Football_Scraper.spiders.English import *

spiders = dict(english=[GoalSpider, SoccerNewsSpider, Min90Spider, SportLensSpider, TeamTalkSpider, OneFootballSpider],
               italian=[CalcioMercatoSpider, CalcioWebSpider, GazzettaSpider, SportalSpider])

if __name__ == "__main__":
    with open('/usr/local/airflow/config.json', 'r') as f:
        config = json.load(f)
        languages = config["languages"]
        path = '/usr/local/airflow/data'

        if os.path.exists(path):
            shutil.rmtree(path)

        os.mkdir(path)

        for lan in languages:

            write_file_path = path + lan["name"] + '.csv'

            selected_spiders = spiders[lan["name"]]
            process = CrawlerProcess()

            print("crawling " + lan["name"] + " websites...")

            for spider in selected_spiders:
                process.crawl(spider)

        process.start()
