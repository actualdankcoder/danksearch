#! /usr/bin/python3
import requests, bs4
from io import BytesIO
import PIL
class ImageDataNotFound(Exception):
    '''No data about the thumbnail could be found because the video wasn't searched yet'''
    pass
class Video:
    def __init__(self):
        self.url=None
        self.thumbnail=None
        self.title=None
        self.video_id=None
        self.pafydata={}
    def search(self, name):
        fullcontent = ('http://www.youtube.com/results?search_query=' + name)
        text = requests.get(fullcontent).text
        soup = bs4.BeautifulSoup(text, 'html.parser')
        img = str(soup.find_all('img')[9]["src"])
        div = [ d for d in soup.find_all('div') if d.has_attr('class') and 'yt-lockup-dismissable' in d['class']]
        a = [ x for x in div[0].find_all('a') if x.has_attr('title') ]
        title = (a[0]['title'])
        a0 = [ x for x in div[0].find_all('a') if x.has_attr('title') ][0]
        url = ('http://www.youtube.com'+a0['href'])
        self.url=str(url)
        self.thumbnail=img
        self.title=str(title)
        self.video_id=a0['href'] 
    def thumbnail_as_image(self):
        if not self.thumbnail==None:
            return PIL.Image.open(BytesIO(requests.get(self.thumbnail).content))
        else:
            raise ImageDataNotFound
