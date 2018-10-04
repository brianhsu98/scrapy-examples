# Scrapy Examples

Some examples using Scrapy.

All of them scrape from [here](http://quotes.toscrape.com/)

To install the dependencies, run `pip install scrapy`, or run `pip install -r requirements.txt`.

Look inside each individual folder for a README describing the usage

## Spiders

- `all_birthdays`: Gets all the birthdays of every author on the quotes page
- `all_scientists`: By default, gets the name of all authors with the word "scientist" in their biography. Also supporst
passing in a search term.
    - Optional parameter `search_term="TERM"`
- `author_quotes`: Spider that grabs all quotes from a specific, user-supplied author.
    - Optional parameter `author=AUTHOR`
    - If author not supplied, lists all quotes
- `list_authors`: Lists all the authors
- `search_author`: Grabs all the quotes from a specific, user-supplied author. If no quotes by that author exists, 
returns a list of all authors with available quotes.
    - Required parameter `author=AUTHOR`
- `quotes_spider` and `quotes_spider_link_extractor`: Gets all quotes, authors, and tags

## Usage

- Move into the examples directory: `cd examples`
- Run a spider: `scrapy crawl SPIDER_NAME`
    - Specify an output file: `scrapy crawl SPIDER_NAME -o out.json`
    - Specify arguments: `scrapy crawl SPIDER_NAME -a ARGUMENT=VALUE`
