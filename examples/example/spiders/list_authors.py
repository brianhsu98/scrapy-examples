import scrapy

class ListAuthorsSpider(scrapy.Spider):
    name = 'list_authors'
    authors = set()

    def start_requests(self):
        start_url = "http://quotes.toscrape.com/page/1/"
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            author = quote.css('small.author::text').extract_first()
            if author in self.authors:
                continue
            self.authors.add(author)
            yield {
                'author': author
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
