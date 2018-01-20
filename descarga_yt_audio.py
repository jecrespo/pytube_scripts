#!/usr/bin/python
from pytube import YouTube
yt = YouTube('www.youtube.com/watch?v=-la04e1zisU')
yt.streams.filter(only_audio=True).first().download()
