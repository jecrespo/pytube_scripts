# -*- coding: utf-8 -*-
"""
Librería https://pypi.python.org/pypi/pytube/

Manual pytube: https://pytube.readthedocs.io/en/latest/

Ejemplo Uso consola: "pytube -emp4 -r360p"


"""

from pytube import YouTube
from pprint import pprint

lista_videos = ['www.youtube.com/watch?v=-la04e1zisU',  #NSN_1x01
                'www.youtube.com/watch?v=qXYcSvrD7S8',  #NSN_1x02
                'www.youtube.com/watch?v=GqJIqv6GHjE',  #NSN_1x03
                'www.youtube.com/watch?v=XxW4dmUSPio',  #NSN_1x04
                'www.youtube.com/watch?v=MRNfXU79e3c']  #NSN_1x05

for video in lista_videos:
    print(video)

    yt = YouTube(video)

    str_yt = yt.streams.filter(subtype='mp4',res='360p') #stream query
    print(type(str_yt))
    
    l_yt = yt.streams.filter(subtype='mp4',res='360p').all() #lista de streams
    pprint(l_yt)
    
    print(str_yt.first()) #primer stream de la query
    
    str_yt.first().download() #descarga primer stream

print("Videos descargados!!!!")