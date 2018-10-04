# All Scientists

A scraper that finds the names of all the scientists -- basically, scans the biography for the word "scientist"

Alternatively, the spider allows for passing in an argument `search_term`, allowing you to scan for all the authors 
with `seach_term` in their biography.

## Usage

- `scrapy crawl all_scientists -o out.json`
- `scrapy crawl all_scientists -o out.json -a search_term="American"`