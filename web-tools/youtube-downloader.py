from pytube import YouTube
import os

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

  # Ask the user if they want to rename the title
  input_title = input("Would you like to rename the video, if no then title on Youtube will be used.  y/n ")

  if(input_title.lower() == "y"):
    # Rename using their input
    fn = input("New title (please no spaces): ")
  else:
    # Rename using the title on youtube, but-converting-to-dashes instead of spaces
    title=yt.title
    fn = title.replace(" ", "-")

  os.chdir(os.path.expanduser("~/Desktop"))

  # finally download the YouTube Video...
  video.download(filename=fn+".mp4")

  print("Video is downloading as " + fn + ".mp4")
  
# Create YouTube Object.
yt = YouTube(video_url) 

# call The function..
download_Video(yt)