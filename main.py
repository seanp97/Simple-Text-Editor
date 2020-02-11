import os
import os.path
from tkinter import *
import sys
import tkinter
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import filedialog

newFiles = ""
saveFiles = ""
textCode = ""
folderSelected = ""

def newFile():
    folderSelected = filedialog.askdirectory()
    global newFiles
    newFiles = askstring('New', 'New file')
    fNewFile = open(folderSelected + "/" + newFiles, "x")
    messagebox.showinfo("Created", newFiles + " has been created")

def saveFile():
    global saveFiles
    global newFiles
    if os.path.exists(newFiles):
        textCode = textArea.get("1.0",END)
        fSaveFile = open(newFiles, "w")
        fSaveFile.write(textCode)
        messagebox.showinfo("Saved", newFiles +  " has been saved")
    else:
        newFile()
        textCode = textArea.get("1.0",END)
        fSaveFile = open(newFiles, "w")
        fSaveFile.write(textCode)
        messagebox.showinfo("Saved", newFiles +  " has been saved")

app = Tk()
app.title("Text Editor")
app.geometry("800x400")
appHeight = app.winfo_reqheight()
appWidth = app.winfo_reqwidth()

newBtn = Button(app, text="New", command=newFile)
newBtn.place(x=5, y=5)

saveBtn = Button(app, text="Save", command=saveFile)
saveBtn.place(x=45, y=4)

textArea = Text(app, height=appHeight, width=appWidth)
textArea.place(x=0, y=35)

app.mainloop()
