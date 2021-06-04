from tkinter import *
root = Tk()
# Logic
def getValues():
    print(userentry.get())
    print(passentry.get())
root.geometry("444x444")
# root.minsize(300,300)
# root.maxsize(600,600)
root.title("Learning Tkinter")
user = StringVar()
passval = StringVar()
userentry = Entry(root,textvariable=user)
passentry = Entry(root,textvariable=passval)
userentry.grid(row=0,column=0)
passentry.grid(row=0,column=1)
Button(text="Submit",command=getValues).grid()
root.mainloop()

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
#-----------------------------------------------------------
# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)