import requests
import os
import sys
import subprocess
import re

headers = {
    'systoken': '23f8249e3b1e44660a4d3daaa83c164c',
    'Host': 'dhcxzil.facecast.xyz',
    'User-Agent': 'okhttp/3.12.1',
}

data = {
  'device': 'G011A',
  'deviceId': '724017785212191',
  'unixTime': '1580846138062',
  'versionCode': '2270',
  'longitude': '',
  'userId': '520725',
  'androidSdkLevel': '22',
  'systoken': '23f8249e3b1e44660a4d3daaa83c164c',
  'cpuArch': '32',
  'cnt': '20',
  'platform': 'android',
  'app_version': '2.2.7',
  'platform_version': '5.1.1',
  'api_version': '2',
  'latitude': '',
  'index': '1',
  'language': 'pt',
  'type_id': '4',
  'user_id': '520725',
  'country_id': '18'
}

requisição = requests.post('https://dhcxzil.facecast.xyz/faceshow/tokens/weapp/live_room/get_room_list', headers=headers, data=data)
x = re.findall('http://live.gchao.cn/live/23331_?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', requisição.text)
s = ('\n'.join(x))
m = re.sub('txSecret=?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', s)
y = re.findall('http://live.gchao.cn/live/23331_.*m3u8', m)

sys.stdout = open('output.txt','wt')
print ('\n'.join(y))
