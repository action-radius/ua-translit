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

# Not done!
def translate():
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
                text="Транслітерація з кирилиці на латиницю", 
                font=('Cantarell', 14, 'normal'), 
                fg='black', 
                bg='white')
label.place(x=5, y=5)

text = Text(window, 
                font=('Cantarell', 14, 'normal'),
                fg="black",
                bg="white")
text.place(x=15, y=45, width=700, height=120)

text2 = Text(window, 
                font=('Cantarell', 14, 'normal'),
                fg="black",
                bg="white",
                state="disabled")
text2.place(x=15, y=175, width=700, height=120)

translate_button = Button(window, 
                text="convert",
                command=translate,
                font=('Cantarell', 14, 'italic'),
                fg="black",
                bg="#e3e3e3")
translate_button.place(x=85, y=305, width=80, height=38)
translate_button["border"] = "0"

copying_button = Button(window, 
                text="copy",
                command=copy_button,
                font=('Cantarell', 14, 'italic'),
                fg="black",
                bg="#e3e3e3")
copying_button.place(x=15, y=305, width=60, height=38)
copying_button["border"] = "0"

window.mainloop()