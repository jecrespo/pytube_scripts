#!/usr/bin/python
from pytube import YouTube
yt = YouTube('www.youtube.com/watch?v=-la04e1zisU')
yt.streams.filter(type='audio',subtype='mp4').first().download()
