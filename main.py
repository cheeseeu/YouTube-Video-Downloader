from pytube import YouTube

link = input("What video would you like to download? ")
yt = YouTube(link)

title = yt.title
views = yt.views
author = yt.author

if views > 1000000:
    views = f"{round(views / 1000000, 2)}M"

elif views > 1000:
    views = f"{round(views / 1000, 2)}K"

print("[System] Downloading video...")
print(f"""---------------
      
Title: {title}

Views: {views}

Author: {author}

---------------""")

yd = yt.streams.get_highest_resolution()
yd.download('./')
print("[System] Downloaded video successfully!")
