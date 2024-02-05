import scrapy

from gsmscraper.items import HalloGsmItem

class HalloGsmSpider(scrapy.Spider):
    name = 'hallogsm'    

    BASE_URL = 'https://www.hallogsm.com/'

    phoneNumber = 0

    def start_requests(self):        
        self.logger.info('Start request Inponsel')

        targetUrl = self.BASE_URL + 'hp'

        yield scrapy.Request(url=targetUrl, callback=self.parseHome)

    def parseHome(self, response):
        self.logger.info('Parse Home')

        #self.logger.info(response.css('div.aps-brands-box > ul.aps-brands-body > li > a::attr(href)').getall())

        urlList = response.css('div.aps-brands-box > ul.aps-brands-body > li > a::attr(href)').getall()

        for url in urlList:            
            #self.logger.info(url)
            yield scrapy.Request(url=url, callback=self.parsePhoneList)

    def parsePhoneList(self, response):   
        self.logger.info('Parse Phone List')

        urlList = response.css('ul.aps-products > li > div.aps-product-box > div.aps-product-thumb > a::attr(href)').getall()        

        for url in urlList:
            #self.logger.info(url)
            yield scrapy.Request(url=url, callback=self.parsePhone)

        nextPage = response.css('div.aps-pagination > a::attr(href)').get()

        if nextPage:
            yield response.follow(nextPage, callback=self.parsePhoneList)


    def parsePhone(self, response):
        self.logger.info('Parse Phone')
        phoneInfo = {}

        olList = response.css('div.aps-content > ol.apscrumbs > li')        
    
        brandName = ''
        modelName = ''
        olNum = 0

        for ol in olList:
            #self.logger.info(ol.css('a > span::text').extract())            
            if olNum == 2:
                #self.logger.info(ol)                
                brandName = ol.css('a > span::text').get()
                #phoneInfo['Brand'] = ol.css('a > span::text').get()
                #self.logger.info(brandName)
            elif olNum == 3:
                #self.logger.info(ol)                
                modelName = ol.css('span::text').get()
                #phoneInfo['Model'] = ol.css('span::text').get()
                #self.logger.info(modelName)            

            olNum = olNum + 1

        category = response.css('span.aps-product-cat > a::text').get()
        #self.logger.info(category)

        rowList = response.css('div.aps-column > div.aps-group')

        for row in rowList:
            mainKey = row.css('h3::text').get()
            mainKey = ''.join(mainKey.split())
            #self.logger.info(mainKey)
            phoneInfo[mainKey] = {}

            trList = row.css('table.aps-specs-table > tbody > tr')

            for tr in trList:
                subKey = tr.css('td.aps-attr-title > span.aps-attr-co > strong.aps-term::text').get()
                                
                #subKey = ''.join(subKey.split())
                #self.logger.info(subKey)

                rowVal = tr.css('td.aps-attr-value > span::text').get()
                #self.logger.info(rowVal)

                phoneInfo[mainKey][subKey] = rowVal

                #self.logger.info(phoneInfo)

        phone = HalloGsmItem()
        phone['phoneNumber'] = self.phoneNumber
        phone['brandName'] = brandName
        phone['modelName'] = modelName
        phone['specs'] = []
        phone['specs'].append(phoneInfo)

        self.phoneNumber = self.phoneNumber + 1

        yield phone

        phoneInfo.clear()