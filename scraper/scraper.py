from scrapy.crawler import CrawlerProcess, Spider
from dbConnector import *
import json

ELEMENTS_PER_PAGE = 20
PAGES_TO_LOAD = 1 

# Using scrapy here is somewhat unnecessary since the data is already in a computer readable format
class FlatSpider(Spider):
    name = 'flatSpider'
    start_urls = [f"https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page={str(ELEMENTS_PER_PAGE)}&page={i}" for i in range(1, PAGES_TO_LOAD + 1)]

    custom_settings = {
        'FEED_EXPORT_ENCODING' : 'utf-8',
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'AUTOTHROTTLE_ENABLED' : True,
        'AUTOTHROTTLE_START_DELAY' : 12,
        'AUTOTHROTTLE_MAX_DELAY' : 20
    }

    def parse(self, res):
        for estate in json.loads(res.text)["_embedded"]["estates"]:
            yield {
                'id': estate["hash_id"],
                'name': estate["name"],
                'price': estate["price_czk"]["value_raw"],
                'location': estate["locality"],
                'image_urls': [image["href"] for image in estate["_links"]["images"]],
            }

# Run crawler
process = CrawlerProcess(settings={
    "FEEDS" : {
            "listings.json" : {"format": "json"}
    }
})
process.crawl(FlatSpider)
process.start()

# Copy scraped listings to the database
with open("listings.json", "r", encoding="utf-8") as f:
    listings = json.load(f)

conn = db_connect()
for listing in listings:
    db_insert(conn, listing["id"], listing["name"], listing["price"], listing["location"], ''.join([item + ";" for item in listing["image_urls"]])[0:-1])
conn.commit()