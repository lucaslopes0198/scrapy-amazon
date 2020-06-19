# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


class ScrapyamazonItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_author = scrapy.Field(
        input_processor=MapCompose(str.strip),
    )
    product_price = scrapy.Field()
    product_imagelink = scrapy.Field()
    pass
