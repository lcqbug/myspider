# 这个是测试的文件  可以忽略

t = ':authority: www.jd.com'
print(t.find(':'))
print(t.find('aaa'))  # find 没有会 -1

print(t.index(':'))
# print(t.index('aa')) # index 没有会报错

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

lines = headers_str.split("\n")[1:-1]


def parse_line(lines):
    dict1 = {}
    for line in lines:
        # if 'cookie' in line:
        #     continue
        if line[0] == ':':
            k, v = line.rsplit(':', 1)  # 观察到有些字段是以:开头的
            dict1[k.strip()] = v.strip()  # 观察到字符串转成字典后,有空格
        else:
            k, v = line.split(':', 1)
            dict1[k.strip()] = v.strip()

        # dict1[x[0]] = x[1]
        # print({v[0]:v[1] for v in x})

    return dict1


res = parse_line(lines)
print(res)
print('.....')
n = res.pop('cookie')
print(n)


def getcookie(cookie_str):
    cookies = {}
    lis = cookie_str.split(';')
    # print('|||||||||')
    # print(lis)
    for l in lis:
        k, v = l.split('=', 1)  # 有形如 o2Control:webp|lastvisit=17 这样的
        # print('|||||||||')
        # print(k,v)
        cookies[k.strip()] = v.strip()
    return cookies


print('.>>>>>>>>>>>>>>>>>>>>>>')

cookies = getcookie(n)
print(cookies)
