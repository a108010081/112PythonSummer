import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] =  'CWA-AF661ABD-8422-4540-A428-894DECC507F9'
r=requests.get(URL, params=P)
t = r.json()

location = input('查詢地點: ')
found = False 
n = len(t['records']['Station'])
for i in range(n):
 if t['records']['Station'][i]['StationName'] == location:
    print('觀測地點: ', t['records']['Station'][i]['StationName'])
    print('觀測時間: ', t['records']['Station'][i]['ObsTime']['DateTime'])
    print('觀測溫度: ', t['records']['Station'][i]['WeatherElement']['AirTemperature'])
    print('觀測溼度: ', t['records']['Station'][i]['WeatherElement']['RelativeHumidity'])
    print('觀測天氣: ', t['records']['Station'][i]['WeatherElement']['Weather'])
    found = True
    break
 
 if (found == False):
    print('輸入站點不存在')
 