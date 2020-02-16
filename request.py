from json import dumps
import requests
import time
from config import stuID, platfromPassword

# 第一次请求
if True:
    r = requests.post(url='http://stuinfo.neu.edu.cn/api/auth/oauth/token',
                      data={
                          'username': stuID,
                          'grant_type': 'password',
                          'password': platfromPassword,
                          '_t': int(time.time())
                      },
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
                          'Origin': 'http://stuinfo.neu.edu.cn',
                          'Referer': 'http://stuinfo.neu.edu.cn/',
                          'Authorization': 'Basic dnVlOnZ1ZQ=='
                      })

    access_token = str(r.json()['access_token'])
    # print('ACCESS TOKEN:\n' + access_token)

# 第二次请求
if True:
    r = requests.post('http://stuinfo.neu.edu.cn/cloud-xxbl/studenLogin',
                      data={
                          '_t': int(time.time())
                      },
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
                          'Origin': 'http://stuinfo.neu.edu.cn',
                          'Referer': 'http://stuinfo.neu.edu.cn/',
                          'Authorization': 'Bearer ' + access_token
                      }, cookies={
            'access_token': access_token,
            'userName': stuID
        })

data3 = str(r.json()['data'])  # 地址栏数据
# print('Address:\n' + data3)

# 第三次请求
r = requests.get('http://stuinfo.neu.edu.cn/cloud-xxbl/studentinfo?tag=' + data3,
                 data={
                     '_t': int(time.time())
                 },
                 headers={
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
                     'Origin': 'http://stuinfo.neu.edu.cn',
                     'Referer': 'http://stuinfo.neu.edu.cn/',
                     'Authorization': 'Bearer ' + access_token
                 },
                 cookies={
                     'access_token': access_token,
                     'userName': stuID
                 })
# print(r.headers['set-cookie'])
JSESSIONID = str(r.headers['set-cookie']).split(';')[0].split('=')[1]
# print(JSESSIONID)

r = requests.get('http://stuinfo.neu.edu.cn/cloud-xxbl/getStudentInfo',
                 headers={
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
                     'Origin': 'http://stuinfo.neu.edu.cn',
                     'Referer': 'http://stuinfo.neu.edu.cn/',
                     'Authorization': 'Bearer ' + access_token
                 },
                 cookies={
                     'accessToken': access_token,
                     'userName': stuID,
                     'JSESSIONID': JSESSIONID
                 })
personalData = dict(r.json()['data'])  # dict class
# print(personalData)

exampleJson = {
    'xm': "",  # 姓名
    'xh': "",  # 学号
    'xy': "",  # 学院
    'njjzy': "",  # 年级及专业
    'bj': "",  # 班级
    'brsjhm': "",  # 手机号
    'sylx': "",  # 生源类型
    'jtxxdz_sf': "",  # 省份
    'jtxxdz_cs': "",  # 城市
    'jtxxdz_qx': "",  # 区县
    'jtxxdz': "",  # 住址
    'mqxxdz_sf': "",  # 省份
    'mqxxdz_cs': "",  # 城市
    'mqxxdz_qx': "",  # 区县
    'mqxxdz': "",  # 地址
    'jzsjhm': "",  #
    'mqzk': "",  # 目前状况
    'zjtw': "",  # empty
    'zzkssj': "",  # empty
    'sfjy': "",  # empty
    'sfyqjc': "",  # empty
    'mqsfzj': "",  # empty
    'jtms': "",  # empty
    'glyyms': "",  # empty
    'gldxxdz_sf': "",  # empty
    'gldxxdz': "",  # empty
    'mqstzk': "",  # empty
    'sfgcyiqz': "",  # empty
    'cjlqk': "曾经医学观察，后隔离解除",
    'dsjtqkms': "",  # 当时具体状况描述 必须留空
    'sfbrtb': "",  # 是否本人填表
    'fdysfty': "否",  # 辅导员是否同意
    'tbrxm': "",  # empty
    'tbrxh': "",  # empty
    'tbrxy': "",  # empty
    'dtyy': "",  # empty
    'id': ""  # id
}  # 需要改的是 'sfgcyiqz': "否",
for i in exampleJson.keys():
    if i in personalData.keys():
        exampleJson[i] = personalData[i]
# 用返回的数据填写要返回的json
exampleJson['sfgcyiqz'] = "否"
exampleJson['dsjtqkms'] = ""

# print(exampleJson)
r = requests.post('http://stuinfo.neu.edu.cn/cloud-xxbl/updateStudentInfo?t=' + str(int(time.time())),
                  cookies={
                      'accessToken': access_token,
                      'userName': stuID,
                      'JSESSIONID': JSESSIONID
                  },
                  headers={
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
                      'Origin': 'http://stuinfo.neu.edu.cn',
                      'Referer': 'http://stuinfo.neu.edu.cn/cloud-xxbl/studentinfo?tag=' + data3,
                      'Content-Type': 'application/json',
                  },
                  data=dumps(exampleJson)
                  )
# print(r.json())
if r.json()['success'] == True:
    print('Done.')
else:
    print('ERROR')
