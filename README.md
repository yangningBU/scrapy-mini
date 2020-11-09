# Scrapy Mini Project 5.5.3
Two methods of scraping identical site [Quotes](http://quotes.toscrape.com), one using CSS selectors one using XPath

### Method
I ran the following commands to generate the JSON files here:
```
scrapy crawl toscrape-css -o css-scraper-results.json
scrapy crawl toscrape-xpath -o xpath-scraper-results.json
```

The spiders are in the spiders directory.