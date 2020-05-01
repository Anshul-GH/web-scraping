# -*- coding: utf-8 -*-
import scrapy
from ..items import CrudeoilpricingItem


class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    allowed_domains = ['https://www.macrotrends.net/2516/wti-crude-oil-prices-10-year-daily-chart']
    start_urls = ['https://www.macrotrends.net/2516/wti-crude-oil-prices-10-year-daily-chart']

    def parse(self, response):
        headers = response.xpath("//th/text()").getall()
        data = response.xpath("//td/text()").getall()
        
        obj = CrudeoilpricingItem()
        obj['header'] = headers
        obj['data'] = data

        formattedData = format_data(obj)

        return formattedData

    def format_data(self, obj):
        
