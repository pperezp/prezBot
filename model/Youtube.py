# sudo pip install --upgrade youtube_dl
from __future__ import unicode_literals
import youtube_dl

class Youtube:
    @staticmethod
    def getMp3(url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'ca.mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)

        video_title = video_title.replace("\'","")
        video_title = video_title.replace("\"","")

        ydl_opts2 = {
            'format': 'bestaudio/best',
            'outtmpl': video_title + '.mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts2) as ydl:
            ydl.download([url])

        return video_title;


