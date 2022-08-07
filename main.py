# Imports: 
from latin.dict_of_latins import x_dict
from translit import transliteration
from threading import Timer
from tkinter import *
from tkinter import ttk
import pyperclip
import os

os.system('clear')

# Functions: 
def convert_func():
    # combo-box value getting: 
    c_box = combo_box.get()

    textarea1 = text.get(1.0, 'end')
    # Choose latin using combo-box's value
    if c_box in x_dict:
        choosing = x_dict[c_box]
        out = transliteration(choosing, textarea1)
    text2.configure(state='normal')
    text2.delete(1.0, 'end')
    text2.insert(1.0, out)
    text2.configure(state='disabled')
    Timer(0.01, convert_func).start()

def copy_button():
    text = text2.get(1.0, 'end')
    pyperclip.copy(text)


# Window config.: 
window = Tk()
window.geometry("800x360")
window.resizable(0, 0)
window.title("Translit")

# icon = PhotoImage(file='dir_to_icon.png')
# window.iconphoto(True, icon) # window icon

window.config(background="white")


# Labels: 
label = Label(window, 
                text="Транслітерація з кирилиці на латиницю.", 
                font=('Cantarell', 14, 'normal'), 
                fg='black', 
                bg='white')
label.place(x=8, y=5)

label2 = Label(window, 
                text="Обери латинику тут: ", 
                font=('Cantarell', 14, 'normal'), 
                fg='black', 
                bg='white')
label2.place(x=424, y=308)


# Text-area's: 
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


# Icon of copy button: 
photo = PhotoImage(file = r"/home/artemiy/git_workspace/ua-translit/copy_btn_icon.png")
photoimage = photo.subsample(5, 4)


# Buttons: 
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


# Combo-Box: 
combo_box = ttk.Combobox(window,
                values=["Custom",
                "ISO9",
                "Nova Latynka",
                "TKPN combo",
                "TKPN diac",
                "TKPN intl",
                "Abecadło",
                "Official KMU 2010"],
                width=16,
                state="readonly")
combo_box.place(x=626, y=310)
combo_box.current(0)
convert_func()
window.mainloop()