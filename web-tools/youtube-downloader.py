from pytube import YouTube
import pytube, os

from dotenv import dotenv_values
config = dotenv_values("../.env")

video_url = input("Please enter the full URL of the video you want to download: ")

def download_Video(yt):
  # filter mp4 streams from object
  my_streams = yt.streams.filter(file_extension='mp4', progressive=True).all()
  for streams in my_streams:
    # print itag, resolution and codec format of Mp4 streams
    print(f"Video itag : {streams.itag} / Resolution : {streams.resolution} / VCodec : {streams.codecs[0]}")
    
    
  # enter the itag value of resolution on which you want to download the video
  input_itag = input("Select and enter itag value : ")
  # get video using itag vale
  video = yt.streams.get_by_itag(input_itag)
  
  title=yt.title
  fn = title.replace(" ", "-")

  fd = os.chdir("/Users/{0}/Desktop/".format(config["user_login"]))

  # finally download the YouTube Video...
  video.download(filename=fn+".mp4")

  print("Video is downloading as " + fn + ".mp4")
  
# Create YouTube Object.
yt = YouTube(video_url) 

# call The function..
download_Video(yt)