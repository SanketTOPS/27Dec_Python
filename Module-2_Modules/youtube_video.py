from pytubefix import YouTube

url = "https://www.youtube.com/watch?v=eEeX2QMlSlo"

YouTube(url).streams.first().download()
print("Download successfully!")
