import requests
import tkinter as tk
from tkinter import ttk, messagebox

# 設定 API URL 和授權
URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {'Authorization': 'CWA-AF661ABD-8422-4540-A428-894DECC507F9'}

# 發送請求並獲取資料
try:
    r = requests.get(URL, params=P)
    r.raise_for_status()  # 檢查請求是否成功
    data = r.json()
except requests.exceptions.RequestException as e:
    print(f"請求失敗: {e}")
    exit()

# 獲取所有觀測站的名稱
stations = data['records']['Station']

# 建立 GUI 應用程式
class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("氣象觀測站查詢")

        # 創建選擇觀測站的下拉式選單
        self.station_names = [station['StationName'] for station in stations]

        self.label = ttk.Label(master, text="選擇觀測站:")
        self.label.pack()

        self.station_combo = ttk.Combobox(master, values=self.station_names)
        self.station_combo.pack()

        self.button = ttk.Button(master, text="查詢", command=self.display_weather)
        self.button.pack()

        self.result_label = ttk.Label(master, text="")
        self.result_label.pack()

    def display_weather(self):
        selected_station_name = self.station_combo.get()
        found = False

        for station in stations:
            if station['StationName'] == selected_station_name:
                # 提取所需資料
                observation_time = station['ObsTime']['DateTime']
    import requests
import tkinter as tk
from tkinter import ttk, messagebox

# 設定 API URL 和授權
URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {'Authorization': 'CWA-AF661ABD-8422-4540-A428-894DECC507F9'}

# 發送請求並獲取資料
try:
    r = requests.get(URL, params=P)
    r.raise_for_status()  # 檢查請求是否成功
    data = r.json()
except requests.exceptions.RequestException as e:
    print(f"請求失敗: {e}")
    exit()

# 獲取所有觀測站的名稱
stations = data['records']['Station']

# 建立 GUI 應用程式
class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("氣象觀測站查詢")

        # 創建選擇觀測站的下拉式選單
        self.station_names = [station['StationName'] for station in stations]

        self.label = ttk.Label(master, text="選擇觀測站:")
        self.label.pack()

        self.station_combo = ttk.Combobox(master, values=self.station_names)
        self.station_combo.pack()

        self.button = ttk.Button(master, text="查詢", command=self.display_weather)
        self.button.pack()

        self.result_label = ttk.Label(master, text="", justify=tk.LEFT)
        self.result_label.pack()

    def display_weather(self):
        selected_station_name = self.station_combo.get()
        found = False

        for station in stations:
            if station['StationName'] == selected_station_name:
                # 提取所需資料
                observation_time = station['ObsTime']['DateTime']
                temperature = station['WeatherElement']['AirTemperature']
                humidity = station['WeatherElement']['RelativeHumidity']
                weather = station['WeatherElement']['Weather']

                # 顯示結果
                result_text = (f"觀測地點: {station['StationName']}\n"
                               f"觀測時間: {observation_time}\n"
                               f"觀測溫度: {temperature} °C\n"
                               f"觀測濕度: {humidity} %\n"
                               f"觀測天氣: {weather}")
                self.result_label.config(text=result_text)
                found = True
                break

        if not found:
            messagebox.showerror("錯誤", "輸入站點不存在")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
