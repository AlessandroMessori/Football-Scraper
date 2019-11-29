YEAR=$(date +%Y)
MONTH=$(date +%m)
DAY=$(date +%d)

cd /home/pi/Desktop/Football-Scraper
rm -rf data
mkdir data
/home/pi/.local/bin/scrapy crawl goal -o data/goal.csv
/home/pi/.local/bin/scrapy crawl 90Min -o data/90Min.csv
/home/pi/.local/bin/scrapy crawl teamTalk -o data/teamTalk.csv
/home/pi/.local/bin/scrapy crawl soccerNews -o data/soccerNews.csv
/home/pi/.local/bin/scrapy crawl sportsLens -o data/sportsLens.csv
/home/pi/.local/bin/scrapy crawl oneFootball -o data/oneFootball.csv
cat data/*.csv > data/all.csv
/usr/local/hadoop/bin/hdfs dfs -put data/* /FootballPosts/"$YEAR/$MONTH/$DAY/"
