import scrapy

class SearchAuthorSpider(scrapy.Spider):
    # Given an author, return all quotes by that author.
    # If the author is not found, return a list of authors.
    name = "search_author"

    def start_requests(self):
        self.all_authors = set()
        self.target_author_found = False

        if getattr(self, "target_author", None) is None:
            raise Exception("Please supply a target_author name")
        self.target_author = getattr(self, 'target_author', None)

        start_url = "http://quotes.toscrape.com/page/1/"
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        # Handle all quotes on the current page.
        for quote in response.css('div.quote'):
            quote_author = quote.css('small.author::text').extract_first()
            self.all_authors.add(quote_author)

            if quote_author == target_author:
                self.target_author_found = True
                yield {
                    'text': quote.css('span.text::text').extract_first(),
                    'author': quote.css('small.author::text').extract_first(),
                    'tags': quote.css('div.tags a.tag::text').extract(),
                }

        # Look at the next page.
        next_page = response.css('li.next a::attr(href)').extract_first()

        # If all the pages have been looked through.
        # Note: We can assume the pages are in order only because each page
        # can only be enqueued by the previous one.
        if next_page is None:
            if not self.target_author_found:
                yield {
                    'possible_authors': self.all_authors
                }
        else:
            yield response.follow(next_page, self.parse)


# Pass at pseud-code description.
# Import necessary libraries

# Initialize spider class
#   Set unique name of spider

#   Define the function to start requests
#     Create container for authors found so far
#     Create checker if the target author has ever been found
#     Create a variable for the target author

#     If the target author isn’t specified
#       Raise an error to define the target author

#     initialize URL to start at
#     Scrape the start URL

#   Define the function to parse a response
#     For every quote on the page
#       Create a variable for the quote author
#       Add to the authors found so far

#       If the quote author is the target author
#         Mark that the target author has been found
#         Yield quote metadata

#     Create a variable with the link to the next page

#     If this is the final page
#       If the target author wasn’t present
#         Yield the full set of authors
#     If this is not the final page
#       Move on to the next page
#       
