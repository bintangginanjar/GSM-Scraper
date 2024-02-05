import scrapy

class InponselSpider(scrapy.Spider):
    name = 'inponsel'

    BASE_URL = 'https://www.inponsel.com/'

    def start_requests(self):        
        self.logger.info('Start request Inponsel')

        targetUrl = self.BASE_URL + 'brand'

        yield scrapy.Request(url=targetUrl, callback=self.parse)

    def parse(self, response):
        self.logger.info('Parse Inponsel')

        self.logger.info(response.body)