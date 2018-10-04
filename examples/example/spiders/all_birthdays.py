import scrapy
import re

class AllBirthdaysSpider(scrapy.Spider):
    name = "all_birthdays"

    def start_requests(self):
        start_url = "http://quotes.toscrape.com/page/1/"
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        author = response.css('h3.author-title::text').extract_first().strip()
        birthday = response.css('.author-born-date::text').extract_first()
        yield {
            'author': author,
            'birthday' : birthday
        }
