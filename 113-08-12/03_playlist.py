import yt_dlp 

PLAYLIST_URL = 'https://youtube.com/playlist?list=PL-TNsCdgs5WCZnsaWi_liXveQzkVFSlSW&si=2Nchiic0c2QNxhX7'
  
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