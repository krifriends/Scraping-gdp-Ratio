# -*- coding: utf-8 -*-
import scrapy
import logging

class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['https://worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("(//table[@class='datatableStyles__StyledTable-bwtkle-1 cyosFW table table-striped'])/tbody/tr")
        for row in rows:
            countryName = row.xpath(".//td[1]/a/text()").get()
            debtRatio = row.xpath("./td[2]/text()").get()
            yield{
                'countries':countryName,
                'debt-ratio':debtRatio
            }