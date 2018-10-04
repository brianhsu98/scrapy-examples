import scrapy

class SearchAuthorSpider(scrapy.Spider):
    name = "search_author"
    authors = set()
    author_found = False

    def start_requests(self):
        if getattr(self, "author", None) is None:
            raise Exception("Please supply an author name")
        start_url = "http://quotes.toscrape.com/page/1/"
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_author = quote.css('small.author::text').extract_first()
            self.authors.add(quote_author)
            author = getattr(self, 'author', None)
            if quote_author != author:
                continue
            else:
                self.author_found = True
                yield {
                    'text': quote.css('span.text::text').extract_first(),
                    'author': quote.css('small.author::text').extract_first(),
                    'tags': quote.css('div.tags a.tag::text').extract(),
                }

        next_page = response.css('li.next a::attr(href)').extract_first()

        # If all the pages have been looked through
        if next_page is None:
            if not self.author_found:
                yield {
                    'possible_authors': self.authors
                }
        else:
            yield response.follow(next_page, self.parse)
