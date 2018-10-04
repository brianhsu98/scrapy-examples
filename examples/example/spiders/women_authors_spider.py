import re
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "women_authors"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            author_href = quote.css('.author + a::attr(href)').extract_first() 
            quote = {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
            request = response.follow(author_href, self.parse_author)
            request.meta['quote'] = quote
            yield request


    def parse_author(self, response):
        author_desc = response.css('.author-description::text').extract_first()
        if re.search(r'(?i)\bshe\b', author_desc):
            yield response.meta['quote']

 
