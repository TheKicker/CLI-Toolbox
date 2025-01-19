import yt_dlp
import os

video_url = input("Please enter the full URL of the video you want to download: ")

def download_video(video_url):
    ydl_opts = {
        'outtmpl': '~/Desktop/%(title)s.%(ext)s',  # Save to Desktop
        'format': 'best[ext=mp4]',  # Select best mp4 format
        'noplaylist': True,  # Download only the single video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        print("Download complete!")

download_video(video_url)
