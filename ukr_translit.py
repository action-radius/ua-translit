# Imports
from latin.ukr.customukr import custom_ukr, letters_for_Custom, letters_for_KMU2010, vowels
from latin.ukr.jirečkivka import Jirečkivka, soft_Jirečkivka, psevdo_jirečkivka
from latin.ukr.TKPN_diac import TKPN_diac, TKPN_combo, TKPN_intl
from latin.ukr.abecadło import abecadło, soft_Abecadło
from latin.ukr.official_KMU_2010 import official_kmu
from latin.ukr.NovaLatynka import NovaLatynka
from latin.ukr.latin_only import latin_only
from latin.ukr.iso9 import iso9

availableChoices = {
    "Custom": custom_ukr,
    "ISO9": iso9,
    "Nova Latynka": NovaLatynka,
    "ТКПН diac": TKPN_diac,
    "ТКПН combo": TKPN_combo,
    "ТКПН intl": TKPN_intl,
    "Abecadło": abecadło,
    "Official КМУ 2010": official_kmu,
    "Їречківка": Jirečkivka,
    "Псевдо-Їречківка": psevdo_jirečkivka,
    "Latin only": latin_only
}

soft_dictionary_hold = {
    "Custom": True,
    "ISO9": True,
    "Nova Latynka": True,
    "ТКПН diac": True,
    "ТКПН combo": True,
    "ТКПН intl": True,
    "Official КМУ 2010": True,
    "Abecadło": soft_Abecadło, 
    "Їречківка": soft_Jirečkivka, 
    "Псевдо-Їречківка": soft_Jirečkivka,
    "Latin only": True
}

soft_dictionary_hold["Custom"]
availableChoices["Custom"]

def ukr_transliteration(choice, message):
    output = ""
    isPreviousLetterConsonant = False
    lower_dictionary = availableChoices[choice]
    soft_dictionary = soft_dictionary_hold[choice]

    for index, i in enumerate(message):
        if index + 1 != len(message):
            index += 1
        lowered = i.lower()
        l = i

        if lowered in lower_dictionary:
            prevLetter = message[index - 2]
            nextLetter = message[index]
            l = lower_dictionary[lowered]
            nextLowered = nextLetter.lower()
            if prevLetter == "'":
                isPreviousLetterConsonant = False

            match choice:
                # sja -> sia (с'я[sja], ся[sia])
                case "Custom" | "Abecadło" | "Псевдо-Їречківка" | "Latin only":
                    if len(l) == 2 and l[0].lower() == 'j' and isPreviousLetterConsonant:
                        if prevLetter.lower() != "ь" and lowered != "ї":
                            l = 'i' + l[1]

                    # ia -> i'a (ся = sia / сіа = si'a) --easyer to read a text
                    if choice == "Custom" or choice == "Latin only":
                        if lowered in letters_for_Custom and prevLetter.lower() == 'і':
                            pl_symbols = {"а": "'a", "е": "'e", "у": "'u"}
                            l = pl_symbols[lowered]

                case "ТКПН diac" | "ТКПН combo" | "ТКПН intl":
                    # v'jo, s'jo, b'jo (вйо, сйо, бйо)
                    if lowered == "й" and i != message[0]:
                        tkpn_letters = ["с", "р", "п", "м", "з", "д", "в", "б"]
                        if prevLetter.lower() in tkpn_letters and nextLowered == "о":
                            l = "'j"

                case "Official КМУ 2010":
                    if len(l) > 1 and lowered in letters_for_KMU2010:
                        if i == message[0] or prevLetter == " " or prevLetter == "":
                            l = "y" + l[1]

                    yi_and_i = {"ї": "yi", "й": "y"}
                    if lowered in yi_and_i:
                        if i == message[0] or prevLetter == " ":
                            l = yi_and_i[lowered]
                    
                    if lowered == "г" and prevLetter.lower() == "з":
                        l = "gh"
            
            # [lia] łia -> la
            if choice == "Abecadło":
                if nextLowered in letters_for_KMU2010 or nextLowered == "л" and message[index + 1] in letters_for_KMU2010: 
                    if lowered == "л": l = "l"

                if prevLetter.lower() == "л" and lowered in letters_for_KMU2010:
                    jeToE = {"я": "a", "є": "e", "ю": "u"}
                    l = jeToE[lowered]
            
            # s -> ś [soft "s"]
            choices_for_soft = ["Abecadło", "Їречківка", "Псевдо-Їречківка"]
            if choice in choices_for_soft:
                if nextLowered == "ь" and lowered in soft_dictionary:
                    l = soft_dictionary[lowered]

                if choice == "Їречківка":
                    # śa (ся) --first letter [ś]
                    if nextLowered in letters_for_KMU2010 and lowered in soft_dictionary:
                        l = soft_dictionary[lowered]

                    # śa (ся) --second letter [a]
                    if prevLetter.lower() in soft_dictionary and lowered in letters_for_KMU2010:
                        l = jeToE[lowered]

            if choice == "Псевдо-Їречківка":
                if nextLowered == "ь" and message[index + 1].lower() == "о":
                    # sio (сьо) | message[index + 1] --after next letter
                    l = psevdo_jirečkivka[lowered] + "i"

            isPreviousLetterConsonant = lowered not in vowels

            match message.isupper() and len(message) > 1:
                case 1:
                    l = l.upper()
                case _:
                    if i.isupper():
                        if len(message) != 1:
                            if nextLetter.isupper() or nextLetter == "'":
                                l = l.upper()
                            if nextLetter.islower() or nextLowered not in lower_dictionary:
                                l = l.title()
                            if i != message[0]:
                                if prevLetter.isupper() and i.isupper():
                                    l = l.upper()
                                if prevLetter.isupper() and nextLetter.islower():
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