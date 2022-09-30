import os
from os import read
from tkinter import *
import tkinter as tk
import webbrowser
from tkinter.font import BOLD
from tkinter import filedialog 

class generateHTML:

    def __init__(self):
         self.gui = Tk()

         self.gui.title("Notepad")

         self.gui.geometry("800x900")
         self.file = None
         # Menu
         mymenu = Menu(self.gui,bg="#a3e1f7",fg="black")
         File = Menu()
         Run = Menu()
         Tools = Menu()
         File.add_command(label="New",command=self.new_file)
         File.add_command(label="Open File",command=self.open_file)
         File.add_command(label="Create File",command=self.save_file)
         File.add_command(label="Save As",command=self.save_as)
         File.add_command(label="Exit",command=self.exit)
        
         Run.add_command(label="Run",command=self.runfile)

         Tools.add_command(label="Font Awesome - 2D Icons",command=self.fontawesome)
         Tools.add_command(label="Box Icons - 2D Icons",command=self.boxicons)
         Tools.add_command(label="Lord Icons - 3D Icons",command=self.lordicons)
         Tools.add_command(label="Png Guru - png img",command=self.pngimg)
         Tools.add_command(label="PngImg - png img",command=self.pngguru)
         Tools.add_command(label="Unsplash - HD img",command=self.unsplash)
         Tools.add_command(label="Squirly - SVG Generator",command=self.shapegenerator)
       
         mymenu.add_cascade(label="File",menu=File,font=("Ubuntu",14,BOLD))
         mymenu.add_cascade(label="Run",menu=Run,font=("Ubuntu",14,BOLD))
         mymenu.add_cascade(label="Tools",menu=Tools,font=("Ubuntu",14,BOLD))

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
        default_name = "index.html"
        if self.file != None:
            default_name = os.path.basename(self.file)

        data = self.text.get(1.0,END)
        f = open(default_name,'w')
        f.write(data)
    
    # Save As
    def save_as(self):
        f = filedialog.asksaveasfile(mode = "w",defaultextension=".txt")
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

    def fontawesome(self):
          webbrowser.open_new_tab('https://fontawesome.com/search?s=solid%2Cbrands')

    def boxicons(self):
          webbrowser.open_new_tab('https://boxicons.com/')

    def lordicons(self):
          webbrowser.open_new_tab('https://lordicon.com/')

    def pngimg(self):
          webbrowser.open_new_tab('https://pngtree.com/')

    def pngguru(self):
          webbrowser.open_new_tab('https://www.pngguru.in/')

    def unsplash(self):
          webbrowser.open_new_tab('https://unsplash.com/')

    def shapegenerator(self):
          webbrowser.open_new_tab('https://squircley.app/')
                
    """ Menu Buttons Ends """


    def options(self):
         self.option = Tk()
         self.option.title("HTML GENERATOR")
         self.option.geometry("800x900")
         self.option.config(bg="#daeef5")

         self.label = Label(self.option, text="!!! Generate HTML !!!",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.label.pack()
         self.label.place(x=270,y=20)
         
         self.imp = Label(self.option, text="Some Important Tags :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imp.pack()
         self.imp.place(x=50,y=100)

         # Template Button
         templatebtn = Button(self.option, text ="template",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.template)
         templatebtn.pack()
         templatebtn.place(x=50,y=150)
         self.gui.bind('<Control-t>',self.shortcuttemplate)

         # class Button
         classbtn = Button(self.option, text ='class= '' " ',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.classbtn)
         classbtn.pack()
         classbtn.place(x=170,y=150)

         # Id Button
         idbtn = Button(self.option, text ='id= '' " ',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.idbtn)
         idbtn.pack()
         idbtn.place(x=290,y=150)

         # html Button
         htmlbtn = Button(self.option, text ="<html>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.html)
         htmlbtn.pack()
         htmlbtn.place(x=380,y=150)

         # head Button
         headbtn = Button(self.option, text ="<head>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.head)
         headbtn.pack()
         headbtn.place(x=480,y=150)

         # title Button
         titlebtn = Button(self.option, text ="<title>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.title)
         titlebtn.pack()
         titlebtn.place(x=580,y=150)
         
         # body Button
         bodybtn = Button(self.option, text ="<body>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.body)
         bodybtn.pack()
         bodybtn.place(x=680,y=150)
         
         # heading Button
         headingbtn = Button(self.option, text ="<h?>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.heading)
         headingbtn.pack()
         headingbtn.place(x=50,y=200)
         self.gui.bind('<Control-h>',self.shortcutheading)
         
         # div Button
         divbtn = Button(self.option, text ="<div>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.div)
         divbtn.pack()
         divbtn.place(x=130,y=200)
         self.gui.bind('<Control-d>',self.shortcutdiv)

         # Paragraph Button
         pbtn = Button(self.option, text ="<p>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.p)
         pbtn.pack()
         pbtn.place(x=225,y=200)

         self.basics = Label(self.option, text="Some Basics Tags :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.basics.pack()
         self.basics.place(x=50,y=250)

         # Anchor Tag
         abtn = Button(self.option, text ="<a>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.a)
         abtn.pack()
         abtn.place(x=50,y=295)
         self.gui.bind('<Control-a>',self.shortcuta)

         # Bold Tag
         bbtn = Button(self.option, text ="<b>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.b)
         bbtn.pack()
         bbtn.place(x=130,y=295)

         # br Tag
         brbtn = Button(self.option, text ="<br>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.br)
         brbtn.pack()
         brbtn.place(x=210,y=295)

         # code Tag
         codebtn = Button(self.option, text ="<code>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.code)
         codebtn.pack()
         codebtn.place(x=300,y=295)

         # hr Tag
         hrbtn = Button(self.option, text ="<hr>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.hr)
         hrbtn.pack()
         hrbtn.place(x=410,y=295)

         # i Tag
         ibtn = Button(self.option, text ="<i>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.i)
         ibtn.pack()
         ibtn.place(x=500,y=295)

         # span Tag
         spanbtn = Button(self.option, text ="<span>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.span)
         spanbtn.pack()
         spanbtn.place(x=580,y=295)

         # u Tag
         ubtn = Button(self.option, text ="<u>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.u)
         ubtn.pack()
         ubtn.place(x=700,y=295)

         self.imgVid = Label(self.option, text="Images, Videos & Audio Tags :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imgVid.pack()
         self.imgVid.place(x=50,y=350)

         # img Tag
         imgbtn = Button(self.option, text ="<img>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.img)
         imgbtn.pack()
         imgbtn.place(x=50,y=400)

         # video Tag
         videobtn = Button(self.option, text ="<video>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.video)
         videobtn.pack()
         videobtn.place(x=150,y=400)

         # audio Tag
         audiobtn = Button(self.option, text ="<audio>",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.audio)
         audiobtn.pack()
         audiobtn.place(x=260,y=400)

         self.inputs = Label(self.option, text="Inputs Tags :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.inputs.pack()
         self.inputs.place(x=50,y=450)

         # button Input Tag
         btn_inp_btn = Button(self.option, text ='<input type="button">',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.btninp)
         btn_inp_btn.pack()
         btn_inp_btn.place(x=50,y=500)

         # email Input Tag
         email_inp_btn = Button(self.option, text ='<input type="email">',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.emailinp)
         email_inp_btn.pack()
         email_inp_btn.place(x=280,y=500)

         # File Input Tag
         file_inp_btn = Button(self.option, text ='<input type="file">',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.fileinp)
         file_inp_btn.pack()
         file_inp_btn.place(x=500,y=500)

         # number Input Tag
         number_inp_btn = Button(self.option, text ='<input type="number">',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.numinp)
         number_inp_btn.pack()
         number_inp_btn.place(x=50,y=550)

         # password Input Tag
         password_inp_btn = Button(self.option, text ='<input type="password">',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.passinp)
         password_inp_btn.pack()
         password_inp_btn.place(x=280,y=550)

         # password Input Tag
         text_inp_btn = Button(self.option, text ='<input type="text">',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.textinp)
         text_inp_btn.pack()
         text_inp_btn.place(x=530,y=550)

         self.tables = Label(self.option, text="Tables Tags :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.tables.pack()
         self.tables.place(x=50,y=600)

         # Table Template Tag
         table_template = Button(self.option, text ='Table Template',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.tabletemplate)
         table_template.pack()
         table_template.place(x=50,y=650)

         self.tables = Label(self.option, text="Tables Tags :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.tables.pack()
         self.tables.place(x=50,y=600)

         # Table Template Tag
         table_template = Button(self.option, text ='Table Template',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.tabletemplate)
         table_template.pack()
         table_template.place(x=50,y=650)

         self.lists = Label(self.option, text="Lists Tags :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.lists.pack()
         self.lists.place(x=50,y=700)

         # OL Lists Template Tag
         ol_template = Button(self.option, text ='OL lists',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.oltemplate)
         ol_template.pack()
         ol_template.place(x=50,y=750)

         # LI Lists Template Tag
         ul_template = Button(self.option, text ='UL lists',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.ultemplate)
         ul_template.pack()
         ul_template.place(x=150,y=750)

         self.others = Label(self.option, text="Others :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.others.pack()
         self.others.place(x=50,y=800)

         # Bootstrap CSS CDN 
         Bootstrap_css_cdn = Button(self.option, text ='Bootstrap CSS CDN',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.bootstrapCSS)
         Bootstrap_css_cdn.pack()
         Bootstrap_css_cdn.place(x=50,y=850)

         # Bootstrap JS CDN 
         Bootstrap_js_cdn = Button(self.option, text ='Bootstrap JS CDN',justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.bootstrapJS)
         Bootstrap_js_cdn.pack()
         Bootstrap_js_cdn.place(x=250,y=850)

      











         self.option.mainloop()

    def template(self):
          self.text.insert(INSERT,
          """<html>
            <head>
                        <link rel="stylesheet" href="">
            </head>
            <body>
            </body>
</html>
          """,'black')
          self.text.pack()
    def shortcuttemplate(self,e):
          self.text.insert(INSERT,
          """<html>
            <head>
                        <link rel="stylesheet" href="">
            </head>
            <body>
            </body>
</html>
          """,'black')
          self.text.pack()

    def classbtn(self):
            self.text.insert(INSERT,' class=""','black')
            self.text.pack()
    
    def idbtn(self):
            self.text.insert(INSERT,' id=""','black')
            self.text.pack()
    
    def html(self):
          self.text.insert(INSERT,"""<html>\n</html>""",'red')
          self.text.pack()
    
    def head(self):
          self.text.insert(INSERT,"""
          <head>
          </head>""")
          self.text.pack()
    
    def title(self):
          self.text.insert(INSERT,"""
          <title></title>""",'black')
          self.text.pack()

    def body(self):
          self.text.insert(INSERT,"""
          <body>
          </body>""",'red')
          self.text.pack()
    
    def heading(self):
          self.text.insert(INSERT,"""
          \t<h></h>""",'black')
          self.text.pack()
    def shortcutheading(self,e):
          self.text.insert(INSERT,"""
          \t<h></h>""",'black')
          self.text.pack()
    
    def div(self):
          self.text.insert(INSERT,"""
          \t<div></div>""",'black')
          self.text.pack()
    def shortcutdiv(self,e):
          self.text.insert(INSERT,"""
          \t<div></div>\n""",'black')
          self.text.pack()

    def p(self):
          self.text.insert(INSERT,"""<p></p>""",'black')
          self.text.pack()

    def a(self):
          self.text.insert(INSERT,"""\t<a></a>""",'black')
          self.text.pack()
    def shortcuta(self,e):
          self.text.insert(INSERT,""" \t<a></a>""",'black')
          self.text.pack()

    def b(self):
          self.text.insert(INSERT,"""\t<b></b>""",'black')
          self.text.pack()

    def br(self):
          self.text.insert(INSERT,"""\t<br>""",'black')
          self.text.pack()

    def code(self):
          self.text.insert(INSERT,"""\t<code></code>""",'black')
          self.text.pack()
    
    def hr(self):
          self.text.insert(INSERT,"""\t<hr>""",'black')
          self.text.pack()

    def i(self):
          self.text.insert(INSERT,"""\t<i></i>""",'black')
          self.text.pack()

    def span(self):
          self.text.insert(INSERT,"""\t<span></span>""",'black')
          self.text.pack()

    def u(self):
          self.text.insert(INSERT,"""\t<u></u>""",'black')
          self.text.pack()

    def img(self):
          self.text.insert(INSERT,"""\t<img src="" alt="">""",'black')
          self.text.pack()

    def video(self):
          self.text.insert(INSERT,"""\t<video src=""></video>""",'black')
          self.text.pack()

    def audio(self):
          self.text.insert(INSERT,"""\t<audio src=""></audio>""",'black')
          self.text.pack()

    def btninp(self):
          self.text.insert(INSERT,"""\t<input type="button">""",'black')
          self.text.pack()

    def emailinp(self):
          self.text.insert(INSERT,"""\t<input type="email">""",'black')
          self.text.pack()

    def fileinp(self):
          self.text.insert(INSERT,"""\t<input type="file">""",'black')
          self.text.pack()

    def numinp(self):
          self.text.insert(INSERT,"""\t<input type="number">""",'black')
          self.text.pack()

    def passinp(self):
          self.text.insert(INSERT,"""\t<input type="password">""",'black')
          self.text.pack()

    def textinp(self):
          self.text.insert(INSERT,"""\t<input type="text">""",'black')
          self.text.pack()

    def tabletemplate(self):
          self.text.insert(INSERT,"""\t<table>
\t\t<tr>
\t\t<th></th>
\t\t</tr>
\t\t<tr>
\t\t<td></td>
\t\t</tr>
\t</table>""",'black')
          self.text.pack()

    def oltemplate(self):
          self.text.insert(INSERT,"""\t<ol>
\t\t<li></li>
\t</ol>""",'black')
          self.text.pack()

    def ultemplate(self):
          self.text.insert(INSERT,"""\t<ul>
\t\t<li></li>
\t</ul>""",'black')
          self.text.pack()

    def bootstrapCSS(self):
          self.text.insert(INSERT,"""\n\t<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">\n""",'black')
          self.text.pack()

    def bootstrapJS(self):
          self.text.insert(INSERT,"""\n\t<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>\n""",'black')
          self.text.pack()

# obj = generateHTML()