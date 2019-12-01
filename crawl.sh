YEAR=$(date +%Y)
MONTH=$(date +%m)
DAY=$(date +%d)

cd /home/pi/Desktop/Football-Scraper
mkdir /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY
/home/pi/.local/bin/scrapy crawl goal -o /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY/goal.csv
/home/pi/.local/bin/scrapy crawl 90Min -o /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY/90Min.csv
/home/pi/.local/bin/scrapy crawl teamTalk -o /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY/teamTalk.csv
/home/pi/.local/bin/scrapy crawl soccerNews -o /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY/soccerNews.csv
/home/pi/.local/bin/scrapy crawl sportsLens -o /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY/sportsLens.csv
/home/pi/.local/bin/scrapy crawl oneFootball -o /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY/oneFootball.csv
cat /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY/*.csv > /home/pi/Desktop/data/Posts/$YEAR/$MONTH/$DAY/all.csv

