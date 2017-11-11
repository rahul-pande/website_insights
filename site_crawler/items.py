# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchResult(scrapy.Item):
    # define the fields for your item here like:
    thread_title = scrapy.Field()
    thread_id = scrapy.Field()

    # forum_category = scrapy.Field()
    # forum_category_id = scrapy.Field()

    # views = scrapy.Field()
    # author = scrapy.Field()
    # created_at = scrapy.Field()
    # modified_at = scrapy.Field()
    pass
