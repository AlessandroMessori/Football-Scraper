cd /home/alessandro/Scrivania/Repos/Football-Scraper
rm -rf data
mkdir data
scrapy crawl calcioMercato -o data/calcioMercato.csv
scrapy crawl sportal -o data/sportal.csv
scrapy crawl calcioWeb -o data/calcioWeb.csv
scrapy crawl gazzetta -o data/gazzetta.csv
cat data/*.csv > data/all.csv