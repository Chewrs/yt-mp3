import tkinter as tk
from pytube import YouTube
import os
from time import sleep


win = tk.Tk()

win.geometry("750x250")
win.title("Youtube - Mp3")

list_url = []
show = ""


def next_url():
    global show
    URL = entry_url.get()
    if URL != "":
        list_url.append(URL)  # add url to list
    else:
        print("else")

    entry_url.delete(0, 100000)  # clear the entry from index 0 to 100000

    url_count_show = "URL", len(list_url) + 1, ":"  # format: URL 1, URL 2 ...
    second_label.configure(text=url_count_show)  # show label URL 1, URL2 ....
    try:
        yt = YouTube(URL)
        video_title = yt.title
    except:
        video_title = "unknown"

    print(show)
    show += video_title
    show += "\n"
    print(show)
    label_video.configure(text=show)


def download():
    global list_url
    global show
    try:
        os.mkdir("mp3")
        print()
    except FileExistsError:
        print()

    for i in list_url:
        yt = YouTube(i)

        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download("./mp3")

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)

    label_video.configure(text="")
    list_url = []
    show = ""

    url_count_show = "URL", len(list_url) + 1, ":"  # format: URL 1, URL 2 ...
    second_label.configure(text=url_count_show)  # show label URL 1, URL2 ....
    status_label.configure(text="")


top_label = tk.Label(text="Enter the URL of the YouTube video you want to download ")
top_label.pack()


second_label = tk.Label(text="URL 1 :")
second_label.pack()

entry_url = tk.Entry(width=50)
entry_url.focus()
entry_url.pack()

label_video = tk.Label(text="")
label_video.pack()


button_next = tk.Button(text="next URL", width=15, command=next_url)
button_next.pack()


button_download = tk.Button(text="Download", width=15, command=download)
button_download.pack()

status_label = tk.Label(text="")
status_label.pack()

win.mainloop()
