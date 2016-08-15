class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:  # 判断url
            return
        if url not in self.new_urls and url not in self.old_urls:  # 判断url既不在待爬去的url列表中也不再已经爬取过的url中
            self.new_urls.add(url)  # 添加url

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)  # 添加url

    def has_new_url(self):  # 判断是否有新的url
        return len(self.new_urls) != 0  # 如果长度不是0,就表示有正在爬取的url

    def get_new_url(self):  # 获取正在爬取的url
        new_url = self.new_urls.pop()  # pop可以在列表中获取一个url,并且移除这个url
        self.old_urls.add(new_url)
        return new_url
