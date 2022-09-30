import os
import re
from os import read
from tkinter import *
import tkinter as tk
import webbrowser
from tkinter.font import BOLD
from tkinter import filedialog 

class generateJAVASCRIPT:

    def __init__(self):
         self.gui = Tk()

         self.gui.title("Notepad")

         self.gui.geometry("800x700")
         self.file = None
         # Menu
         mymenu = Menu(self.gui,bg="#a3e1f7",fg="black")
         File = Menu()
         Run = Menu()
         Show = Menu()

         File.add_command(label="New",command=self.new_file)
         File.add_command(label="Open File",command=self.open_file)
         File.add_command(label="Create File",command=self.save_file)
         File.add_command(label="Save As",command=self.save_as)
         File.add_command(label="Exit",command=self.exit)
        
         Run.add_command(label="Run",command=self.runfile)

         Show.add_command(label="class",command=self.getclass)
         Show.add_command(label="id",command=self.getid)
       
         mymenu.add_cascade(label="File",menu=File,font=("Ubuntu",14,BOLD))
         mymenu.add_cascade(label="Run",menu=Run,font=("Ubuntu",14,BOLD))
         mymenu.add_cascade(label="Show",menu=Show,font=("Ubuntu",14,BOLD))
         self.gui.config(menu = mymenu)

         self.text = Text(self.gui,wrap=WORD,bg="#b8f9ff",font=("Ubuntu",14))
         self.text.pack(expand=TRUE,fill=BOTH)

         self.text.tag_config('red', foreground="red")
         self.text.tag_config('black', foreground="black")
         self.text.tag_config('green', foreground="green")

         self.options()
         self.gui.mainloop()
    
    """ Menu Buttons Start """
    def new_file(self):
        self.text.delete(1.0,END)
    
    # Open File
    def open_file(self):
        file_name = filedialog.askopenfile(mode = "r")
        data = file_name.read()
        self.text.delete(1.0,END)
        self.text.insert(1.0,data)
    
    # Save File
    def save_file(self):
        default_name = "style.css"
        if self.file != None:
            default_name = os.path.basename(self.file)

        data = self.text.get(1.0,END)
        f = open(default_name,'w')
        f.write(data)
    
    # Save As
    def save_as(self):
        f = filedialog.asksaveasfile(mode = "w",defaultextension=".js")
        data = self.text.get(1.0,END)
    
    def exit(self):
        self.gui.destroy()
    
    def runfile(self):
          try:
                file = os.path.isfile('./index.html')
                if (file == True):
                      webbrowser.open_new_tab('index.html')
                else:
                     raise Exception
          except Exception:
                self.Errorgui = Tk()
                self.Errorgui.title("Error")
                self.Errorgui.geometry("600x120")
                self.Errorlabel = Label(self.Errorgui, text="!!! Error : Please Create the File First !!!",font=("Ubuntu",20,BOLD),fg='#000')
                self.Errorlabel.pack()
                self.Errorlabel.place(x=50,y=30)
                self.Errorgui.mainloop()

    def getclass(self):
        className = []
        textfile = open('index.html', 'r')
        pattern = r'class="\w*"'
        for line in textfile:
            pat = re.findall(pattern,line)
            if len(pat) != 0:
               name = pat[0][7:-1]
               className.append(name)

        self.classgui = Tk()
        self.classgui.title("class names")
        self.classgui.geometry("400x400")
        self.classNameText = Text(self.classgui,wrap=WORD,font=("Ubuntu",14),bg="#daeef5")
        self.classNameText.pack(expand=TRUE,fill=BOTH)
        self.classNameText.insert(INSERT,"Class Names : \n",'black')
        self.classNameText.pack()
        
        for i in className:
            self.classNameText.insert(INSERT,i+"\n",'black')
            self.classNameText.pack()

        self.classgui.mainloop()

    def getid(self):
        idName = []
        textfile = open('index.html', 'r')
        pattern = r'id="\w*"'
        for line in textfile:
            pat = re.findall(pattern,line)
            if len(pat) != 0:
               name = pat[0][4:-1]
               idName.append(name)

        self.idgui = Tk()
        self.idgui.title("Id names")
        self.idgui.geometry("400x400")
        self.idNameText = Text(self.idgui,wrap=WORD,font=("Ubuntu",14),bg="#daeef5")
        self.idNameText.pack(expand=TRUE,fill=BOTH)
        self.idNameText.insert(INSERT,"Id Names : \n",'black')
        self.idNameText.pack()
        
        for i in idName:
            self.idNameText.insert(INSERT,i+"\n",'black')
            self.idNameText.pack()

        self.idgui.mainloop()
        


    """ Menu Buttons Ends """
    
    def options(self):
         self.option = Tk()
         self.option.title("JAVASCRIPT GENERATOR")
         self.option.geometry("800x750")
         self.option.config(bg="#daeef5")

         self.label = Label(self.option, text="!!! Generate JAVASCRIPT !!!",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.label.pack()
         self.label.place(x=220,y=20)
                  
         self.imp = Label(self.option, text="Some Important's :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imp.pack()
         self.imp.place(x=50,y=100)

        # Let Button
         letbtn = Button(self.option, text ="let",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.let)
         letbtn.pack()
         letbtn.place(x=50,y=150)

        # Const Button
         constbtn = Button(self.option, text ="const",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.const)
         constbtn.pack()
         constbtn.place(x=120,y=150)

        # Let Button
         varbtn = Button(self.option, text ="var",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.var)
         varbtn.pack()
         varbtn.place(x=220,y=150)

        # Object Button
         objectbtn = Button(self.option, text ="object",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.object)
         objectbtn.pack()
         objectbtn.place(x=300,y=150)

        # Function Button
         functionbtn = Button(self.option, text ="function",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.function)
         functionbtn.pack()
         functionbtn.place(x=300,y=150)

        # Arrow Function Button
         functionbtn = Button(self.option, text ="()=>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.Arrowfunction)
         functionbtn.pack()
         functionbtn.place(x=420,y=150)

        # Array Button
         arraybtn = Button(self.option, text ="array",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.array)
         arraybtn.pack()
         arraybtn.place(x=500,y=150)
       
         self.conditional = Label(self.option, text="Conditional Statement's & Loops :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.conditional.pack()
         self.conditional.place(x=50,y=200)

        # If Button
         ifbtn = Button(self.option, text ="if",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.iff)
         ifbtn.pack()
         ifbtn.place(x=50,y=250)

        # If else if Button
         ifelsebtn = Button(self.option, text ="if else",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.ifelse)
         ifelsebtn.pack()
         ifelsebtn.place(x=110,y=250)

        # If else if Button
         ifelseifbtn = Button(self.option, text ="if else if",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.ifelseif)
         ifelseifbtn.pack()
         ifelseifbtn.place(x=205,y=250)

        # switch Button
         switchbtn = Button(self.option, text ="switch",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.switch)
         switchbtn.pack()
         switchbtn.place(x=320,y=250)

        # for Button
         forbtn = Button(self.option, text ="for",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.forr)
         forbtn.pack()
         forbtn.place(x=420,y=250)

        # for eachButton
         foreachbtn = Button(self.option, text ="foreach",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.foreach)
         foreachbtn.pack()
         foreachbtn.place(x=500,y=250)

        # while Button
         whilebtn = Button(self.option, text ="while",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.whilee)
         whilebtn.pack()
         whilebtn.place(x=610,y=250)

        # Do while Button
         dowhilebtn = Button(self.option, text ="do while",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.dowhile)
         dowhilebtn.pack()
         dowhilebtn.place(x=700,y=250)
                           
         self.strings = Label(self.option, text="Strings Methods :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.strings.pack()
         self.strings.place(x=50,y=300)

        # length Button
         lengthbtn = Button(self.option, text ="length",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.length)
         lengthbtn.pack()
         lengthbtn.place(x=50,y=350)

        # slice Button
         slicebtn = Button(self.option, text ="slice",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.slice)
         slicebtn.pack()
         slicebtn.place(x=150,y=350)

        # substring Button
         substringbtn = Button(self.option, text ="substring",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.substring)
         substringbtn.pack()
         substringbtn.place(x=240,y=350)

        # substr Button
         substrbtn = Button(self.option, text ="substr",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.substr)
         substrbtn.pack()
         substrbtn.place(x=370,y=350)

        # replace Button
         replacebtn = Button(self.option, text ="replace",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.replace)
         replacebtn.pack()
         replacebtn.place(x=470,y=350)

        # uppercase Button
         uppercasebtn = Button(self.option, text ="uppercase",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.uppercase)
         uppercasebtn.pack()
         uppercasebtn.place(x=580,y=350)

        # uppercase Button
         lowercasebtn = Button(self.option, text ="lowercase",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.lowercase)
         lowercasebtn.pack()
         lowercasebtn.place(x=50,y=400)

        # concat Button
         concatbtn = Button(self.option, text ="concat",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.concat)
         concatbtn.pack()
         concatbtn.place(x=185,y=400)

        # trim Button
         trimbtn = Button(self.option, text ="trim",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.trim)
         trimbtn.pack()
         trimbtn.place(x=290,y=400)

        # charAt Button
         charAtbtn = Button(self.option, text ="charAt",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.charAt)
         charAtbtn.pack()
         charAtbtn.place(x=385,y=400)

        # split Button
         splitbtn = Button(self.option, text ="split",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.split)
         splitbtn.pack()
         splitbtn.place(x=495,y=400)
                           
         self.arrays = Label(self.option, text="Array Methods :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.arrays.pack()
         self.arrays.place(x=50,y=450)

        # toString Button
         toStringbtn = Button(self.option, text ="toString",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.toString)
         toStringbtn.pack()
         toStringbtn.place(x=50,y=500)

        # join Button
         joinbtn = Button(self.option, text ="join",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.join)
         joinbtn.pack()
         joinbtn.place(x=170,y=500)

        # pop Button
         popbtn = Button(self.option, text ="pop",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.pop)
         popbtn.pack()
         popbtn.place(x=255,y=500)

        # push Button
         pushbtn = Button(self.option, text ="push",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.push)
         pushbtn.pack()
         pushbtn.place(x=255,y=500)

        # shift Button
         shiftbtn = Button(self.option, text ="shift",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.shift)
         shiftbtn.pack()
         shiftbtn.place(x=350,y=500)

        # unshift Button
         unshiftbtn = Button(self.option, text ="unshift",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.unshift)
         unshiftbtn.pack()
         unshiftbtn.place(x=450,y=500)

        # arrsplice Button
         arrsplicebtn = Button(self.option, text ="splice",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.arrsplice)
         arrsplicebtn.pack()
         arrsplicebtn.place(x=560,y=500)

        # arrslice Button
         arrslicebtn = Button(self.option, text ="slice",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.arrslice)
         arrslicebtn.pack()
         arrslicebtn.place(x=665,y=500)

        # sort Button
         sortbtn = Button(self.option, text ="sort",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.sort)
         sortbtn.pack()
         sortbtn.place(x=50,y=550)
                           
         self.dom = Label(self.option, text="DOM Maniplations :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.dom.pack()
         self.dom.place(x=50,y=600)

        # byID Button
         getIDbtn = Button(self.option, text ="getElementByID",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.getID)
         getIDbtn.pack()
         getIDbtn.place(x=50,y=650)

        # byCLASS Button
         getClassbtn = Button(self.option, text ="getElementsByClassName",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.getclasss)
         getClassbtn.pack()
         getClassbtn.place(x=250,y=650)

        # Query Selector Button
         querySelectorbtn = Button(self.option, text ="querySelector",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.query)
         querySelectorbtn.pack()
         querySelectorbtn.place(x=530,y=650)

    def let(self):
        self.text.insert(INSERT,"""let """)  

    def const(self):
        self.text.insert(INSERT,"""const """)        

    def var(self):
        self.text.insert(INSERT,"""var """)        

    def object(self):
        self.text.insert(INSERT,"""var  = {\n\n}""")        

    def function(self):
        self.text.insert(INSERT,"""function  () {\n\n}""")        

    def Arrowfunction(self):
        self.text.insert(INSERT,"""()=> {\n\n}""")        

    def array(self):
        self.text.insert(INSERT,"""const  = []""")        

    def iff(self):
        self.text.insert(INSERT,"""if () {\n\n}""")        

    def ifelse(self):
        self.text.insert(INSERT,"""if () {\n\n} \nelse {\n\n}""")        

    def ifelseif(self):
        self.text.insert(INSERT,"""if () {\n\n} \nelse if () {\n\n}\nelse {\n\n}""")        

    def switch(self):
        self.text.insert(INSERT,"""switch () {\ncase  :\n\nbreak;\ndefault:\n\n}""")
    
    def forr(self):
        self.text.insert(INSERT,"""for ( , , ){\n\n}""")        
    
    def foreach(self):
        self.text.insert(INSERT,""".foreach(){\n\n}""")        
    
    def whilee(self):
        self.text.insert(INSERT,"""while () {\n\n}""")        
    
    def dowhile(self):
        self.text.insert(INSERT,"""do {\n\n}\nwhile ();""")        
    
    def length(self):
        self.text.insert(INSERT,""".length;""")        
    
    def slice(self):
        self.text.insert(INSERT,""".slice( , );""")        
    
    def substring(self):
        self.text.insert(INSERT,""".substring( , );""")        
    
    def substr(self):
        self.text.insert(INSERT,""".substr( , );""")        
    
    def replace(self):
        self.text.insert(INSERT,""".replace( , );""")        
    
    def uppercase(self):
        self.text.insert(INSERT,""".toUpperCase();""")        
    
    def lowercase(self):
        self.text.insert(INSERT,""".toLowerCase();""")        
    
    def concat(self):
        self.text.insert(INSERT,""".concat( , );""")        
    
    def trim(self):
        self.text.insert(INSERT,""".trim();""")        
    
    def charAt(self):
        self.text.insert(INSERT,""".charAt();""")        
    
    def split(self):
        self.text.insert(INSERT,""".split();""")        
    
    def toString(self):
        self.text.insert(INSERT,""".toString();""")        
    
    def join(self):
        self.text.insert(INSERT,""".join();""")        
    
    def pop(self):
        self.text.insert(INSERT,""".pop();""")        
    
    def push(self):
        self.text.insert(INSERT,""".push();""")        
    
    def shift(self):
        self.text.insert(INSERT,""".shift();""")        
    
    def unshift(self):
        self.text.insert(INSERT,""".unshift();""")        
    
    def arrsplice(self):
        self.text.insert(INSERT,""".splice( , );""")        
    
    def arrslice(self):
        self.text.insert(INSERT,""".slice( , );""")        
    
    def sort(self):
        self.text.insert(INSERT,""".sort();""")        
    
    def getID(self):
        self.text.insert(INSERT,""".getElementById() ;""")        
    
    def getclasss(self):
        self.text.insert(INSERT,""".getElementByClassName() ;""")        
    
    def query(self):
        self.text.insert(INSERT,""".querySelector() ;""")        


        

# obj = generateJAVASCRIPT()