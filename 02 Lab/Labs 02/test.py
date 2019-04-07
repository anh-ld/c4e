# Note: If you have not installed youtube-dl yet, do it before trying this tutorial
# Open your command-lline (Ctrl + `) then enter:
# pip install youtube-dl
from youtube_dl import YoutubeDL

# Type and run the samples below, one by one
# Result: https://www.dropbox.com/s/cm5m6zitnuwdqbk/Screenshot%202017-12-08%2005.32.02.png?dl=0

# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4']) # Remember to put your video in a list, eventhough one video is downloaded



# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
# Put list of song urls in download function to download them, one by one
dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])



# Sample 3: Download audio
options = {
    'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])



# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])


# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])
