# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class GsmscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HalloGsmItem(scrapy.Item):
    phoneNumber = Field()
    brandName = Field()
    modelName = Field()
    specs = Field()
