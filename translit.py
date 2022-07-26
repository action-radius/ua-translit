# Imports
from latin.NovaLatynka import NovaLatynka
from latin.TKPN_combo import TKPN_combo
from latin.TKPN_diac import TKPN_diac
from latin.TKPN_intl import TKPN_intl
from latin.custom import custom
from latin.iso9 import iso9

vowels = {
    "а": True,
    "е": True,
    "є": True,
    "и": True,
    "і": True,
    "ї": True,
    "о": True,
    "у": True,
    "ю": True,
    "я": True
}

forCustom = ["а", "е", "у"]
# for1994diac = ["с", "р", "п", "м", "з", "д", "в", "б"]
# for1994diac_upper = ["С", "Р", "П", "З", "Д", "В", "Б"]
# for1994diac_choice = [4, 5, 6]

def transliteration(message):
    choice = 1
    output = ""
    lower_dictionary = custom
    isPreviousLetterConsonant = False

    # if choice == "1":
    #     lower_dictionary = custom
    # if choice == "2":
    #     lower_dictionary = iso9
    # if choice == "3":
    #     lower_dictionary = NovaLatynka
    # if choice == "4":
    #     lower_dictionary = TKPN_diac
    # if choice == "5":
    #     lower_dictionary = TKPN_combo
    # if choice == "6":
    #     lower_dictionary = TKPN_intl

    for index, i in enumerate(message):
        if index + 1 != len(message):
            index += 1
        lowered = i.lower()
        l = i
 
        if lowered in lower_dictionary:
            nextLetter = message[index]
            l = lower_dictionary[lowered]
 
            ###########################################################
            if choice == "1":
                if len(l) == 2 and l[0] == 'j':
                    if isPreviousLetterConsonant:
                        l = 'i' + l[1]
            ###########################################################
            if choice == "1":
                if i == "і" and nextLetter in forCustom:
                    l = "í"
            ###########################################################
            # if choice in for1994diac_choice:
            #     if lowered == "й" and i != message[0]:
            #         if message[index - 2] in for1994diac and nextLetter == "о":
            #             l = "'j"

            #     if lowered == "й" and i != message[0]:
            #         if message[index - 2] in for1994diac_upper and nextLetter == "О":
            #             l = "'j"
            ###########################################################
 
            isPreviousLetterConsonant = lowered not in vowels
 
            if message.isupper() and len(message) > 1:
                 l = l.upper()
            else:
                if i.isupper():
                    if len(message) != 1:
                        if nextLetter.isupper():
                            l = l.upper()
                        if nextLetter.islower() or nextLetter.lower() not in lower_dictionary:
                            l = l.title()
                    else: 
                        l = l.title()
            if l == "'j" and i.isupper():
                l = l.upper()
        else:
            isPreviousLetterConsonant = False
        output += l
    return output

# Моя латинка
# ISO9 ГОСТ 7.79 А
# Nova Latynka
# ТКПН Вакуленко 1994 diac
# ТКПН Вакуленко 1994 combo
# ТКПН Вакуленко 1994 intl

#############################
# Official КМУ 2010         #
# Avtorśka                  #
#############################