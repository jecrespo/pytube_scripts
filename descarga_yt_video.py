#!/usr/bin/python
from pytube import YouTube
yt = YouTube('www.youtube.com/watch?v=-la04e1zisU')
print(yt.streams.filter(subtype='mp4').all())
yt.streams.filter(subtype='mp4').first().download()
