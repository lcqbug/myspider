# 首个爬取界面 http://www.dizigui.cn/xijiang1.asp
# 观察界面可知 有40 个章节
# 这个网页没有反爬
import requests
from bs4 import BeautifulSoup
import re


def all_urls():
    for i in range(1, 41):
        yield 'http://www.dizigui.cn/xijiang{}.asp'.format(i)


# print(list(gen_all_urls()))

def down_one_page(url, headers=None):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding  # 让它自己去猜网站的编码  GB2312
    # print(res.encoding)
    res.raise_for_status()  # 如果状态码不对 直接抛异常
    # print(res.text)
    return res.text
    # parse_one_page(res.text)


def parse_one_page(html):
    """
    解析一个界面
    :param html: 待解析的网页
    :return: ()
    """
    soup = BeautifulSoup(html, 'html.parser')
    # title = soup.find('font',size=5).text.strip()
    # table22 > tbody > tr:nth-child(1) > td > p > b > font
    title = soup.select_one('td>p>b>font').text.strip()
    num = soup.select_one('tr:nth-child(2) > td > p > font').text.strip()
    # 主讲人和时间
    author_time = soup.select_one('tr:nth-child(3) > td > p > font').text.strip()
    # print(title)
    # print(num)
    lecturer = author_time.split(' ')[0].strip()
    lec_date = author_time.split(' ')[1].strip()
    # print(lecturer)
    # print(lec_date)
    # table22 > tbody > tr:nth-child(5) > td > p > span
    content = soup.select_one('tr:nth-child(5) > td > p > span').text
    # print(content)
    return (title, num, lecturer, lec_date, content)

    # table22 > tbody > tr:nth-child(2) > td > p > font
    # table22 > tbody > tr:nth-child(3) > td > p > font
    # p =r'<font face="楷体_GB2312" size="5">\s+(\S+?)</font></b></td>'
    # c = re.compile(pattern=p)
    # # c.findall()
    # print(c.findall(html))


# p = parse_one_page(down_one_page('http://www.dizigui.cn/xijiang1.asp'))
# print(p)


def save_page(tupledata):
    """
    将解析好的数据保存
    存储成文件 数据库.. 都可以
    :return:
    """
    pass


url = next(all_urls())
print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# down_one_page(url, headers=headers)
# for page in all_urls():
#     down_one_page(page)
