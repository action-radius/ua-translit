# Imports
from latin.ukr.jirečkivka import Jirečkivka, soft_Jirečkivka, psevdo_jirečkivka
from latin.ukr.customukr import custom_ukr, forCustom, forKMU2010, vowels
from latin.ukr.TKPN_diac import TKPN_diac, TKPN_combo, TKPN_intl
from latin.ukr.abecadło import abecadło, soft_Abecadło
from latin.ukr.official_KMU_2010 import official_kmu
from latin.ukr.NovaLatynka import NovaLatynka
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
    "Псевдо-Їречківка": psevdo_jirečkivka
}

soft_dict_list = {
    "Abecadło": soft_Abecadło,
    "Їречківка": soft_Jirečkivka,
    "Псевдо-Їречківка": soft_Jirečkivka
}

availableChoices["Custom"]

def transliteration(choice, message):
    output = ""
    soft_dictionary = soft_dict_list
    isPreviousLetterConsonant = False
    lower_dictionary = availableChoices[choice]

    for index, i in enumerate(message):
        if index + 1 != len(message):
            index += 1
        lowered = i.lower()
        l = i

        if lowered in lower_dictionary:
            prevLetter = message[index - 2]
            nextLetter = message[index]
            l = lower_dictionary[lowered]
            if prevLetter == "'":
                isPreviousLetterConsonant = False

            match choice:
                # sja -> sia (с'я[sja], ся[sia])
                case "Custom" | "Abecadło" | "Псевдо-Їречківка":
                    if len(l) == 2 and l[0].lower() == 'j' and isPreviousLetterConsonant:
                        if prevLetter.lower() != "ь":
                            l = 'i' + l[1]

                    # ia -> ią (ся = sia / сіа = sią) --easyer to read a text
                    if choice == "Custom" and lowered in forCustom and prevLetter.lower() == 'і':
                        plsymbols = {"а": "ą", "е": "ę", "у": "ų"}
                        l = plsymbols[lowered]

                case "ТКПН diac" | "ТКПН combo" | "ТКПН intl":
                    # v'jo, s'jo, b'jo (вйо, сйо, бйо)
                    if lowered == "й" and i != message[0]:
                        tkpn_letters = ["с", "р", "п", "м", "з", "д", "в", "б"]
                        if prevLetter.lower() in tkpn_letters and nextLetter.lower() == "о":
                            l = "'j"
            ###########################################################
            # s[сь] -> ś (soft "s")
            if choice == "Abecadło" and lowered in soft_Abecadło:
                if nextLetter.lower() == "ь":
                    l = soft_dictionary[lowered]
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
            if choice == "Їречківка":
                # s[сь] -> ś (soft "s")
                if nextLetter.lower() == "ь":
                    if lowered in soft_Jirečkivka:
                        l = soft_Jirečkivka[lowered]

                # śa (ся) --first letter [ś]
                if nextLetter.lower() in forKMU2010:
                    if lowered in soft_Jirečkivka:
                        l = soft_Jirečkivka[lowered]

                # śa (ся) --second letter [a]
                if prevLetter.lower() in soft_Jirečkivka:
                    if lowered in forKMU2010:
                        jeToE = {"я": "а", "є": "е", "ю": "у"}
                        l = jeToE[lowered]
            ###########################################################
            # ся -> sia (сьо -> sio)
            if choice == "Псевдо-Їречківка":
                if nextLetter.lower() == "ь" and lowered in soft_Jirečkivka:
                    # s[сь] -> ś (soft "s") | message[index + 1] --after next letter
                    if message[index + 1].lower() != "о":
                        l = soft_Jirečkivka[lowered]
                    # sio (сьо)
                    else:
                        l = psevdo_jirečkivka[lowered] + "i"
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