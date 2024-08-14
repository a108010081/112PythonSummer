import yt_dlp 

PLAYLIST_URL = 'https://youtube.com/playlist?list=PLJIxQEea9fRY50FL5RXVYXW6-KFt5W1pX&si=y1gtxDn2K6PEh13m'
  
DIR = 'C\\Youtube'
ydl_opts = {
        'format': "worst",

        'outtmpl':f'{DIR}/%(title)s.%(ext)s',
    }
try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([PLAYLIST_URL])

        print(f"PLAYLIST downloaded successfully to {DIR}")        

except Exception as e :
        print(f"非預期錯誤發生: {e}")