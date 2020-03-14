from danksearch import Video
from PIL import Image
video=Video()
video.search("Never gonna give you up")
print(video.title)
# Rick Astley - Never Gonna Give You Up (Video)
print(video.video_id)
# dQw4w9WgXcQ
print(video.url)
# http://www.youtube.com/watch?v=dQw4w9WgXcQ
