# Imports
from latin.TKPN_diac import TKPN_diac, for1994diac
from latin.abecadło import abecadło, for_abecadło
from latin.custom import custom, forCustom
from latin.NovaLatynka import NovaLatynka
from latin.TKPN_combo import TKPN_combo
from latin.TKPN_intl import TKPN_intl
from latin.custom_pl import custom_pl
from latin.vowels import vowels
from latin.iso9 import iso9

def transliteration(message):
    output = ""
    lower_dictionary = custom
    isPreviousLetterConsonant = False
    choice = "8"

    if choice == "1":
        lower_dictionary = custom
    if choice == "2":
        lower_dictionary = iso9
    if choice == "3":
        lower_dictionary = NovaLatynka
    if choice == "4":
        lower_dictionary = TKPN_diac
    if choice == "5":
        lower_dictionary = TKPN_combo
    if choice == "6":
        lower_dictionary = TKPN_intl
    if choice == "7":
        lower_dictionary = custom_pl
    if choice == "8":
        lower_dictionary = abecadło

    for index, i in enumerate(message):
        if index + 1 != len(message):
            index += 1
        lowered = i.lower()
        l = i
 
        if lowered in lower_dictionary:
            nextLetter = message[index]
            l = lower_dictionary[lowered]
 
            ###########################################################
            if choice == "1" or choice == "8" or choice == "7":
                if len(l) == 2 and l[0] == 'j':
                    if isPreviousLetterConsonant:
                        l = 'i' + l[1]
            ###########################################################
            if choice == "1":
                if i.lower() == "і" and nextLetter.lower() in forCustom:
                    if i.islower(): 
                        l = "í"
                    else:
                        l = "í"
                        l.upper()
            ###########################################################
            if choice == "4" or choice == "5" or choice == "6":
                if lowered == "й" and i != message[0]:
                    msg_m2 = message[index - 2]
                    if msg_m2.lower() in for1994diac and nextLetter.lower() == "о":
                        if i.islower():
                            l = "'j"
                        else:
                            l = "'J"
            ###########################################################
            if choice == "7" and lowered == "і":
                if nextLetter.lower() in forCustom:
                    if i.islower():
                        l = "i'"
                    else:
                        l = "I'"
            ###########################################################
            if choice == "8" and lowered in for_abecadło:
                if nextLetter.lower() == "ь":
                    if i.isupper():
                        l = for_abecadło[lowered]
                        l.upper()
                    else:
                        l = for_abecadło[lowered]
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