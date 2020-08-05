YEAR=$(date +%Y)
MONTH=$(date +%m)
DAY=$(date +%d)

cd /home/alessandro/Scrivania/Repos/Football-Scraper
rm -rf data
mkdir data
scrapy crawl goal -o data/goal.csv
scrapy crawl 90Min -o data/90Min.csv
scrapy crawl teamTalk -o data/teamTalk.csv
scrapy crawl soccerNews -o data/soccerNews.csv
scrapy crawl sportsLens -o data/sportsLens.csv
scrapy crawl oneFootball -o data/oneFootball.csv
cat data/*.csv > data/all.csv
#/usr/local/hadoop/bin/hdfs dfs -put data/* /FootballPosts/"$YEAR/$MONTH/$DAY/"
