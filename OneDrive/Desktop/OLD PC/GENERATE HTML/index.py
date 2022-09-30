from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from htmlInterface import generateHTML
from cssInterface import generateCSS
from javascriptInterface import generateJAVASCRIPT
from notepad import GUI
from PIL import ImageTk, Image

class Interface:

    def __init__(self):
        
        self.interface = Tk()
        self.interface.title("webGenie")
        self.interface.geometry("500x500")
        self.interface.config(bg="#daeef5")

        text= Image.open("text.png")
        renderr = ImageTk.PhotoImage(text)
        imgg = Label(self.interface, image=renderr,bg="#daeef5")
        imgg.place(x=20, y=80)
        load= Image.open("genie.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.interface, image=render,bg="#daeef5")
        img.place(x=330, y=10)

        # html Button
        htmlbtn = Button(self.interface, text ="HTML Generator",justify=CENTER,font=("Ubuntu",12,BOLD),fg="#1b85c2",bg="#fff",relief=RAISED,command=self.htmlGenerator)
        htmlbtn.pack()
        htmlbtn.place(x=170,y=250)

        # css Button
        cssbtn = Button(self.interface, text ="CSS Generator",justify=CENTER,font=("Ubuntu",12,BOLD),fg="#1b85c2",bg="#fff",relief=RAISED,command=self.cssGenerator)
        cssbtn.pack()
        cssbtn.place(x=180,y=300)

        # javasctipt Button
        javascriptbtn = Button(self.interface, text ="JAVASCRIPT Generator",justify=CENTER,font=("Ubuntu",12,BOLD),fg="#1b85c2",bg="#fff",relief=RAISED,command=self.javascriptGenerator)
        javascriptbtn.pack()
        javascriptbtn.place(x=140,y=350)
        
        # text edito Button
        textbtn = Button(self.interface, text ="Text Editor",justify=CENTER,font=("Ubuntu",12,BOLD),fg="#1b85c2",bg="#fff",relief=RAISED,command=self.notepad)
        textbtn.pack()
        textbtn.place(x=190,y=400)

        self.interface.mainloop()

    def htmlGenerator(self):
        self.interface.destroy()
        obj = generateHTML()

    def cssGenerator(self):
        self.interface.destroy()
        obj = generateCSS()
    
    def javascriptGenerator(self):
        self.interface.destroy()
        obj = generateJAVASCRIPT()

    def notepad(self):
        self.interface.destroy()
        obj = GUI()

obj = Interface()