# danksearch
Search youtube videos purely using python requests and BeautifulSoup

# Usage
Searching YouTube videos is as easy as this

    from danksearch import Video
    video=Video()
    video.search("me at the zoo")
    print(video.url)
    
Get video thumbnail as a PIL image object
    
    image=video.thumbnail_as_image()
    image.show()
    
# Installation
No installation is required, download the header only library `danksearch.py` and move it to your project folder
