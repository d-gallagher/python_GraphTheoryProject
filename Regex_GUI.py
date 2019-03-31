from tkinter import *
from tkinter.ttk import Notebook
from PIL import ImageTk, Image
from thompsonsConst_Submission import match 
import os

picsize = 250,250
# Colour List 585858, e1ce7a, fbffb9, fdd692, ec7357

infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c", "a.b.c+", "a.b.c?"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]
regexOut = []
userInfixes = []
userStrings = []

def runRegex(l1, l2):
    for i in l1:
        for s in l2:
            print(match(i, s), i, s)
            regexOut.append(print(match(i, s), i, s))

# def addUserInfixandString():
#     uInfix = infixEntry.get()
#     uString = stringEntry.get()
#     userInfixes.append(uInfix)
#     userStrings.append(uString)
#     print(uInfix, uString)

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
        about_tab.create_image(0, 0, image = about_tab.image, anchor = 'nw')

        #init and set up regex tab for reges operations
        regex_tab = Frame(self.notebook)  

        self.infix_label = Label(regex_tab, text=infixes, bg="#585858", fg="#ec7357").grid(row=0, column=0)
        self.string_label = Label(regex_tab, text=strings, bg="#585858", fg="#ec7357").grid(row=1, column=0)
        # self.infix_label.pack()
        # self.string_label.pack()

        self.regex_entryLabel = Label(regex_tab, text="infix", bg="#585858", fg="#ec7357").grid(row=2, column=0)
        self.infix_entryBox = Entry(regex_tab, bg="#fdd692", fg="black").grid(row=2)
        self.string_entryBox = Entry(regex_tab, bg="#fdd692", fg="black").grid(row=3)
        infixEntry = StringVar()
        stringEntry = StringVar()

        def addUserInfixandString():
            uInfix = infixEntry.get()
            uString = stringEntry.get()
            userInfixes.append(uInfix)
            userStrings.append(uString)
            print(uInfix, uString)
            #print(match(uInfix, uString), uInfix, uString)

        self.add_regex_and_string = Button(regex_tab, text="Add Regex and String", command=addUserInfixandString).grid(row=4)
        #self.add_regex_and_string.pack(fill=X)

        # self.button = Button(regex_tab, text="Run Regex", command=runRegex).grid(row=5)
        #self.button.pack( fill=X)

        #output regex data
        self.outputtext = Text(regex_tab).grid(column=1, row=5)
        #outputtext.grid(column=1, row=5)
        def check_expression():
            #Your code that checks the expression
            #self.outputtext.delete('0', END) # clear the outputtext text widget           
            for s in regexOut:
                varContent = "" + regexOut.pop() # get what's written in the inputentry entry widget  
                runRegex(infixes, strings)              
                self.outputtext.insert(varContent)

        self.button = Button(regex_tab, text="Run Regex", command=check_expression).grid(row=5)

        #add tabs to notebook window
        self.notebook.add(about_tab, text="About")
        self.notebook.add(regex_tab, text="Regex")
        self.notebook.pack(fill=BOTH, expand=1)
       
if __name__ == '__main__' :
    root = Root()
    root.mainloop()