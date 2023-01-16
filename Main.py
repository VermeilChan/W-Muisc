import youtube_dl
import tkinter as tk

def start_download():
    url = url_entry.get()
    ydl_opts = {
        'format': 'bestaudio/mp3',
        'outtmpl':'%(title)s.%(ext)s',
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.config(text='Download complete!')
    except Exception as e:
        status_label.config(text=f'An error occured: {e}')

root = tk.Tk()
root.title("YouTube Downloader")

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(root)
url_entry.grid(row=0, column=1, padx=10, pady=10)

download_button = tk.Button(root, text="Download", command=start_download)
download_button.grid(row=1, column=0, columnspan=2, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
