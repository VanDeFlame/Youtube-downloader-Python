# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:46:06 2022

@author: agush
"""
from cProfile import label
from pytube import YouTube
from tkinter import *
from tkinter import messagebox

def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

root = Tk()
root.config(bd=15)
root.title('KannaDownloader')


videos = Entry(root)
videos.grid(row = 1, column =2 )

texto = Label(root, text ="Downloader KannaTeam")
texto.grid(row = 1 ,column = 1)
boton = Button(root , text = "Descargar （＾∀＾●）ﾉｼ",command=accion)
boton.grid(row =2,column=1)

root.mainloop()

