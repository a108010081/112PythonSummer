#LINENOTIFY傳送本機圖片
import requests
IMG = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/%E6%A2%85%E9%87%8C%E9%9B%AA%E5%B1%B1.jpg'
URL = 'https://notify-api.line.me/api/notify'
H, P, F ={}, {}, {}
H['Authorization'] = 'Bearer UDKJSZ0QqUz8OLtGbHYaih5KOy7GwV6Uwp6GOuDaE46'
P['message'] = "網路圖片"
F['imageFile'] = requests.get(IMG).content
response = requests.post(URL, headers=H, params=P, files=F)

print(response.status_code)
print(response.text)
