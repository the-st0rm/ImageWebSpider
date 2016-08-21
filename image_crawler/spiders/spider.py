import scrapy
import urlparse
from image_crawler.items import ImageCrawlerItem


class ImageSpider(scrapy.Spider):
     
    name = "storm_spider"
#    allowed_domains = "starwarsccg.org"
    image_exts = [".svg", ".ico"] #['.gif', '.png', '.jpg', '.ico', '.svg', '.tiff', ' tiff', 'psd', 'jpeg', 'eps']
    allowed_exts = ['.html', '.htm', '.php', '.aspx', '.asp']
    #allowed_domains = ['tumblr.com', 'flickr.com', 'cnn.com', 'bbc.co.uk', 'bbc.com', 'twitter.com',]
    seen_urls = set()
    def __init__(self, *args, **kwargs):
        super(ImageSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get('start_url').split(",")
        print self.start_urls
        return
    #start_urls = [
    #  "http://www.starwarsccg.org/cardlists/PremiereType.html"
    #]

    def check_ext(self, exts, url):
        for ext in exts:
            if url.endswith(ext):
                return True
        return False

    def parse(self, response):
        for anchors in response.xpath('//a'):
            #self.logger.info(str(anchors))
            links = anchors.xpath('@href').extract()
            for link in links:
                link = urlparse.urljoin(response.url,link)
                #if self.check_ext(self.allowed_exts, link) and link not in self.seen_urls:
                if link not in self.seen_urls:
                    if "." not in urlparse.urlparse(link).path.split("/")[-1] or self.check_ext(self.allowed_exts, link):
                        self.seen_urls.add(link)
                        yield scrapy.Request(link, callback=self.parse)
        for imgs in response.xpath('//img'):
            links = imgs.xpath('@src').extract()
            for link in links:
                link = urlparse.urljoin(response.url,link)
                if self.check_ext(self.image_exts, link) and link not in self.seen_urls:
                    self.seen_urls.add(link)
                    cardImage = ImageCrawlerItem()
                    cardImage['file_urls'] = [link]
                    yield cardImage
