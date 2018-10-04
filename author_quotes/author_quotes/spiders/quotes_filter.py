import scrapy

class QuotesFilterSpider(scrapy.Spider):
    """
    Gets quotes from a certain author, if specified. Otherwise, returns all quotes.
    """
    name = "quotes_filter"

    def start_requests(self):
        start_url = "http://quotes.toscrape.com/page/1/"
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_author = quote.css('small.author::text').extract_first()
            author = getattr(self, 'author', None)
            if author is not None:
                if quote_author != author:
                    continue
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
