# Imports
from latin.ukr.customukr import custom_ukr, forCustom, forKMU2010
from latin.ukr.TKPN_diac import TKPN_diac, for1994diac
from latin.ukr.abecadło import abecadło, for_abecadło
from latin.ukr.official_KMU_2010 import of_kmu
from latin.ukr.NovaLatynka import NovaLatynka
from latin.ukr.TKPN_combo import TKPN_combo
from latin.ukr.TKPN_intl import TKPN_intl
from latin.ukr.vowels import vowels
from latin.ukr.iso9 import iso9

def transliteration(choice, message):
    output = ""
    lower_dictionary = custom_ukr
    isPreviousLetterConsonant = False

    if choice == "Custom": #1
        lower_dictionary = custom_ukr
    if choice == "ISO9": #2
        lower_dictionary = iso9
    if choice == "Nova Latynka": #3
        lower_dictionary = NovaLatynka
    if choice == "TKPN diac": #4
        lower_dictionary = TKPN_diac
    if choice == "TKPN combo": #5
        lower_dictionary = TKPN_combo
    if choice == "TKPN intl": #6
        lower_dictionary = TKPN_intl
    if choice == "Abecadło": #7
        lower_dictionary = abecadło
    if choice == "Official KMU 2010": #8
        lower_dictionary = of_kmu

    for index, i in enumerate(message):
        if index + 1 != len(message):
            index += 1
        lowered = i.lower()
        l = i
 
        if lowered in lower_dictionary:
            prevLetter = message[index - 2]
            nextLetter = message[index]
            l = lower_dictionary[lowered]
            if message[index - 2] == "'":
                isPreviousLetterConsonant = False
 
            ###########################################################
            if choice == "Custom" or choice == "Abecadło":
                if len(l) == 2 and l[0].lower() == 'j':
                    if isPreviousLetterConsonant:
                        l = 'i' + l[1]
            ###########################################################
            if choice == "Custom":
                if lowered == "і" and nextLetter.lower() in forCustom:
                    l = "i'"
            ###########################################################
            if choice == "TKPN diac" or choice == "TKPN combo" or choice == "TKPN intl":
                if lowered == "й" and i != message[0]:
                    msg_m2 = message[index - 2]
                    if msg_m2.lower() in for1994diac and nextLetter.lower() == "о":
                        l = "'j"
            ###########################################################
            if choice == "Abecadło" and lowered in for_abecadło:
                if nextLetter.lower() == "ь":
                    l = for_abecadło[lowered]
            
            if choice == "Abecadło" and lowered in forKMU2010:
                if prevLetter.lower() == "ь":
                    l = abecadło[i]
            ###########################################################
            if choice == "Official KMU 2010":
                if len(l) > 1 and lowered in forKMU2010:
                    if i == message[0] or prevLetter == " ":
                        l = "y" + l[1]

                if lowered == "ї":
                    if i == message[0] or prevLetter == " ":
                        l = "yi"
                    
                if lowered == "й":
                    if i == message[0] or prevLetter == " ":
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
# ТКПН Вакуленко 1994 combo
# ТКПН Вакуленко 1994 diac
# ТКПН Вакуленко 1994 intl
# Abecadło
# Official КМУ 2010