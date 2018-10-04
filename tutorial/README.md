# Scrapy Tutorial
The tutorial from [here](https://docs.scrapy.org/en/latest/intro/tutorial.html)

## Spiders
There are two spiders here, both of which pretty much just crawl the website for quotes and output them. The first one uses explicitly stated URLs, while the second follows the pagination links.

Run them with `scrapy crawl quotes` and `spacy crawl quotes_follow`.

Append the argument `-o out.json` to output the results to a JSON file, like this: `scrapy crawl quotes -o out.json`
