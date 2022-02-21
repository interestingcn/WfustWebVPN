from urllib import parse
'''
URL2WebVpn 
用于将URL链接转换为 VPN358 WebNPN代理系统链接

Author：interestingcn01@gmail.com
Date:2022.2.20

'''
class url2WebVpn():
    def __init__(self,webVpnGateWayUrl,webVpnScheme):
        self.webVpnGateWayUrl = webVpnGateWayUrl
        self.webVpnScheme = webVpnScheme

    def generateWebVpnUrl(self,url):
        # 去除结尾多余的 ’/‘
        if str(url).endswith('/'):
            url = url[:-1]
        url = parse.urlparse(url)
        if url.scheme == 'https':
            prefix = 'h-s.'
        else:
            prefix = str('')
        if url.port != 80 and url.port != None:
            prefix = prefix + 'p-' + str(url.port) + '.'
        if url.query != '':
            generateWebVpnUrl = f'{self.webVpnScheme}://{prefix}{url.hostname}.{self.webVpnGateWayUrl}{url.path}?{url.query}'
        else:
            generateWebVpnUrl = f'{self.webVpnScheme}://{prefix}{url.hostname}.{self.webVpnGateWayUrl}{url.path}'
        return generateWebVpnUrl

    def isWebVpnUrl(self,url):
        url = parse.urlparse(url)
        return str(url.netloc).endswith(self.webVpnGateWayUrl)

    def isUrl(self,url):
        url = parse.urlparse(url)
        if url.netloc == '':
            return False
        else:
            return True