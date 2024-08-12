import yt_dlp 

URLs = [
    'https://youtu.be/bSJxw5-z1xQ?si=8rJH_YttUyRaxwCL',
    'https://youtu.be/Wua2hiMJu8s?si=E6i95cJsFvaEsyv2',
    'https://youtu.be/NzkvwuTK_LI?si=7tn_q7E65rs5TgmL',
    'https://youtu.be/0Pnj0__dWE0?si=HE6MpvvVx11KxDfa'
    ]
 
DIR = 'C\\Youtube'

for URL in URLs:
   
    ydl_opts = {
        'format': "worst",

        'outtmpl':f'{DIR}/%(title)s.%(ext)s',
    }
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