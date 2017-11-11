import scrapy
from urlparse import urljoin

class KaskusSpider(scrapy.Spider):
    name = "kaskus_bot"
    base_url = 'https://www.kaskus.co.id'

    def __init__(self, search_term='new', *args, **kwargs):
        super(KaskusSpider, self).__init__(*args, **kwargs)
        self.search_text = search_term.replace(',', '+')

    def start_requests(self):
        urls = [
            urljoin(self.base_url, '/search/forum?q={}'.format(self.search_text)),
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_search_results)

    def parse_search_results(self, response):
        thread_links = response.xpath("//tbody/tr/td/div[@class='post-title']/a/@href").extract()

        for link in thread_links:
            yield scrapy.Request(url=link, callback=self.parse_thread, meta = {'thread_link' : link})

        next_result_page = response.xpath('//ul[@class="pagination pull-right"]/li/a[@data-original-title="Next Page"]/@href').extract_first()

        if next_result_page is not None:
            yield scrapy.Request(url=urljoin(self.base_url, next_result_page), callback=self.parse_search_results)

    def parse_thread(self, response):
        thread_link = 'None'
        try:
            thread_link = response.meta['thread_link']
        except:
            print response.url

        posts = zip(
            response.xpath('//div[@class="entry"]'),
            response.xpath('//div[@class="entry-head bar0"]')
        )

        for item in posts:
            text = ''.join(item[0].xpath('.//text()').extract())
            post_number = ''.join(item[1].xpath('./div/div[@class="permalink"]/a/@name').extract())

            yield {
                'thread' : thread_link,
                'post_number':post_number,
                'text' : text
            }

        next_comment_page = response.xpath('//ul[@class="pagination"]/li/a[@title="Next Page"]/@href').extract_first()

        # yield response.follow(next_comment_page, self.parse_thread, meta = {'thread_link' : thread_link})

        yield scrapy.Request(url=urljoin(self.base_url, next_comment_page), callback=self.parse_thread, meta = {'thread_link' : thread_link})

