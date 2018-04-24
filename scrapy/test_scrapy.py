import logging
import scrapy
from twisted.internet import reactor, defer
from twisted.python.failure import Failure
from sp_ads.utils.async_tools import wget_async
from scrapy.exceptions import DropItem

logger = logging.getLogger(__name__)

class TestItem(object):

    def process_item(self, item, spider):
        print('process_item', item)

        out = defer.Deferred()
        reactor.callInThread(self.process_item_thread, item, out)
        return out

    def process_item_thread(self, item, out):
        reactor.callFromThread(out.errback, Failure(DropItem(item)))
        #raise DropItem(item)
        #reactor.callFromThread(out.callback, {'111':111})

class TestItem2(object):
    def process_item(self, item, spider):
        print('process_item2', item)

class TestSpider(scrapy.Spider):
    name = 'test'
    custom_settings = {
        'ITEM_PIPELINES': {
            # "sp_ads.pipelines.resource_conversion.ResourceConversionPipline": None,
            # "sp_ads.pipelines.etl_unique.EtlUniquePipline": None,
            # "sp_ads.pipelines.save_unique_relation.SaveUniqueRelationPipline": None,
            # "sp_ads.pipelines.send_message.SendMessagePipline": None,
            "sp_ads.spiders.test.TestItem": 990,
            "sp_ads.spiders.test.TestItem2": 999,
        }
    }

    DOWNLOADER_MIDDLEWARES = {
        "sp_ads.downloadermiddlewares.proxy_middleware.ProxyMiddleware": None,
        # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
        # downloader
    }

    # SPIDER_MIDDLEWARES = {
    #     'sp_ads.spidermiddlewares.feedback.Feedback': None,
    #     # spider
    # }

    # EXTENSIONS = {
    #     'scrapy.extensions.telnet.TelnetConsole': None,
    #     'sp_ads.extensions.log_monitor.ScrapyCrawlLogMonitorExtensions': None,
    #     'sp_ads.extensions.crawl_monitor.ScrapyDailyCrawlMonitorExtensions': None,
    #     # load later
    # }

    def start_requests(self):
        while 1:
            #yield scrapy.Request('https://lumtest.com/myip.json', meta={"proxy_class": VpUserProxy})
            # yield scrapy.Request('https://lumtest.com/myip.json', meta={"aa":1}, dont_filter=True)
            # yield scrapy.Request('https://lumtest.com/myip1.json', meta={"aa":2}, dont_filter=True)
            yield scrapy.Request('https://lumtest.com/myip.json', meta={"aa":3}, callback=self.parse, errback=self.error_back, dont_filter=True)
            break

    #@defer.inlineCallbacks
    def parse(self, response):
        logger.error('fdfa', extra={"spider":self})
        print('rep', response.text, response.meta)
        d = wget_async(response.url)
        d.addBoth(self.result)
        return d
        #print(response.request.headers, response.meta, r)

    def result(self, r):
        yield {"b": r.body}
        yield {"b": r.body}
        #raise RuntimeError()

    def error_back(self, f):
        if isinstance(f, Exception):
            f =  Failure(f)

        if isinstance(f, Failure):
            print({
                'err': f.value,
                'stack': f.stack
            })

        else:
            print('Unknown f %s' % repr(f))

# @defer.inlineCallbacks
# def get_url_content(url):
#     def _md5(url, cb):
#         time.sleep(10)
#         r = requests.get(url)
#         cb.callback(r.content)
#     d = defer.Deferred()
#     reactor.callInThread(_md5, url=url, cb=d)
#     r = yield d
#     return r


# def call_in_thread(f):
#     @wraps(f)
#     def _wrapped(*args, **kwargs):
#         d = defer.Deferred()
#         reactor.callInThread(f, cb=d, *args, **kwargs)
#         r = yield d
#         return r
#     return _wrapped
#
# @defer.inlineCallbacks
# @call_in_thread
# def _md5(url, cb):
#     try:
#         time.sleep(10)
#         r = requests.get(url)
#         cb.callback('1111')
#     except Exception as err:
#         # prevent not errback and stuck!!!
#         cb.errback(err)

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl test".split())
