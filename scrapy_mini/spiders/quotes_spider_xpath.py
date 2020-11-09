import scrapy

class QuotesSpiderXPath(scrapy.Spider):
    name = "toscrape-xpath"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').get(),
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('./div[@class="tags"]//a[@class="tag"]/text()').getall(),
            }

        next_page = response.xpath('//li[@class="next"]/a/attribute::href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)