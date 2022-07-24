import translit
from tkinter import *
import os
# from subprocess import Popen, PIPE
# import pyperclip

os.system('clear')
print("UA - Translit V1.0")
print("Hello, World! Testing GitHub.")


def copy_button():
    text = text2.get()
    # pyperclip.copy(text)
    print(f'Copied: {text}')

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()
window.geometry("800x360")
window.resizable(0, 0)
window.title("Translit")

# icon = PhotoImage(file='dir_to_icon.png')
# window.iconphoto(True, icon) # window icon

window.config(background="white")

label = Label(window, 
                text="Транслітерація з кирилиці на латиницю.", 
                font=('Cantarell', 14, 'normal'), 
                fg='black', 
                bg='white')
label.place(x=8, y=5)

text = Text(window, 
                font=('Cantarell', 14, 'normal'),
                fg="black",
                bg="white")
text.place(x=25, y=45, width=747, height=120)

text2 = Text(window, 
                font=('Cantarell', 14, 'normal'),
                fg="black",
                bg="white",
                state="disabled")
text2.place(x=25, y=175, width=747, height=120)

translate_button = Button(window, 
                font=('Cantarell', 14, 'normal'),
                command=None,
                bg="#e3e3e3",
                text="Convert",
                fg="black")
translate_button.place(x=122, y=308, width=80, height=38)
translate_button["border"] = "1"

# Icon
photo = PhotoImage(file = r"/home/artemiy/git_workspace/ua-translit/copy_btn_icon.png")
photoimage = photo.subsample(5, 4)

copying_button = Button(window, 
                font=('Cantarell', 14, 'normal'),
                command=copy_button,
                image=photoimage,
                compound=LEFT,
                bg="#e3e3e3",
                text="copy",
                fg="black")
copying_button.place(x=25, y=308, width=90, height=38)
copying_button["border"] = "1"

window.mainloop()