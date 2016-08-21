# Scrapy settings for image_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'image_crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['image_crawler.spiders']
NEWSPIDER_MODULE = 'image_crawler.spiders'
ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
IMAGES_STORE = './images' 
FILES_STORE  = './files_downloaded'
