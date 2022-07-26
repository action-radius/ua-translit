# Imports: 
from blr_translit import blr_transliteration
from ukr_translit import ukr_transliteration
from tkinter import *
from tkinter import ttk
import pyperclip


# Functions: 
def convert_func():
    if tabControl.tab(tabControl.select(), "text") == "Ukrainian":
        # combo-box value getting: 
        c_box_ua = combo_boxukr.get()

        textarea1 = text.get(1.0, 'end')
        # Choose latin using combo-box's value
        out = ukr_transliteration(c_box_ua, textarea1)
        text2_ukr.configure(state='normal')
        text2_ukr.delete(1.0, 'end')
        text2_ukr.insert(1.0, out)
        text2_ukr.configure(state='disabled')
    else:
        # combo-box value getting: 
        c_box_bl = combo_boxblr.get()

        textarea1 = text.get(1.0, 'end')
        out = blr_transliteration(c_box_bl, textarea1)
        text2_blr.configure(state='normal')
        text2_blr.delete(1.0, 'end')
        text2_blr.insert(1.0, out)
        text2_blr.configure(state='disabled')
    window.after(10, convert_func)

def copy_button():
    text = text2_ukr.get(1.0, 'end')
    pyperclip.copy(text)


# Window config.:
window = Tk()
window.geometry("800x370")
window.resizable(0, 0)
window.title("Translit")

# icon = PhotoImage(file='dir_to_icon.png')
# window.ico"Їречківка": Jirečkivka,nphoto(True, icon) # window icon
window.config(background="white")


# Tabs: 
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Ukrainian')
tabControl.add(tab2, text ='Belarusian')
tabControl.pack(expand = 1, fill ="both")


# Labels: 
label_ukr = Label(tab1, 
                text="Транслітерація з кирилиці на латиницю.", 
                font=('Cantarell', 14, 'normal'), 
                fg='black')
label_ukr.place(x=8, y=5)

label_blr = Label(tab2, 
                text="Транслітарацыя з кірыліцы на лацінку.", 
                font=('Cantarell', 14, 'normal'), 
                fg='black')
label_blr.place(x=8, y=5)

label2_ukr = Label(tab1, 
                text="Оберіть латинику тут: ", 
                font=('Cantarell', 14, 'normal'), 
                fg='black')
label2_ukr.place(x=424, y=303)

label2_blr = Label(tab2, 
                text="Абярыце лацінку тут: ", 
                font=('Cantarell', 14, 'normal'), 
                fg='black')
label2_blr.place(x=424, y=303)


# Text-area's: 
text = Text(window, 
                font=('Cantarell', 14, 'normal'),
                fg="black",
                bg="white")
text.place(x=25, y=65, width=747, height=120)

text2_ukr = Text(tab1, 
                font=('Cantarell', 14, 'normal'),
                fg="black",
                bg="white",
                state="disabled")
text2_ukr.place(x=25, y=170, width=747, height=120)

text2_blr = Text(tab2, 
                font=('Cantarell', 14, 'normal'),
                fg="black",
                bg="white",
                state="disabled")
text2_blr.place(x=25, y=170, width=747, height=120)


# Icon of copy button: 
photo = PhotoImage(file = r"./copy_btn_icon.png")
photoimage = photo.subsample(5, 4)


# Buttons: 
copying_button = Button(window, 
                font=('Cantarell', 14, 'normal'),
                command=copy_button,
                image=photoimage,
                compound=LEFT,
                bg="#e3e3e3",
                text="Копія",
                fg="black")
copying_button.place(x=25, y=324, width=90, height=38)
copying_button["border"] = "1"


# Combo-Box: 
combo_boxukr = ttk.Combobox(tab1,
                values=["Custom",
                "ISO9",
                "Nova Latynka",
                "ТКПН combo",
                "ТКПН diac",
                "ТКПН intl",
                "Abecadło",
                "Official КМУ 2010",
                "Глаголиця",
                # "Їречківка",
                "Псевдо-Їречківка",
                "Latin only"],
                width=16,
                state="readonly")
combo_boxukr.place(x=626, y=305)
combo_boxukr.current(0)

combo_boxblr = ttk.Combobox(tab2,
                values=["Official",
                "Станкевіч",
                "Тарашкевіч",
                "Custom"],
                width=16,
                state="readonly")
combo_boxblr.place(x=626, y=305)
combo_boxblr.current(0)
window.after(10, convert_func)
window.mainloop()