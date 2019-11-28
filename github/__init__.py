# 此 模块模拟登陆github

# 注意: 不同的浏览器访问github,github的请求方式有所不同
# 我用的是谷歌浏览器

# 请求流程是
url1= 'https://github.com/login'
url2 = 'https://github.com/manifest.json'
url3 = 'https://github.com/session'
# step 1: 先去 url1 去获取界面上的相关 请求头中的数据
# step 2: 再去 url2 更新cookie,  我们发现 url3中携带的cookie和url1中返回的cookie不一致
# step 3: 用新cookie和请求头中的数据 去访问url3 登陆成功


