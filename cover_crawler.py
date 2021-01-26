import scrapy
from magazine_spider.items import MagazineCover

class MagazineSpider(scrapy.Spider):
    name = 'covers'

    start_urls = ["http://www.coverbrowser.com/covers/wolverines"]

    def parse(self, response):
        for cover in response.css('p.cover'):
            yield{
                'title' : cover.css('img::attr(alt)').get(),
                'cover' : cover.css('img::attr(src)').get()
            }

        page_links = response.css('p.issuesNavigationBottom a::attr(href)').getall()
        next_page = page_links[-1]
        yield response.follow(next_page, callback=self.parse)
