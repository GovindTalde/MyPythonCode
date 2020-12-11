from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title("frames")

frame = LabelFrame(root, padx=20, pady=20, bg="blue")
frame.pack(padx=10, pady=10)

b = Button(frame, text="dont click hare")
b.grid(row=0, column=0)
           
b2 = Button(frame, text="dont click hare also")
b2.grid(row=1, column=1)




root.mainloop()
