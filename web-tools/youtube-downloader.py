from pytube import YouTube
import os

def download_Video(yt):
    try:
        # Attempt to filter mp4 streams
        my_streams = yt.streams.filter(file_extension='mp4', progressive=True).all()
        for streams in my_streams:
            print(f"Video itag : {streams.itag} / Resolution : {streams.resolution} / VCodec : {streams.codecs[0]}")
        
        input_itag = input("Select and enter itag value: ")
        video = yt.streams.get_by_itag(input_itag)

        input_title = input("Would you like to rename the video? (y/n): ")

        if input_title.lower() == "y":
            fn = input("New title (spaces will be replaced with dashes): ")
        else:
            title = yt.title
            fn = title[0:25]

        os.chdir(os.path.expanduser("~/Desktop"))

        fn = fn.replace(" ", "-")
        video.download(filename=fn + ".mp4")
        print("Video is downloading as " + fn + ".mp4")
    except Exception as e:
        print("An error occurred: ", e)

# Main Program
video_url = input("Please enter the full URL of the video you want to download: ")
yt = YouTube(video_url)

# This will bypass the age gate (if applicable)
yt.bypass_age_gate()

# Call the function
download_Video(yt)
