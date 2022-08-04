# Imports: 
from translit import transliteration
from tkinter import *
from tkinter import ttk
import pyperclip
import os

os.system('clear')
print("UA - Translit V1.0")

# Functions: 
def convert_func():
    # combo-box value getting:
    global x_choice
    x_choice = "1"
    c_box = combo_box.get()
    label4.configure(text=c_box)
    # if c_box == "Custom":
    #     choice = "1"
    # else:
    #     choice = "2"

    textarea1 = text.get(1.0, 'end')
    out = transliteration(textarea1)
    text2.configure(state='normal')
    text2.delete(1.0, 'end')
    text2.insert(1.0, out)
    text2.configure(state='disabled')
    result = text2.get(1.0, 'end')
    os.system('clear')
    # Console printing
    print("UA - Translit V1.0")
    print(f"Source: \n{textarea1}--------------\nTranslit: \n{result}")

def copy_button():
    text = text2.get(1.0, 'end')
    pyperclip.copy(text)
    print(f'Copied: {text}')


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
label2.place(x=215, y=308)

label3 = Label(window, 
                text="Обрана латинка: ", 
                font=('Cantarell', 14, 'normal'), 
                fg='black', 
                bg='white')
label3.place(x=500, y=5)

label4 = Label(window, 
                font=('Cantarell', 14, 'normal'), 
                fg='black', 
                bg='white')
label4.place(x=660, y=5)



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


# Icon: 
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

translate_button = Button(window, 
                font=('Cantarell', 14, 'normal'),
                command=convert_func,
                bg="#e3e3e3",
                text="Convert",
                fg="black")
translate_button.place(x=122, y=308, width=80, height=38)
translate_button["border"] = "1"


# Combo-Box: 
combo_box = ttk.Combobox(window,
                values=["Custom",
                "ISO9",
                "Nova Latynka",
                "Avtorska",
                "TKPN combo",
                "TKPN diac",
                "TKPN intl"],
                width=12)

combo_box.place(x=415, y=310)
window.mainloop()