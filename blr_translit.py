# Imports
from latin.blr.vowels import vowels, spec_vowels, blr_soft
from latin.blr.official import blr_official
from latin.blr.customblr import custom_blr

availableChoices = {
    "Official": blr_official,
    "Станкевіч": blr_official,
    "Тарашкевіч": blr_official,
    "Custom": custom_blr,
}

availableChoices["Official"]

def blr_transliteration(choice, message):
    output = ""
    isPreviousLetterConsonant = False
    lower_dictionary = availableChoices[choice]

    for index, i in enumerate(message):
        if index + 1 != len(message):
            index += 1
        lowered = i.lower()
        isPrevLetterL = False
        l = i
 
        if lowered in lower_dictionary:
            prevLetter = message[index - 2]
            nextLetter = message[index]
            nextLowered = nextLetter.lower()
            l = lower_dictionary[lowered]
            if message[index - 2] == "'":
                isPreviousLetterConsonant = False
 
            ###########################################################
            # sja -> sia
            if len(l) == 2 and l[0].lower() == 'j':
                if isPreviousLetterConsonant: l = 'i' + l[1]

            match choice:
                case "Станкевіч" | "Тарашкевіч":
                    if lowered == "л": l = "ł"
                
                    if choice == "Тарашкевіч":
                        if lowered == "в": l = "w"
            ###########################################################
            # ł(л) -> l(ль)
            if lowered in blr_soft:
                if nextLowered == "ь": 
                    l = blr_soft[lowered]
                    if choice == "Official" and lowered == "л": l = "ĺ"
            
            # śia -> śja
            if lowered in spec_vowels:
                if prevLetter.lower() == "ь": l = blr_official[i]

            # [lia] łia -> la
            if choice != "Official":
                if nextLowered in spec_vowels or nextLowered == "л" and message[index + 1] in spec_vowels: 
                    if lowered == "л": l = "l"

                if prevLetter.lower() == "л" and lowered in spec_vowels:
                    spec_vowels_plus = {"я": "a", "е": "e", "ю": "u", "ё": "o"}
                    l = spec_vowels_plus[lowered]
            
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
# Афіцыйная трансьлітарацыя
# Тарашкевіч
# Станкевіч