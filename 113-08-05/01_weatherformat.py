import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] =  'CWA-AF661ABD-8422-4540-A428-894DECC507F9'
r=requests.get(URL, params=P)
t = r.json()
print(t)
