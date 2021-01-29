import scrapy
from urllib.parse import urljoin
from magazine_spider.items import Magazine

class MagazineSpider(scrapy.Spider):
    name = 'covers'

    start_urls = ["http://www.coverbrowser.com/covers/wolverine"]

    def parse(self, response):
        image_urls = response.css('p.cover img::attr(src)').getall()
        for image_url in image_urls:
            item = Magazine()
            item['image_urls'] = [response.urljoin(image_url)]
            yield item        

        page_links = response.css('p.issuesNavigationBottom a::attr(href)').getall()
        next_page = page_links[-1]
        yield response.follow(next_page, callback=self.parse)