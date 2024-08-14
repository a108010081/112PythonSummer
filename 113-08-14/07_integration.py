import yt_dlp
import ffmpeg
import os 


URL = 'https://youtu.be/b4PIxzqsV0Y?si=x-bUXeEkY_YfEOgj'
DIR = 'C\\Youtube'


ydl_opts_video = {
    'format': 'bestvideo[ext-mp4][height=2160]',
    'outtmpl':f'{DIR}/video.mp4'
}
try:
    with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
        info_dict_video = ydl.extract_info(URL, download=True)
        video_itag = info_dict_video.get("format_id", None)
        print(f"Video DOWNLOAD: {DIR}\\video.mp4")
        print(f"Video itag: {video_itag}")
except Exception as e :
    print(f"非預期錯誤發生: {e}")

ydl_opts_audio = {
    'format': 'bestaudio[ext=mp4]',
    'outtmpl': f'{DIR}/audio.mp4',
}
try:
        with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
            info_dict_audio = ydl.extract_info(URL, download=True)
            audio_itag = info_dict_audio("format_id", None)
            print(f"Audio download: {DIR}\\audio.mp4")
            print(f"audio itag: {audio_itag}")
        
            video_input = ffmpeg.input(os.path.join(DIR, 'video.mp4'))
            audio_input = ffmpeg.input(os.path.join(DIR, 'audio.mp4'))
            outprt_path = os.path.join(DIR, 'output.mp4') 

            ffmpeg.output(video_input, audio_input, output_path).run (capture_stdout=True)
            print(f"Video and audio merged:{outprt_path}")

            os.remove(os.path.join(DIR,'video.mp4'))
            os.remove(os.path.join(DIR,'audio.mp4'))
            print("Temporary files removed")

except Exception as e :
    print(f"非預期錯誤發生: {e}")