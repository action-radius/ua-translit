# Imports
from latin.blr.vowels import vowels, spec_vowels, blr_soft
from latin.blr.official import blr_official
from latin.blr.customblr import custom_blr

def blr_transliteration(choice, message):
    output = ""
    lower_dictionary = blr_official
    isPreviousLetterConsonant = False

    if choice == "Official": #1
        lower_dictionary = blr_official
    if choice == "Станкевіч": #2
        lower_dictionary = blr_official
    if choice == "Тарашкевіч": #3
        lower_dictionary = blr_official
    if choice == "Custom": #4
        lower_dictionary = custom_blr

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
            # sja -> sia
            if len(l) == 2 and l[0].lower() == 'j':
                if isPreviousLetterConsonant:
                    l = 'i' + l[1]
            ###########################################################
            if choice == "Станкевіч":
                if lowered == "л":
                    l = "ł"
            if choice == "Тарашкевіч":
                if lowered == "л":
                    l = "ł"
                if lowered == "в":
                    l = "w"
            ###########################################################
            # ł(л) -> l(ль)
            if lowered in blr_soft:
                if nextLetter.lower() == "ь":
                    l = blr_soft[lowered]
            
            # śia -> śja
            if lowered in spec_vowels:
                if prevLetter.lower() == "ь":
                    l = blr_official[i]
            
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
# Афіцыйная трансьлітарацыя
# Тарашкевіч
# Станкевіч