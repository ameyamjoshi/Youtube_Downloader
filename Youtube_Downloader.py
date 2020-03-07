from pytube import YouTube
from tkinter import *

def Download():
    link=a.get()
    path=b.get()
    yt=YouTube(link)
    yt.title
    stream = yt.streams.first()
    stream.download(path)
    return"Done"



main=Tk()
main.title("Downloader")
main.geometry('300x300')
a=StringVar()
b=StringVar()
lblAmount = Label(main, text = 'Link:').grid(row = 0, column = 0, padx = 30, pady = 10)
entAmount = Entry(main, textvariable = a).grid(row = 0, column = 1)

lblIntRate = Label(main, text = 'Path:').grid(row = 1, column = 0, padx = 30, pady = 10)
entIntRate = Entry(main, textvariable = b).grid(row = 1, column = 1)

btn = Button(main, text = 'Download Completed', command=Download).grid(row = 5, column = 1)
main.mainloop()
