# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
link="https://youtu.be/sK7riqg2mr4"

try:
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.streams.filter('mp4')

#to set the name of the file
yt.set_filename('python youtube Video downloader')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
