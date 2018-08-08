# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppStoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    app_name = scrapy.Field()
    age_rating = scrapy.Field()
    seller_name = scrapy.Field()
    price = scrapy.Field()
    review_ratings= scrapy.Field()
    num_reviews = scrapy.Field()
    app_size = scrapy.Field()
    lang = scrapy.Field()
    copy_right = scrapy.Field()
    in_app_purchases = scrapy.Field()
    version = scrapy.Field()
