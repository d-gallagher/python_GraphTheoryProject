from tkinter import *
from tkinter.ttk import Notebook
from PIL import ImageTk, Image
from thompsonsConst_Submission import match 
import os

picsize = 250,250
# Colour List 585858, e1ce7a, fbffb9, fdd692, ec7357

infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c", "a.b.c+", "a.b.c?"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

def runRegex():
    for i in infixes:
        for s in strings:
            print(match(i, s), i, s)

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.geometry('800x500')
        self.title('Regex Matching with Thompsons Construction')

        self.notebook = Notebook(self)
        

        #init and set up about tab as canvas
        about_tab = Canvas(self, bg = "#fbffb9")
        about_tab.label = Label(about_tab, text="Deterministic Finite Automaton Examples", padx=5, pady=5, anchor = 'nw')
        about_tab.label.pack()
        about_tab.pack(expand = YES, fill = BOTH)
        img = Image.open('NFA_1.png')
        img.thumbnail(picsize, Image.ANTIALIAS)
        about_tab.image = ImageTk.PhotoImage(img)        
        about_tab.create_image(0, 0, image = about_tab.image, anchor = 'nw', )

        #init and set up regex tab for reges operations
        regex_tab = Frame(self.notebook)  

        self.button = Button(regex_tab, text="Run Regex", command=runRegex)
        self.button.pack(side=BOTTOM, fill=X)

        self.infix_label = Label(regex_tab, text=infixes, bg="lightgrey", fg="black")
        self.string_label = Label(regex_tab, text=strings, bg="lightgrey", fg="black")
        self.infix_label.pack(side=TOP, fill=BOTH, expand=1)
        self.string_label.pack(side=TOP, fill=BOTH, expand=1)

        #add tabls to notebook window
        self.notebook.add(about_tab, text="About")
        self.notebook.add(regex_tab, text="Regex")
        self.notebook.pack(fill=BOTH, expand=1)
       
if __name__ == '__main__' :
    root = Root()
    root.mainloop()