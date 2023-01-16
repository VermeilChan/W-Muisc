import youtube_dl
import os

ydl_opts = {
    'format': 'bestaudio/mp3',
    'outtmpl':'%(title)s.%(ext)s',
}

def download_video(url:str)->None:
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube URL:")
    download_video(url)
