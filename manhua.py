import requests
from lxml import etree
url = 'https://www.manhuadb.com/manhua/126' #漫画列表地址
def get_html(url):
    html = requests.get(url).text
    doc = etree.HTML(html)
    list = doc.xpath('//ol[@class="links-of-books num_div"]/li[contains(@class,"sort_div")]/a/@href')
    print(len(list),type(list))
    return list


#获取图片地址
def get_img(list):
    answer = 1
    url = 'https://www.manhuadb.com/'
    for i in list:
        sonurl = url + i
        html = requests.get(sonurl).text
        node = etree.HTML(html)
    # 获取这一回全部的图片地址
        node_next = node.xpath('//div[@class="pagination px-2 py-3 justify-content-center"][1]//div[@class="mx-1 mb-1"]/select/option/@value')
    # 遍历下载这一回全部的图片
        name = 1
        for node in node_next:

            node_url = url + node
            hm = etree.HTML(requests.get(node_url).text)
            node_img = hm.xpath('//div[@class="text-center"]/img[@class="img-fluid"]/@src')[0]
            img_url = url + node_img
            print(img_url)
            with open('./城市猎人/'+str(answer) + '回'+ str(name)+'.jpg','wb') as mh:
                bimg = requests.get(img_url).content
                mh.write(bimg)
            name += 1
        answer += 1


list = get_html(url)
get_img(list)
print('123')


