import urllib.request


class HtmlDownloader(object):
    def download(self, url):  # 传入需要下载的url
        if url is None:
            return None

        resp = urllib.request.urlopen(url)

        if resp.getcode() != 200:
            return None
        return resp.read()
