import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] =  'CWA-AF661ABD-8422-4540-A428-894DECC507F9'
r=requests.get(URL, params=P)
t = r.json()
station_id = 28
print('觀測地點: ', t['records']['Station'][station_id]['StationName'])
print('觀測時間: ', t['records']['Station'][station_id]['ObsTime']['DateTime'])
print('觀測溫度: ', t['records']['Station'][station_id]['WeatherElement']['AirTemperature'])
print('觀測溼度: ', t['records']['Station'][station_id]['WeatherElement']['RelativeHumidity'])
print('觀測天氣: ', t['records']['Station'][station_id]['WeatherElement']['Weather'])