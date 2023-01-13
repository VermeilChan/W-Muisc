import youtube_dl

ydl_opts = {
    'format': 'bestaudio/mp3',
    'outtmpl':'%(title)s.%(ext)s',
}

try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=0KaWvzuYFB8'])
except Exception as e:
    print(f'An error occured: {e}')
