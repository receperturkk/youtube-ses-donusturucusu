import tkinter as tk
from tkinter import *
from pytube import YouTube
from pytube import Playlist


pencere = tk.Tk()
pencere.geometry("900x600")
pencere.title("github: receperturkk")
canvas = Canvas(pencere, width=1000, height=1000,background="light blue")
canvas.pack()



def playlist():
    global urlGiris
    global urlBaslik
    global urlBaslik
    global urlArama

    baslik.destroy()
    baslik1.config(text="Sese dönüştürmek istediğiniz playlist\'in linkini giriniz.")
    baslik1.place(x=120 , y=200)
    secimPlaylist.destroy()
    secimTek.destroy()
    

    urlBaslik = Label(pencere)
    urlBaslik.config(text="URL",font=("Arial",20),foreground="black",background="light blue")
    urlBaslik.place(x=10 ,y=270)

    urlGiris = Entry(pencere)
    urlGiris.config(font=("Arial",17),foreground="black",width=50)
    urlGiris.place(x=75 ,y=275)

    urlArama = Button(pencere)
    urlArama.config(text="Bul",font=("Arial",12),foreground="white",width=10,bg="gray",command=pBul)
    urlArama.place(x=750 ,y=273)

def tek():
    global urlGiris
    global urlBaslik
    global urlBaslik
    global urlArama

    baslik.destroy()
    baslik1.config(text="Sese dönüştürmek istediğiniz video\'nun linkini giriniz.")
    baslik1.place(x=120 , y=200)
    secimPlaylist.destroy()
    secimTek.destroy()
    

    urlBaslik = Label(pencere)
    urlBaslik.config(text="URL",font=("Arial",20),foreground="black",background="light blue")
    urlBaslik.place(x=10 ,y=270)

    urlGiris = Entry(pencere)
    urlGiris.config(font=("Arial",17),foreground="black",width=50)
    urlGiris.place(x=75 ,y=275)

    urlArama = Button(pencere)
    urlArama.config(text="Bul",font=("Arial",12),foreground="white",width=10,bg="gray",command=bul)
    urlArama.place(x=750 ,y=273)

    

def bul():
    global yt
    baslik1.place(x=120 , y=10)
    urlBaslik.place(x=10 , y=60)
    urlGiris.place(x=75 , y=65)
    urlArama.place(x=750 , y=63)

    url = str(urlGiris.get())
    yt = YouTube(url)
    müzikBaslik =  yt.title
    müzikTitle = Label(pencere)
    müzikTitle.config(text="VİDEO DETAYLARI ",font=("Arial",20),fg="black",bg="light blue")
    müzikTitle.place(x=330,y=120)

    canvas.delete("all")
    canvas.create_text(430,500,font=("Arial",15),text=müzikBaslik)

    indir = Button(pencere)
    indir.config(text="İNDİR",font=("Arial",12),fg="white",bg="gray",command=tekİndir,width=10)
    indir.place(x=750 , y=550)


def pBul():
    global p
    baslik1.place(x=120 , y=10)
    urlBaslik.place(x=10 , y=60)
    urlGiris.place(x=75 , y=65)
    urlArama.place(x=750 , y=63)

    url = str(urlGiris.get())
    p = Playlist(url)

    playlistTitle = Label(pencere)
    playlistTitle.config(text="PLAYLİST DETAYLARI ",font=("Arial",20),fg="black",bg="light blue")
    playlistTitle.place(x=300,y=120)

    k = 0
    for x in p.video_urls:
        print(x)
        k = k+10
        y = YouTube(x)
        print(y.title)
        canvas.create_text(50,200+k,font=("Arial",15),text=x)

    #canvas.delete("all")
    #canvas.create_text(430,500,font=("Arial",15),text=playlistBaslik)

    indir = Button(pencere)
    indir.config(text="İNDİR",font=("Arial",12),fg="white",bg="gray",command=playlistİndir,width=10)
    indir.place(x=750 , y=550)



def tekİndir():


    urlGiris.delete(0,150)

def playlistİndir():

    
    urlGiris.delete(0,150)




     

baslik = Label(pencere)
baslik.config(text="Yotube\'dan istediğiniz videoyu \n ses formatında inderebilirsiniz.", font=("Arial",25),foreground="black",background="light blue")
baslik.place(x=220, y=10)

baslik1 = Label(pencere)
baslik1.config(text="",font=("Arial",20),bg="light blue")
baslik1.place(x=210 , y=200)

secimPlaylist = Button(pencere)
secimPlaylist.config(text="Playlist için buraya tıklayınız.",font=("Arial",20),command=playlist)
secimPlaylist.place(x=30 , y=275)

secimTek = Button(pencere)
secimTek.config(text="Tek video için buraya tıklayınız.",font=("Arial",20),command=tek)
secimTek.place(x=460 , y=275)




"""urlBaslik = Label(pencere)
urlBaslik.config(text="URL",font=("Arial",20),foreground="black",background="light blue")
urlBaslik.place(x=10 ,y=70)

urlGiris = Entry(pencere)
urlGiris.config(font=("Arial",15),foreground="black",width=50,highlightbackground="purple")
urlGiris.place(x=75 ,y=75)

urlArama = Button(pencere)
urlArama.config(text="Bul",font=("Arial",12),foreground="white",width=10,bg="gray",command=bul)
urlArama.place(x=650 ,y=73)
"""

mainloop()
