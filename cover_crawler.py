import scrapy
import re

class MagazineSpider(scrapy.Spider):
    name = 'covers'

    start_urls = ["http://www.coverbrowser.com/covers/wolverines"]

    def parse(self, response):
        #retrive all covers and titles on the current page
        covers = response.css('p.cover img::attr(src)').getall()
        titles = response.css('p.cover img::attr(alt)'),getall()

        #create a dict with 'title' : cover structure
        collection = {}
        for cover, title in zip(covers, titles):
            collection[title] = cover

        yield colleciton 

    #the response.css('p.cover') reutrns a string. code below uses regex to extract the title
    """def parse(self, response):
        for cover in response.css('p.cover').get():
            title = re.findall('alt="(.+)" t', cover)
            yield {
                'title' : title[0]
            }"""
        
        #grab all page links, select the last one (the next button), navigate to that page
        page_links = response.css('p.issuesNavigationBottom a::attr(href)').getall()
        next_page = page_links[-1]
        yield response.follow(next_page, callback=self.parse)