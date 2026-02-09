import tkinter as tk
from PIL import Image,ImageTk
def test():
    root = tk.Tk()
    root.geometry('250x250')
    image = Image.open('C:\\Users\\User\\OneDrive\\Desktop\\python\\project\\proj\\qr.png')
    re_im = image.resize((150,150))
    tkim = ImageTk.PhotoImage(re_im)
    tk.Label(root,image=tkim).pack()

    root.mainloop()

test()