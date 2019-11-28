# 将 浏览器中的京东header请求头粘贴在这里
# 请求头类似于这样
headers_str = """
:authority: www.jd.com
:method: GET
:path: /
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: __jdu=248095303; o2Control=webp|lastvisit=17; shshshfpa=eb2ba56c-3c42-8e7f-77fc-cb36b01741f4-1547684317; shshshfpb=rPkzx2jF22v1iHWpUEPQJbA%3D%3D; o2State={%22webp%22:true%2C%22lastvisit%22:1571711405752}; unpl=V2_ZzNtbRZXEBAhDk8BfBEIAWIFEllKUxZAfF9DXSsRWlFiAxYIclRCFX0URlRnGlUUZwMZXUJcRhRFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHgcVQRvBxBcQGdzEkU4dl19HF4CVwIiXHIVF0lyC05Qfh8RBmIKE1VGVUIXRQl2Vw%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_e1b4e78d69e5471595dd8f48a97e415d|1574910700331; areaId=1; ipLoc-djd=1-2901-0-0; PCSYCityID=CN_110000_110100_0
pragma: no-cache
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
"""


def parse_headers(headers_str):
    lines = headers_str.split("\n")[1:-1]
    dict_with_cookie = {}
    for line in lines:
        if line[0] == ':':
            k, v = line.rsplit(':', 1)  # 观察到有些字段是以:开头的
            dict_with_cookie[k.strip()] = v.strip()  # 观察到字符串转成字典后,有空格
        else:
            k, v = line.split(':', 1)
            dict_with_cookie[k.strip()] = v.strip()
    return dict_with_cookie


def get_cookie_str(headers_str):
    """
    仅仅得到cooke字符串
    :param headers_str:
    :return:
    """
    lines = headers_str.split("\n")[1:-1]
    for line in lines:
        if line.startswith('cookie'):
            return line.split(':', 1)[1]


# print(get_cookie_str(headers_str))


def getcookie(cookie_str):
    cookies = {}
    lis = cookie_str.split(';')
    for l in lis:
        k, v = l.split('=', 1)  # 有形如 o2Control:webp|lastvisit=17 这样的
        cookies[k.strip()] = v.strip()
    return cookies


print('.>>>>>>>>>>>>>>>>>>>>>>')


# cookies = getcookie(n)
# print(cookies)

def getcookie_from_headerstr(headerstr):
    # dict_with_cookie = parse_headers(headers_str)
    # cookie_str = dict_with_cookie.pop('cookie')
    cookie_str = get_cookie_str(headers_str)
    cookies = getcookie(cookie_str)
    return cookies


def get_headers_cookies(headerstr):
    dict_with_cookie = parse_headers(headers_str)
    cookie_str = dict_with_cookie.pop('cookie')  # 经过这一步后 dict_with_cookie 变成了 dict without cookie
    cookies = getcookie(cookie_str)
    return dict_with_cookie, cookies

# res = getcookie_from_headerstr(headers_str)
# print(res)
