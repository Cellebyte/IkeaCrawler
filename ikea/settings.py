# Scrapy settings for ikea project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ikea'

SPIDER_MODULES = ['ikea.spiders']
NEWSPIDER_MODULE = 'ikea.spiders'
COOKIES_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'ikea (+https://couch.cellebyte.de)'

LOG_FILE = 'scrapyOperation.log'
CONCURRENT_REQUESTS_PER_DOMAIN = 3
LOG_LEVEL = 'INFO'
RETRY_ENABLED = False
CONCURRENT_SPIDERS = 3
