from pytube import YouTube
from pytube.cli import on_progress
import sys

"""
Do all of these:
pip install git+https://github.com/ssuwani/pytube
pip install pytube
pip install pytube3
pip install sys
"""

raw_link = input("[>] Enter Video Id: ")
link = "https://youtu.be/" + raw_link
video = YouTube(link, on_progress_callback=on_progress)

try:
    print("[+] Title: " + str(video.title))
    print("[+] Description: " + "\n" + str(video.description))
    print("[+] Length: " + str(video.length) + " Seconds")
    final_video = video.streams.get_highest_resolution()
except KeyError:
    print("[-] Invalid Link")
    sys.exit()

try:
    print("[*] Downloading...")
    final_video.download('C:\\Users\\hp\\Desktop\\YouTube')
    print("\n[+] Download completed!!")
except KeyboardInterrupt:
    print("[-] Aborted")
    sys.exit()
