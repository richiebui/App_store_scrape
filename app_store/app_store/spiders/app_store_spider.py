from scrapy import Spider, Request
from app_store.items import AppStoreItem
import re


class AppStoreSpider(Spider):
    name = 'appstore_spider'
    allowed_urls = ['https://itunes.apple.com/us/genre/ios-games/id6014?mt=8']
    start_urls = ['https://itunes.apple.com/us/genre/ios-games/id6014?mt=8&letter=A&page=1#page']

    def parse(self, response):
        dic = {'A': 131, 'B': 152, 'C': 192,'D': 96, 'E': 50, 'F': 130,'G': 71, 'H':77, 'I': 29, 'J': 41, 'K': 40, 'L': 64,
        'M': 141, 'N': 36, 'O':23,'P': 125, 'Q': 11, 'R': 74,'S':226, 'T': 109, 'U': 18, 'V': 23,
        'W': 61, 'X': 6,'Y': 7, 'Z': 19}
        result_urls = ['https://itunes.apple.com/us/genre/ios-games/id6014?mt=8']
        #['https://itunes.apple.com/us/genre/ios-games/id6014?mt=8&letter={}&page={}#page'.format(k, v) for k in dic.keys() for v in range(1,dic[k])]
        for url in result_urls:
            yield Request(url=url, callback=self.parse_app)

    def parse_app(self, response):
        first_column = response.xpath('.//div[@class="column first"]/ul/li/a/@href').extract()
        middle_column = response.xpath('.//div[@class="column"]/ul/li/a/@href').extract()
        last_column = response.xpath('.//div[@class="column last"]/ul/li/a/@href').extract()

        for alink in first_column:
            yield Request(url = alink, callback=self.app_details)

        for alink in middle_column:
            yield Request(url= alink, callback=self.app_details)

        for alink in last_column:
            yield Request(url= alink, callback=self.app_details)

    def app_details(self, response):
        app_name = response.xpath('.//div/header/h1[@class="product-header__title product-header__title--app-header"]/text()').extract_first().strip()
        age_rating = response.xpath('.//div/header/h1[@class="product-header__title product-header__title--app-header"]/span/text()').extract()
        seller_name = response.xpath('.//h2[@class="product-header__identity product-header__identity--app-header product-header__identity--spaced"]/a/text()').extract()
        price = response.xpath('.//li[@class="product-header__list__item"]/ul/li/text()').extract()
        review_ratings= response.xpath('.//h3[@class="we-customer-ratings__averages"]/span/text()').extract()
        num_reviews = response.xpath('.//div[@class="we-customer-ratings__stats l-column small-4 medium-6 large-4"]/h4/text()').extract()
        app_size = response.xpath('.//div[@class="information-list__item l-row"]/dd/text()').extract()[1]
        lang = response.xpath('.//div[@class="information-list__item l-row"]/dd/@aria-label').extract()[2:]
        copy_right = response.xpath('.//div[@class="information-list__item l-row"]/dd/text()').extract()[9]
        in_app_purchases = response.xpath('.//div[@class="ember-view"]/li/span/text()').extract()
        version = response.xpath('.//div[@class]/p/text()').extract()[3]

        item = AppStoreItem()
        item['app_name'] = app_name
        item['age_rating'] = age_rating
        item['seller_name'] = seller_name
        item['price'] = price
        item['review_ratings'] = review_ratings
        item['num_reviews'] = num_reviews
        item['app_size'] = app_size
        item['lang'] = lang
        item['copy_right'] = copy_right
        item['in_app_purchases'] = in_app_purchases
        item['version'] = version
        yield item

        '''for a in alink:
            app_name = response.xpath('.//div/header/h1[@class="product-header__title product-header__title--app-header"]/text()').extract_first().strip()
            age_rating = response.xpath('.//div/header/h1[@class="product-header__title product-header__title--app-header"]/span/text()').extract()
            seller_name = response.xpath('.//h2[@class="product-header__identity product-header__identity--app-header product-header__identity--spaced"]/a/text()').extract()
            price = response.xpath('.//li[@class="product-header__list__item"]/ul/li/text()').extract()
            review_ratings= response.xpath('.//h3[@class="we-customer-ratings__averages"]/span/text()').extract()
            num_reviews = response.xpath('.//div[@class="we-customer-ratings__stats l-column small-4 medium-6 large-4"]/h4/text()').extract()
            app_size = response.xpath('.//div[@class="information-list__item l-row"]/dd/text()').extract()[1]
            lang = response.xpath('.//div[@class="information-list__item l-row"]/dd/@aria-label').extract()[2:]
            copy_right = response.xpath('.//div[@class="information-list__item l-row"]/dd/text()').extract()[9]
            in_app_purchases = response.xpath('.//div[@class="ember-view"]/li/span/text()').extract()

            item = AppStoreItem()
            item['app_name'] = app_name
            item['age_rating'] = age_rating
            item['seller_name'] = seller_name
            item['price'] = price
            item['review_ratings'] = review_ratings
            item['num_reviews'] = num_reviews
            item['app_size'] = app_size
            item['lang'] = lang
            item['copy_right'] = copy_right
            item['in_app_purchases'] = in_app_purchases

            yield item







    def parse_page(self, response):
        page_list = response.xpath('.//ul[@class="list paginate"]/li/a/@href').extract()
        for page in page_list[:5]:
            yield Request(url=page, callback=self.parse_app)

    def parse_app(self, response):
        first_column = response.xpath('.//div[@class="column first"]/ul/li/a/@href').extract()
        middle_column = response.xpath('.//div[@class="column"]/ul/li/a/@href').extract()
        last_column = response.xpath('.//div[@class="column last"]/ul/li/a/@href').extract()
        print(len(first_column))
        print(len(middle_column))
        print(len(last_column))

        for alink in first_column[:1]:
            yield Request(url = alink, callback=None)

        for alink in middle_column[:1]:
            yield Request(url= alink, callback=None)

        for alink in last_column[:1]:
            yield Request(url= alink, callback=None)

        for a in alink:
            app_name = response.xpath('.//div/header/h1[@class="product-header__title product-header__title--app-header"]/text()').extract_first().strip()
            age_rating = response.xpath('.//div/header/h1[@class="product-header__title product-header__title--app-header"]/span/text()').extract()
            seller_name = response.xpath('.//h2[@class="product-header__identity product-header__identity--app-header product-header__identity--spaced"]/a/text()').extract()
            price = response.xpath('.//li[@class="product-header__list__item"]/ul/li/text()').extract()
            review_ratings= response.xpath('.//h3[@class="we-customer-ratings__averages"]/span/text()').extract()
            num_reviews = response.xpath('.//div[@class="we-customer-ratings__stats l-column small-4 medium-6 large-4"]/h4/text()').extract()
            app_size = response.xpath('.//div[@class="information-list__item l-row"]/dd/text()').extract()[1]
            lang = response.xpath('.//div[@class="information-list__item l-row"]/dd/@aria-label').extract()[2:]
            copy_right = response.xpath('.//div[@class="information-list__item l-row"]/dd/text()').extract()[9]
            in_app_purchases = response.xpath('.//div[@class="ember-view"]/li/span/text()').extract()

            item = AppStoreItem
            item['app_name'] = app_name
            item['age_rating'] = age_rating
            item['seller_name'] = seller_name
            item['price'] = price
            item['review_ratings'] = review_ratings
            item['num_reviews'] = num_reviews
            item['app_size'] = app_size
            item['lang'] = lang
            item['copy_right'] = copy_right
            item['in_app_purchases'] = in_app_purchases

            yield item'''
