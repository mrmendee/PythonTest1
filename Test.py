from tkinter import *
from tkinter import ttk



win =Tk()

wr1 = LabelFrame(win)
wr2 = LabelFrame(win)

mycanvas = Canvas(wr1)
mycanvas.pack(side=LEFT)

yscrollbar = ttk.Scrollbar(wr1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

myframe = Frame(mycanvas)
myframe.pack()

wr1.pack(fill="both", expand="yes", padx=10,pady=10)

for i in range(50):
    Button(myframe, text="My Button - "+str(i)).pack()

win.geometry("500x500")
win.resizable(False,False)
win.title("Testing")
win.mainloop()