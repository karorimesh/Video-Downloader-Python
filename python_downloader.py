from hashlib import new
import os
import pytube
import datetime

downloadDir = os.path.dirname(os.getcwd())
videoDir = "videos"
playlistDir = datetime.datetime.now().strftime("%f")

isPlaylist = False

link = "https://www.youtube.com/watch?v=8gDDwIQc838"

def downloadVid(video, path):
    os.chdir(path)
    videoStream = video.streams.get_lowest_resolution()
    try:
        videoStream = video.streams.get_highest_resolution()
        videoStream.download()
    except:
        try:
            print('Could not download highest quality of', video.title)
            videoStream = video.streams.filter(progressive=True)
            videoStream.download()
        except:
            try:
                print("Could not download video... Downloading audio")
                videoStream = video.streams.get_lowest_resolution()
                videoStream.download()
            except:
                print("Could not download anyway... Aborting")

if isPlaylist:
    playlist = pytube.Playlist(link)
    try:
        playlistDir = playlist.title
    except:
        print("Playlist does not have a name")
    path = os.path.join(downloadDir, playlistDir)
    os.mkdir(path)
    for video in playlist.videos:
        downloadVid(video, path)
    

else:
    video = pytube.YouTube(link)
    path = os.path.join(downloadDir, videoDir)
    downloadVid(video,path)
    
        