import requests
from bs4 import BeautifulSoup
import settings
url = 'https://github.com/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
url2 = 'https://github.com/manifest.json'
url3 = 'https://github.com/session'

# commit: Sign in
# utf8: ✓
# authenticity_token: D4kV0JvnLydtUJtazqAH23ZEbAO/uY2YltB6l+CAIE+ZwGa+9zWDChXDB3GTQa4oGUwlaRRVKhYV0+H9xcpOow==
# ga_id: 755860019.1542809296
# login: 54093177@qq.com
# password: 11111
# webauthn-support: supported
# webauthn-iuvpaa-support: unsupported
# required_field_5241:
# timestamp: 1574836123980
# timestamp_secret: 6cd6


s = requests.session()
s.headers.update(headers)
res = s.get(url, headers=headers)
print(res.text)


def parsehtml_getdata(html):
    soup = BeautifulSoup(html,'html.parser')
    authenticity_token=soup.find(name='input',attrs={'name':'authenticity_token'}).get('value')
    ga_id=soup.find(name='input',attrs={'name':'ga_id'}).get('value')
    timestamp=soup.find(name='input',attrs={'name':'timestamp'}).get('value')
    timestamp_secret=soup.find(name='input',attrs={'name':'timestamp_secret'}).get('value')

    data = {
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': authenticity_token,
        # 'ga_id': ga_id,
        'ga_id': '755860019.1542809296',
        'login': settings.user,
        'password': settings.password,
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'unsupported',
        'required_field_5241': '',
        'timestamp': timestamp,
        'timestamp_secret': timestamp_secret
    }
    return data


print(parsehtml_getdata(res.text))

s.get(url2) # 更新cookie
res = s.post(url3,data=parsehtml_getdata(res.text))
print('-------------------------------------')
print(res.text)