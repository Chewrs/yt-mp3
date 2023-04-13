# import the library
from pytube import YouTube  # pip3 install pytube
import os

# loop for user to input the URL
user_in = True
list_url = []  # for collect the URL
url_count = 1

print("Enter the URL of the YouTube video you want to download :")

while user_in == True:
    url = str(input(f" URL {url_count} :"))
    url_count += 1
    if url != "":
        list_url.append(url)
    elif url == "":
        user_in = False
print()
print(f"preparing {len(list_url)} items")

# create a dir
try:
    os.mkdir("mp3")
    print()
except FileExistsError:
    print()

# loop for download and save the file
for i in list_url:
    yt = YouTube(i)
    print("downloading")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download("./mp3")

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print(f"finish {list_url.index(i)+ 1} /{len(list_url)}")
    print()
