# Imports
from latin.custom import custom, forCustom, forKMU2010
from latin.TKPN_diac import TKPN_diac, for1994diac
from latin.abecadło import abecadło, for_abecadło
from latin.official_KMU_2010 import of_kmu
from latin.NovaLatynka import NovaLatynka
from latin.TKPN_combo import TKPN_combo
from latin.TKPN_intl import TKPN_intl
from latin.vowels import vowels
from latin.iso9 import iso9

def transliteration(choice, message):
    output = ""
    lower_dictionary = custom
    isPreviousLetterConsonant = False

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
        lower_dictionary = abecadło
    if choice == "8":
        lower_dictionary = of_kmu

    for index, i in enumerate(message):
        if index + 1 != len(message):
            index += 1
        lowered = i.lower()
        l = i
 
        if lowered in lower_dictionary:
            nextLetter = message[index]
            l = lower_dictionary[lowered]
            if message[index - 2] == "'":
                isPreviousLetterConsonant = False
 
            ###########################################################
            if choice == "1" or choice == "7":
                if len(l) == 2 and l[0].lower() == 'j':
                    if isPreviousLetterConsonant:
                        l = 'i' + l[1]
            ###########################################################
            if choice == "1":
                if lowered == "і" and nextLetter.lower() in forCustom:
                    l = "i'"
            ###########################################################
            if choice == "4" or choice == "5" or choice == "6":
                if lowered == "й" and i != message[0]:
                    msg_m2 = message[index - 2]
                    if msg_m2.lower() in for1994diac and nextLetter.lower() == "о":
                        l = "'j"
            ###########################################################
            if choice == "7" and lowered in for_abecadło:
                if nextLetter.lower() == "ь":
                    l = for_abecadło[lowered]
            ###########################################################
            if choice == "8":
                if len(l) > 1 and lowered in forKMU2010:
                    if i == message[0] or message[index - 2] == " ":
                        l = "y" + l[1]

                if lowered == "ї":
                    if i == message[0] or message[index - 2] == " ":
                        l = "yi"
                    
                if lowered == "й":
                    if i == message[0] or message[index - 2] == " ":
                        l = "y"
            ###########################################################
 
            isPreviousLetterConsonant = lowered not in vowels
 
            if message.isupper() and len(message) > 1:
                 l = l.upper()
            else:
                if i.isupper():
                    if len(message) != 1:
                        if nextLetter.isupper() or nextLetter == "'":
                            l = l.upper()
                        if nextLetter.islower() or nextLetter.lower() not in lower_dictionary:
                            l = l.title()
                        if i != message[0]:
                            if message[index - 2].isupper() and i.isupper():
                                l = l.upper()
                            if message[index - 2].isupper() and nextLetter.islower():
                                l = l.title()
                    else: 
                        l = l.title()
        else:
            isPreviousLetterConsonant = False
        output += l
    return output

# Custom
# ISO9 ГОСТ 7.79 А
# Nova Latynka
# ТКПН Вакуленко 1994 diac
# ТКПН Вакуленко 1994 combo
# ТКПН Вакуленко 1994 intl
# Official КМУ 2010

# custom, custom_pl
# iso9
# TKPN_diac
# abecadło
# official_KMU_2010
# NovaLatynka
# TKPN_combo
# TKPN_intl