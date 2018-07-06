import requests
from bs4 import BeautifulSoup

# headers = {
#     # 'Host': 'www.douban.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
#     'Referer': 'www.douban.com'
# }

start_url = 'https://accounts.douban.com/login?source=movie'
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
})
res = session.get(start_url)

print(res.status_code)
print(res.text)
soup = BeautifulSoup(res.text, 'lxml')
img = soup.find(id='captcha_image')['src']
print('*******img', img)

post_url = 'https://accounts.douban.com/login'


def getid(img):
    left = img.find('=')
    right = img.find('&')
    print(img[left:right + 1])
    return img[left + 1:right]


from about_login import setting

if not img:
    print('没有验证码!')
    # resp = session.post(post_url, data=data)
    # print(resp.status_code)
    # print(resp.text)
else:
    print('有验证码!')
    stri = input('请输入验证码:\n')
    # moM7f9R9Rb6iueTVo46KVGcP: en
    data = {
        'redir': 'https://www.douban.com/',
        'form_email': setting.email,  # 此处需要填写自己的email
        'form_password': setting.psd,  # 此处需要填写自己的密码
        'captcha-solution': stri,
        'captcha-id': getid(img),
        'login': '登录'

    }

    resp = session.post(post_url, data=data)
    print(resp.status_code)
    print(resp.text)
# captcha_image
