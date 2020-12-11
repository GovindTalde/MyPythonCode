from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title("dropdown menu")

def show():
    mylabel = Label(root, text=clicked.get()).pack()

options = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

btn = Button(root, text="show selestion", command=show).pack()




root.mainloop()
