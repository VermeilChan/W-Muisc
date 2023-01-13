from pytube import YouTube

# URL of the video you want to download
url = "https://www.youtube.com/watch?v=XXXXXXXXXXX"

# Create a YouTube object
yt = YouTube(url)

# Download the video
yt.streams.first().download()
