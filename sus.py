from tkinter import *
# import pyperclip
from subprocess import Popen, PIPE
import os

os.system('clear')
print("UA - Translit V1.0")

def copy_button():
    text = entry2.get()
    # pyperclip.copy(text)
    print(f'Copied: {text}')

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()
window.geometry("800x500")
window.resizable(0, 0)
window.title("Translit V1.0")

# icon = PhotoImage(file='dir_to_icon.png')
# window.iconphoto(True, icon) # window icon

window.config(background="white")

label = Label(window, 
                text="Транслітерація з кирилиці на латиницю", 
                font=('SF Pro', 20, 'normal'), 
                fg='black', 
                bg='white')
label.place(x=5, y=0)

entry = Entry(window, 
                font=('SF Pro', 25, 'normal'),
                fg="black",
                bg="white")
entry.place(x=15, y=40, width=700, height=120)

entry2 = Entry(window, 
                font=('SF Pro', 25, 'normal'),
                fg="black",
                bg="white")
entry2.place(x=15, y=170, width=700, height=120)

submit_button = Button(window, 
                text="copy",
                command=copy_button,
                font=('SF Pro', 24, 'normal'),
                fg="black",
                bg="#e3e3e3")
submit_button.place(x=15, y=440, width=80, height=38)
submit_button["border"] = "0"

window.mainloop()