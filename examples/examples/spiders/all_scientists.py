import scrapy
import re

class AllScientistsSpider(scrapy.Spider):
    name = "all_scientists"

    def start_requests(self):
        start_url = "http://quotes.toscrape.com/page/1/"
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        bio = response.css('.author-description::text').extract_first()
        search_term = getattr(self, 'search_term', None)

        # Defaults to searching for scientists
        if search_term is None:
            search_term = "scientist"
        if search_term is not None:
            search_results = re.findall(search_term, bio, re.IGNORECASE)
            if len(search_results) != 0:
                yield {
                    'author': response.css('h3.author-title::text').extract_first().strip()
                }