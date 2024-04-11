from tkinter import *
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image, ImageDraw
import sys
import AccountSystem
import os

root = Tk()
root.resizable(0, 0)
logoIcon1 = Image.open('images//coffee3.jpeg')
image = ImageTk.PhotoImage(logoIcon1)
height = 590
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.config(background='#ffffff')


logoIcon = Image.open('images//icon3.jpeg')
photo = ImageTk.PhotoImage(logoIcon)
logo = Label(root, image=photo, bg='#ffffff')
logo.image = photo
logo.place(x=140, y=0)

bg_label = Label(root, image=image, bg='#ffffff')
bg_label.place(x=10, y=150)

progress_label = Label(root, text="Please Wait...", font=('yu gothic ui', 13, 'bold'), fg='black', bg='#ffffff')
progress_label.place(x=190, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=390)


def exit_window():
    sys.exit(root.destroy())


def top():
    root.withdraw()
    os.system("python AccountSystem.py")
    root.destroy()

i = 0

def load():
    global i
    if i <= 10:
        txt = 'Please Wait...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()
load()
load()
root.mainloop()
