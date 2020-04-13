import scrapy
import pymysql
from bigchuang.items import policyItem
# cd myproject/bigchuang
# scrapy crawl bigchuangpo


class PolicySpider(scrapy.Spider):
    name = "bigchuangpo"
    # allowed_domains = ["http://www.chinapolicy.net"]
    start_urls = [
        'http://www.chinapolicy.net/list.php?fid-67-page-1.htm',
    ]

    def parse(self, response):
        url = "http://www.chinapolicy.net/"

        for policy in response.xpath('//*[@id="list_article"]/tr[2]/td/table/tr'):
            href = policy.xpath('td/span[1]/a/@href').getall()
            strr = "".join(href)
            new_url = url+strr

            if (new_url == url):
                continue

            timee = policy.xpath('td/span[2]/text()').getall()
            timee = "".join(timee).replace('(', '').replace(')', '')
            # print(time)
            items = policyItem()
            items['timee'] = timee

            yield scrapy.Request(new_url, callback=self.parse2, meta={'items': items})

        next_url = response.xpath(
            '//*[@id="list_article"]/tr[2]/td/div/a[10]/@href').getall()
        next_url = 'http://www.chinapolicy.net/'+("".join(next_url))
        # print(response.request.url)
        # print(next_url)
        if (response.request.url != next_url):
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse2(self, response):
        items = response.meta['items']
        for para in response.xpath('//*[@id="view_article"]/tr[2]/td'):
            title = para.xpath('div[@class="main_title"]/text()').get()
            title = "".join(title)
            # print(title)
            items['title'] = title

            articles = para.xpath('//*[@id="post1"]/p/font/text()').getall()
            if articles == []:
                articles = para.xpath(
                    '//*[@id="post1"]/p/font/font/span[1]/text()').getall()
            articles = "".join(articles)
            # print(articles)
            items['articles'] = articles

            return items
