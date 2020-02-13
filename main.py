import os
import os.path
from tkinter import *
import sys
import tkinter
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import filedialog
import time

newFiles = ""
textCode = ""
folderSelected = ""
existPath = ""
folderFile = ""
fOpenFile = ""
Opened = False
openString = ""

def newFile():
    Opened = False
    global folderSelected
    folderSelected = filedialog.askdirectory()
    global newFiles
    newFiles = askstring('New', 'New file')
    fNewFile = open(folderSelected + "/" + newFiles, "x")
    global existPath
    existPath = folderSelected + "/" + newFiles
    messagebox.showinfo("Created", newFiles + " has been created")

def saveFile():
    global newFiles
    global existPath
    global folderSelected
    global Opened
    global folderFile
    if os.path.exists(existPath):
        textCode = textArea.get("1.0",END)
        fSaveFile = open(folderSelected + "/" + newFiles, "w")
        fSaveFile.write(textCode)
        messagebox.showinfo("Saved", newFiles +  " has been saved")

    if Opened == True:
        getText = textArea.get("1.0",END)
        fOpenSave = open(folderFile, "w")
        fOpenSave.write(getText)
        messagebox.showinfo("Saved", folderFile +  " has been saved")
    else:
        saveFolderSelected = filedialog.askdirectory()
        textCodeSave = textArea.get("1.0",END)
        newSavedFiles = askstring('New', 'New file')
        fNewSaveFile = open(saveFolderSelected + "/" + newSavedFiles, "w")
        fNewSaveFile.write(textCodeSave)
        messagebox.showinfo("Saved", newSavedFiles +  " has been saved")


def openFile():
    global Opened
    Opened = True
    global folderFile
    global fOpenFile
    global openString
    folderFile = filedialog.askopenfilename()
    fOpenFile = open(folderFile, "r")
    openString = fOpenFile.read()
    textArea.delete('1.0', END)
    textArea.insert(END, openString)

app = Tk()
app.title("Text Editor")
app.geometry("800x400")
appHeight = app.winfo_reqheight()
appWidth = app.winfo_reqwidth()

newBtn = Button(app, text="New", command=newFile)
newBtn.place(x=5, y=5)

saveBtn = Button(app, text="Save", command=saveFile)
saveBtn.place(x=45, y=4)

openBtn = Button(app, text="Open", command=openFile)
openBtn.place(x=85, y=4)

textArea = Text(app, height=appHeight, width=appWidth)
textArea.place(x=0, y=35)

app.mainloop()
