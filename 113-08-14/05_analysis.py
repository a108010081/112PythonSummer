import yt_dlp 

URL = 'https://youtu.be/b4PIxzqsV0Y?si=x-bUXeEkY_YfEOgj'
DIR = 'C\\Youtube'
ydl_opts = {
        'format': 'all',
        'skip_download':True,
}

try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(URL, download=False)
            format = info_dict.get('formats',[])
            for res in format:
                vcodec = res.get('vcodec','none')
                acodec = res.get('acodec','none')

                is_video_only = vcodec != 'none' and acodec =='none'
                is_audio_only = vcodec == 'none' and acodec !='none'
                is_progressive = vcodec!='none'and acodec!='None'
                
                label =""
                if is_video_only:
                    label = "[video only]"
                elif  is_audio_only:
                    label = "[audio only]"
                if is_progressive:
                     label += "[progressive]"
                else:
                     label +="[non-progressive]"
                # 打印流信息，包括 codec 信息和 progressive/non-progressive 信息
                print(f"Format ID: {res['format_id']}, Ext: {res['ext']}, Resolution: {res.get('resolution', 'N/A')}, "
                  f"Video Codec: {vcodec}, Audio Codec: {acodec}, Note: {res.get('format_note', 'N/A')}{label}")

except Exception as e :
        print(f"非預期錯誤發生: {e}")