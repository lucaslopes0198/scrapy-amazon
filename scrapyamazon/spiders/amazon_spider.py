# # -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyamazonItem
from scrapy.loader import ItemLoader

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011%2Cp_n_feature_browse-bin%3A618073011&dc&page={}&fst=as%3Aoff&qid=1588099537&rnid=618072011&ref=sr_pg_2'.format(i) for i in range(1, 101)]

    def parse(self, response):
        items = ItemLoader(item=ScrapyamazonItem())

        all_div_quotes = response.css('div.a-section.a-spacing-medium')

        for quote in all_div_quotes:
            product_name = quote.css('.a-color-base.a-text-normal::text').extract()
            product_author = quote.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
            product_price = quote.css('.a-spacing-top-small .a-price:nth-child(1) span.a-offscreen').css('::text').extract()
            product_imagelink = quote.css('.s-image::attr(src)').extract()
            
            items.replace_value('product_name', product_name)
            items.replace_value('product_author', product_author)
            items.replace_value('product_price', product_price)
            items.replace_value('product_imagelink', product_imagelink)

            yield items.load_item()


# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyamazonItem
from scrapy.loader import ItemLoader

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    base_url = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011%2Cp_n_feature_browse-bin%3A618073011&dc&page={page}&fst=as%3Aoff&qid=1588099537&rnid=618072011&ref=sr_pg_2'
		
    def start_requests(self):
        yield scrapy.Request(
        url='https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011%2Cp_n_feature_browse-bin%3A618073011&dc&page=1&fst=as%3Aoff&qid=1588099537&rnid=618072011&ref=sr_pg_2',
        callback=self.parse_pages
        )
    
    def parse_pages(self, response):
        total_pages = int(response.css('li+ .a-disabled::text').extract_first())
        
        for page in range(1, total_pages):
            next_page = page
            url = self.base_url.format(page=next_page)
            yield response.follow(url, callback=self.parse)
    
    def parse(self, response):
        items = ItemLoader(item=ScrapyamazonItem())

        all_div_quotes = response.css('div.a-section.a-spacing-medium')

        for quote in all_div_quotes:
            product_name = quote.css('.a-color-base.a-text-normal::text').extract()
            product_author = quote.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
            product_price = quote.css('.a-spacing-top-small .a-price:nth-child(1) span.a-offscreen').css('::text').extract()
            product_imagelink = quote.css('.s-image::attr(src)').extract()
            
            items.replace_value('product_name', product_name)
            items.replace_value('product_author', product_author)
            items.replace_value('product_price', product_price)
            items.replace_value('product_imagelink', product_imagelink)

            yield items.load_item()
