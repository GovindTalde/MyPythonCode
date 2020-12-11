from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title("creating new window")

def open():
    global my_img
    top = Toplevel()
    top.title("new window")
    my_img = ImageTk.PhotoImage(Image.open("1.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close", command=top.destroy).pack()



btn = Button(root, text = "open window", command=open).pack()

mainloop()
