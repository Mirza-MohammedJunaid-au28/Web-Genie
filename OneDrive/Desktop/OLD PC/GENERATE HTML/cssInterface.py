import os
import re
from os import read
from tkinter import *
import tkinter as tk
import webbrowser
from tkinter.font import BOLD
from tkinter import filedialog 

class generateCSS:

    def __init__(self):
         self.gui = Tk()

         self.gui.title("Notepad")

         self.gui.geometry("800x900")
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
        f = filedialog.asksaveasfile(mode = "w",defaultextension=".css")
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
        print(className)

        self.classgui = Tk()
        self.classgui.title("class names")
        self.classgui.geometry("400x400")
        self.classNameText = Text(self.classgui,wrap=WORD,bg="#daeef5",font=("Ubuntu",14))
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
        print(idName)

        self.idgui = Tk()
        self.idgui.title("Id names")
        self.idgui.geometry("400x400")
        self.idNameText = Text(self.idgui,wrap=WORD,bg="#daeef5",font=("Ubuntu",14))
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
         self.option.title("CSS GENERATOR")
         self.option.geometry("800x700")
         self.option.config(bg="#daeef5")

         self.label = Label(self.option, text="!!! Generate CSS !!!",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.label.pack()
         self.label.place(x=270,y=20)
                  
         self.imp = Label(self.option, text="Some Important Tags :",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imp.pack()
         self.imp.place(x=50,y=100)

        # Template Button
         templatebtn = Button(self.option, text ="intro template",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.template)
         templatebtn.pack()
         templatebtn.place(x=50,y=150)

        # Bracket Button
         bracketbtn = Button(self.option, text ="{ }",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.bracket)
         bracketbtn.pack()
         bracketbtn.place(x=210,y=150)

        # Margin Button
         marginbtn = Button(self.option, text ="margin",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.margin)
         marginbtn.pack()
         marginbtn.place(x=280,y=150)
         self.gui.bind('<Control-m>',self.shortcutmargin)

        # Padding Button
         padddingbtn = Button(self.option, text ="padding",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.padding)
         padddingbtn.pack()
         padddingbtn.place(x=380,y=150)
         self.gui.bind('<Control-p>',self.shortcutpadding)
         
         #Body Button
         bodybtn = Button(self.option, text ="body",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.body)
         bodybtn.pack()
         bodybtn.place(x=480,y=150)
         
         self.imp = Label(self.option, text="Position:",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imp.pack()
         self.imp.place(x=50,y=200)
         
         #static Button
         staticbtn = Button(self.option, text ="static",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.static)
         staticbtn.pack()
         staticbtn.place(x=50,y=250)
         
         #relative Button
         relativebtn = Button(self.option, text ="relative",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.relative)
         relativebtn.pack()
         relativebtn.place(x=110,y=250)
         
         #fixed Button
         fixedbtn = Button(self.option, text ="fixed",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.fixed)
         fixedbtn.pack()
         fixedbtn.place(x=190,y=250)
         
         #absolute Button
         absolutebtn = Button(self.option, text ="absolute",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.absolute)
         absolutebtn.pack()
         absolutebtn.place(x=250,y=250)
         
         #sticky Button
         stickybtn = Button(self.option, text ="sticky",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.sticky)
         stickybtn.pack()
         stickybtn.place(x=340,y=250)
         
         #Top Button
         topbtn = Button(self.option, text ="top",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.top)
         topbtn.pack()
         topbtn.place(x=410,y=250)
         
         #Bottom Button
         bottombtn = Button(self.option, text ="bottom",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.bottom)
         bottombtn.pack()
         bottombtn.place(x=460,y=250)
         
         #Left Button
         leftbtn = Button(self.option, text ="left",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.left)
         leftbtn.pack()
         leftbtn.place(x=540,y=250)
         
         #Right Button
         rightbtn = Button(self.option, text ="right",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.right)
         rightbtn.pack()
         rightbtn.place(x=590,y=250)
         
         #AlignItems Button
         alignitemsbtn = Button(self.option, text ="align-items",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.alignitems)
         alignitemsbtn.pack()
         alignitemsbtn.place(x=650,y=250)
         
         #LineHeight Button
         lineheightbtn = Button(self.option, text ="line-height",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.lineheight)
         lineheightbtn.pack()
         lineheightbtn.place(x=760,y=250)
         
         self.imp = Label(self.option, text="Display:",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imp.pack()
         self.imp.place(x=50,y=300) 
         
         #displaynone Button
         displaynonebtn = Button(self.option, text ="display-none",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.displaynone)
         displaynonebtn.pack()
         displaynonebtn.place(x=50,y=350)
         
         #displayinline Button
         displayinlinebtn = Button(self.option, text ="display-inline",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.displayinline)
         displayinlinebtn.pack()
         displayinlinebtn.place(x=170,y=350)
         
         #displayblock Button
         displayblockbtn = Button(self.option, text ="display-block",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.displayblock)
         displayblockbtn.pack()
         displayblockbtn.place(x=290,y=350)
         
         #displayinlineblock Button
         displayinlineblockbtn = Button(self.option, text ="display-inline-block",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.displayinlineblock)
         displayinlineblockbtn.pack()
         displayinlineblockbtn.place(x=410,y=350)
         
         #color Button
         colorbtn = Button(self.option, text ="color",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.color)
         colorbtn.pack()
         colorbtn.place(x=50,y=400)
         
         #display Button
         displaybtn = Button(self.option, text ="display",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.display)
         displaybtn.pack()
         displaybtn.place(x=110,y=400)
         
         #transition Button
         transitionbtn = Button(self.option, text ="transition",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.transition)
         transitionbtn.pack()
         transitionbtn.place(x=190,y=400)
         
         #background Button
         backgroundbtn = Button(self.option, text ="background",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.background)
         backgroundbtn.pack()
         backgroundbtn.place(x=290,y=400)
         
         #backgroundimg Button
         backgroundimgbtn = Button(self.option, text ="backgroundimg",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.backgroundimg)
         backgroundimgbtn.pack()
         backgroundimgbtn.place(x=410,y=400)
         
         #font Button
         fontbtn = Button(self.option, text ="font",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.font)
         fontbtn.pack()
         fontbtn.place(x=550,y=400)
         
         #fontsize Button
         fontsizebtn = Button(self.option, text ="fontsize",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.fontsize)
         fontsizebtn.pack()
         fontsizebtn.place(x=600,y=400)
         
         #whitespace Button
         whitespacebtn = Button(self.option, text ="whitespace",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.whitespace)
         whitespacebtn.pack()
         whitespacebtn.place(x=680,y=400)
         
         #justify Button
         justifybtn = Button(self.option, text ="justify",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.justify)
         justifybtn.pack()
         justifybtn.place(x=790,y=400)
         
         self.imp = Label(self.option, text="Border:",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imp.pack()
         self.imp.place(x=50,y=450)
         
         #border Button
         borderbtn = Button(self.option, text ="border",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.border)
         borderbtn.pack()
         borderbtn.place(x=50,y=500)
         
         #bordercolor Button
         bordercolorbtn = Button(self.option, text ="bordercolor",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.bordercolor)
         bordercolorbtn.pack()
         bordercolorbtn.place(x=120,y=500)
         
         #borderstyle Button
         borderstylebtn = Button(self.option, text ="borderstyle",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.borderstyle)
         borderstylebtn.pack()
         borderstylebtn.place(x=230,y=500)
         
         #borderwidth Button
         borderwidthbtn = Button(self.option, text ="borderwidth",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.borderwidth)
         borderwidthbtn.pack()
         borderwidthbtn.place(x=340,y=500)
         
         self.imp = Label(self.option, text="Grid:",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imp.pack()
         self.imp.place(x=50,y=550)
         
         #Grid Button
         gridbtn = Button(self.option, text ="grid",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.grid)
         gridbtn.pack()
         gridbtn.place(x=50,y=600)
         
         #Gap Button
         gapbtn = Button(self.option, text ="gap",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.gap)
         gapbtn.pack()
         gapbtn.place(x=100,y=600)
         
         #Grid-area Button
         gridareabtn = Button(self.option, text ="grid-area",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.gridarea)
         gridareabtn.pack()
         gridareabtn.place(x=150,y=600)
         
         #Grid-row Button
         gridrowbtn = Button(self.option, text ="grid-row",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.gridrow)
         gridrowbtn.pack()
         gridrowbtn.place(x=250,y=600)
         
         #Grid-column Button
         gridcolumnbtn = Button(self.option, text ="grid-column",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.gridcolumn)
         gridcolumnbtn.pack()
         gridcolumnbtn.place(x=350,y=600)
         
         
         self.imp = Label(self.option, text="Flex:",font=("Ubuntu",20,BOLD),fg='#000',bg="#daeef5")
         self.imp.pack()
         self.imp.place(x=50,y=650)
         
         #Flex Button
         flexbtn = Button(self.option, text ="Flex",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.flex)
         flexbtn.pack()
         flexbtn.place(x=50,y=700)
         
         #flex-wrap Button
         flexwrapbtn = Button(self.option, text ="Flex-wrap",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.flexwrap)
         flexwrapbtn.pack()
         flexwrapbtn.place(x=120,y=700)
         
         #flex-basis Button
         flexbasisbtn = Button(self.option, text ="Flex-basis",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.flexbasis)
         flexbasisbtn.pack()
         flexbasisbtn.place(x=220,y=700)
         
         #flex-flow Button
         flexflowbtn = Button(self.option, text ="Flex-flow",justify=CENTER,font=("Ubuntu",12,BOLD),fg="purple",bg="#fff",relief=RAISED,command=self.flexflow)
         flexflowbtn.pack()
         flexflowbtn.place(x=320,y=700)
         

        
    def template(self):
          self.text.insert(INSERT,
          """*{
margin : 0;
padding : 0;
box-sizing : border-box;
}
""",'black')
          self.text.pack()
    
    def bracket(self):
        self.text.insert(INSERT,"""{\n\n}""")
    
    def body(self):
        self.text.insert(INSERT,"""body{\n\n}""")
    
    def margin(self):
        self.text.insert(INSERT,"""margin : """)
    def top(self):
        self.text.insert(INSERT,"""top: 00px;""")    
    def bottom(self):
        self.text.insert(INSERT,"""bottom: 00px;""")
    def left(self):
        self.text.insert(INSERT,"""left: 00px;""")  
    def right(self):
        self.text.insert(INSERT,"""right: 00px;""")    
    def alignitems(self):
        self.text.insert(INSERT,"""align-items: ;""")    
    def lineheight(self):
        self.text.insert(INSERT,"""line-height:0 ;""") 
        
        
    def static(self):
        self.text.insert(INSERT,""" position: static;""")
    def relative(self):
        self.text.insert(INSERT,""" position: relative;""")
    def fixed(self):
        self.text.insert(INSERT,""" position: fixed;""")
    def absolute(self):
        self.text.insert(INSERT,""" position: absolute;""")
    def sticky(self):
        self.text.insert(INSERT,""" position: sticky;""")  
    def displaynone(self):
        self.text.insert(INSERT,""" display: none;""")
    def displayinline(self):
        self.text.insert(INSERT,""" display: inline;""")
    def displayblock(self):
        self.text.insert(INSERT,""" display: block;""")        
    def displayinlineblock(self):
        self.text.insert(INSERT,""" display: inline-block;""")     
         
         
    def color(self):
        self.text.insert(INSERT,"""color: ;""")
    def display(self):
        self.text.insert(INSERT,"""display: ;""")
    def transition(self):
        self.text.insert(INSERT,"""transition: ;""")    
    def background(self):
        self.text.insert(INSERT,"""background: ;""")      
    def backgroundimg(self):
        self.text.insert(INSERT,"""backgroundimg:url("") ;""")
    def font(self):
        self.text.insert(INSERT,"""font: ;""") 
    def fontsize(self):
        self.text.insert(INSERT,"""font-size: ;""")      
    def whitespace(self):
        self.text.insert(INSERT,"""white-space: ;""")
    def justify(self):
        self.text.insert(INSERT,"""justify-content: center;""")
         
    def border(self):
        self.text.insert(INSERT,"""border: ;""")
    def bordercolor(self):
        self.text.insert(INSERT,"""border-color: ;""") 
    def borderstyle(self):
        self.text.insert(INSERT,"""border-style: ;""")         
    def borderwidth(self):
        self.text.insert(INSERT,"""border-width: ;""")      
          
    def grid(self):
        self.text.insert(INSERT,""" grid: 150px / auto auto auto;""")      
    def gap(self):
        self.text.insert(INSERT,"""gap: 00px;""") 
    def gridarea(self):
        self.text.insert(INSERT,"""grid-area: auto;""") 
    def gridrow(self):
        self.text.insert(INSERT,"""grid-row: auto;""")
    def gridcolumn(self):
        self.text.insert(INSERT,"""grid-column: auto;""")  
        
    def flex(self):
        self.text.insert(INSERT,"""flex: 50%;""") 
    def flexwrap(self):
        self.text.insert(INSERT,"""flex-wrap: wrap;""")    
    def flexbasis(self):
        self.text.insert(INSERT,"""flex-basis: 100px;""")  
    def flexflow(self):
        self.text.insert(INSERT,"""flex-flow: row-reverse wrap;""")    
          
    def shortcutmargin(self,e):
        self.text.insert(INSERT,"""margin : """)
    
    def padding(self):
        self.text.insert(INSERT,"""padding: 00px;""")
    def shortcutpadding(self,e):
        self.text.insert(INSERT,"""padding : """)
        
        

# obj = generateCSS()