import yt_dlp 


URL = 'https://youtu.be/b4PIxzqsV0Y?si=x-bUXeEkY_YfEOgj'
DIR = 'C\\Youtube'


ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]',  # 選擇最高解析度並確保為MP4格式
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',  # 定義文件名格式
    'merge_output_format': 'mp4',  # 確保合併後的格式為MP4
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(URL, download=True)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get("title", None)
        downloaded_format_id = info_dict.get("format_id", None)
    if video_id and downloaded_format_id:
        print(f"Video '{video_title}' downloaded succesfully with the lowest resolution!")
        print(f"Video ID: {video_id}")    
        print(f"Downloaded format itag: {downloaded_format_id}")

except Exception as e :
    print(f"非預期錯誤發生: {e}")

