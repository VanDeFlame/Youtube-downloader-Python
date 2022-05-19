# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:46:06 2022

@author: agush
"""
from cProfile import label
from logging import PlaceHolder
from turtle import color
from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import os
import re

def removeInvalidChar(str):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+", flags=re.UNICODE)
    return re.sub(r'[^\w\-_\. ]', '_', emoji_pattern.sub(r'', str).strip())

def accion(enlace, audio: bool):
    video = YouTube(enlace)

    if(audio):
        descarga = video.streams.get_audio_only()
        nombreArchivo = removeInvalidChar(descarga.default_filename)
        archivo = descarga.download(output_path='./audio', filename=nombreArchivo)
        nombreArchivo = nombreArchivo[0:-4] + '.mp3'
        os.rename(archivo, './audio/' + nombreArchivo)
    else:
        descarga = video.streams.get_highest_resolution()
        nombreArchivo = removeInvalidChar(descarga.default_filename)
        descarga.download(output_path='./video', filename=nombreArchivo)

    info = Label(root, text = "Finish")
    info.grid(row = 2, column = 1)
    root.after(2000, info.destroy)

def run():
    global root
    root = Tk()
    root.config(bd=15)
    root.title('KannaDownloader')

    foto = PhotoImage(file='./dow.png')
    insertarFoto = Label(root, image=foto, bd = 0)
    insertarFoto.grid(row = 1 , column=1)

    texto = Label(root, text = "Downloader\n KannaTeam\n （＾∀＾●）ﾉｼ")
    texto.grid(row = 1 , column = 2)

    url = Label(root, text = "URL")
    url.grid(row = 2 , column = 1)

    videos = Entry(root)
    videos.grid(row = 2, column = 2)

    mp4 = Button(root , text = "Download Video",command=lambda: accion(videos.get(), False))
    mp4.grid(row = 3, column = 1)
    mp3 = Button(root , text = "Download Audio",command=lambda: accion(videos.get(), True))
    mp3.grid(row = 3, column = 2)

    root.mainloop()

if __name__ == "__main__":    
    run()