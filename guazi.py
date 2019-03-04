import requests
from lxml import etree
import time,random
# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H33G987WT4CF638D"
proxyPass = "8D0ECC52011CA7D4"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxy_handler ={
    "http": proxyMeta,
    "https": proxyMeta,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'antipas=2kWa9787243x8815A93128037',
    'Host':'www.guazi.com',
    'Referer': 'https://www.guazi.com/www/buy/'
}
domain_name = 'https://www.guazi.com'

s = requests.session()
s.headers = headers
#获取响应结果返回xpath对象
def get_html(offset):

    url = 'https://www.guazi.com/www/buy/' + offset
    response = s.get(url)
    html = etree.HTML(response.text)
    return html

#返回一个可迭代对象 每一页的全部URL 40个
def get_list_url(html):

    list = html.xpath('//ul[@class="carlist clearfix js-top"]/li/a/@href')
    for eachlist in list:
        yield domain_name + eachlist

#访问details页 返回xpath对象
def get_details(url):

    time.sleep(random.randint(2, 5))
    details = s.get(url)
    doc = etree.HTML(details.content.decode('utf-8'))
    return doc

def main(offset):
    html = get_html('o'+ str(offset) +'c-1')
    list = get_list_url(html)
    a = 1
    for i in list:
        doc = get_details(i)
        print(a,doc.xpath('//title/text()'),'---标题')
        a += 1

if __name__ == '__main__':
    page = 1
    for i in range(1,51):
        print(page,'\n当前是第',page,'页')
        main(i)
        page += 1