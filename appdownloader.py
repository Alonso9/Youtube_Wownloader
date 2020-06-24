#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pytube import YouTube
from pytube.cli import on_progress
from tkinter import * 
from tkinter import messagebox


url = ""

#-------------------------YouTube----------------------------------#
class Youtube():
    
    global url
    
    def __init__(self):
        print(url)
        print("-----------------YouTube downloader-----------------")
        
        self.url = url 
        
    def prepare_download(self):
        print("-------------------Preparing to download.------------------")
        self.yt = YouTube(self.url, on_progress_callback=on_progress) #Barra de descarga
        
    def start_download(self):
        print("\n----------------Starting the download----------------------")
        self.yt.streams.first().download()
        print("\n---------------------Full download--------------------")
          
def action():
    obj = Youtube()
    obj.prepare_download()
    obj.start_download()

#---------------------------GUI-------------------------------------#  
       
root = Tk()
root.title("Youtube Downloader")
root.resizable(0,0)
root.geometry('250x200')

#Create the menu 
barraMenu = Menu(root)
root.config(menu=barraMenu) 

#function menu
def buttonExit():
    menuValue = messagebox.askquestion("Exit", "Do you like to exit?") 
    if(menuValue=="yes"):
        root.destroy()
        
def buttonLicense():
    messagebox.showwarning("License", "GNU licensed product")
    
def buttonDeveloper():
    messagebox.showinfo("Information", """This app was devloped in
     Python language programing by Alonso using Pytube and tkinter""")
     
def closeFile():
    valor = messagebox.askretrycancel("Retry", "Can't close this file'")

def buttonHelp():
    messagebox.showinfo("Information", """This app is useful to download youtube videos safely""")

def buttonInstruction():
    messagebox.showinfo("Information", "You only need to paste the url and the app start to download the video")

archivoFile = Menu(barraMenu, tearoff=0) #elementos del menu 
archivoFile.add_command(label="Cancel", command=closeFile)
archivoFile.add_command(label="Exit", command=buttonExit)
barraMenu.add_cascade(label="File", menu=archivoFile) #Agregamos  texto

archivoProgrammer = Menu(barraMenu, tearoff=0) #elementos del menu 
archivoProgrammer.add_command(label="About of app:", command=buttonDeveloper)
archivoProgrammer.add_command(label="license", command=buttonLicense)
barraMenu.add_cascade(label="developer", menu=archivoProgrammer) #Agregamos  texto

archivoAyuda = Menu(barraMenu, tearoff=0) #elementos del menu 
archivoAyuda.add_command(label="About of:", command=buttonHelp)
barraMenu.add_cascade(label="Help", menu=archivoAyuda) #Agregamos  texto

archivoAyuda = Menu(barraMenu, tearoff=0) #elementos del menu 
archivoAyuda.add_command(label="Instruction:", command=buttonInstruction)
barraMenu.add_cascade(label="Instructions", menu=archivoAyuda) #Agregamos  texto


#create the Frame
myFrame = Frame(root)
myFrame.pack()

readurl = StringVar() 

def button_action(): #https://www.youtube.com/watch?v=Tasg3FD3h2M
    global url
    var_string = cuadroUrl.get()
    url = var_string
    action()
    messagebox.showinfo("Information", "The video has been downloaded!")
    buttonExit()
    cuadroUrl.delete(0, END)
    
#Entry URL

cuadroUrl = Entry(myFrame, textvariable=readurl)
d = readurl.get()
cuadroUrl.grid(row=0, column=1, padx=5, pady=30)
labelUrl = Label(myFrame, text="URL: ").grid(row=0, column=0, padx=5, pady=5)

#Sumit Buton

btn = Button(root, text="Start Download", bd='5', bg="orange", command=button_action)
btn.pack(side='top')

mainloop()
