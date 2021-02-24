from pytube import YouTube
link = input("Enter The Link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()