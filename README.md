# Scrapy Examples

Some examples using Scrapy.

All of them scrape from [here](http://quotes.toscrape.com/)

To install the dependencies, run `pip install scrapy`, or run `pip install -r requirements.txt`.

Look inside each individual folder for a README describing the usage

## Spiders

- `all_birthdays`: Gets all the birthdays of every author on the quotes apge
- `all_scientists`: By default, gets the name of all authors with the word "scientist" in their biography. Also supporst
passing in a search term.
- `author_quotes`: Spider that grabs all quotes from a specific, user-supplied author.
- `list_authors`: Lists all the authors
- `search_author`: Grabs all the quotes from a specific, user-supplied author. If no quotes by that author exists, 
returns a list of all authors with available quotes.
- `tutorial`: The tutorial, straight from the scrapy website. Grabs authors and quotes.
