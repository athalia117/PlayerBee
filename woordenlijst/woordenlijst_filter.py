#!/usr/bin/python3
"""
                Dit programma filtert alle woorden op volgende de specificaties:

                De volgende woorden gaan we verwijderen:
                - woorden met meer dan 7 verschillende letters
                - Woorden met minder dan 4 letters
                - Woorden met getallen
                - Woorden met punctuatie
                - Woorden met als eerste letter een hoofdletter
                - Woorden met een laag of hoog getal zoals CO₂-heffing (superscript, subscript)
                - Scheldwoorden (met behulp van een andere set van woorden)

                De volgende woorden gaan we aanpassen:
                - Woorden met 1 of meerdere accenten zoals ë é (hiervan wordt de letter(s) aangepast naar dezelfde letter(s) maar dan zonder het accent(en)),
                  hierbij wordt overigens in de regels gezet hoe je hier gebruik van kunt maken
                - Woorden met een hoofdletter die niet op de eerste plek staan (worden aangepast naar hetzelfde woord lowercase,
                  dit zodat we bij het maken van het programma geen uitzondering hoeven te maken
"""

import string
import unidecode

def pangrams_only(words_possible, letters_used):
    letters_used = list(letters_used)
    almost_pangrams = []
    for word in words_possible:
        counter = 0
        for letter in letters_used:
            if letter not in word:
                break
            else:
                counter = counter + 1
                if counter == len(letters_used):
                    if len(word) == 7:                       # deze regel is alleen nodig als je perfecte super pangrams wil
                        almost_pangrams.append(word)
    return set(almost_pangrams)


def possible_words(words_set, letters_on_display):
    good_words = []
    for word in words_set:
        counter = 0
        for car in word:
            if car not in letters_on_display:
                break
            counter += 1
        # gaat net zo lang door totdat er break is voor het woord en anders net zo lang totdat alle chars zijn geweest

            if len(word) == counter:
                good_words.append(word)
        # zijn alle chars geweest, dus heeft het algo bevestigd dat alle chars in de letters_on_display zaten dan voegt hij hem hier toe

    return (good_words, letters_on_display)

def filter(words, curse_words):

    exceptions = string.punctuation + string.digits + " \t\xb2\xb3\u2082\xb4"
    # punctuation, superscript, subscript, digits

    clean_list = [word.replace('\n', "") for word in words if not any(p in word for p in exceptions)]
    # haalt hier de enters uit elk element en checkt op de exceptions

    clean_list = {unidecode.unidecode(word) for word in clean_list if len(word) >= 4 and not word[0] == word[0].upper()}
    # Eerste letter een hoofdletter, lengte van woord, accenten

    better_words = set()
    for word in clean_list:
        letters_in_word = {char for char in word}
        if len(letters_in_word) < 8:
            better_words.add(word)
    letters_in_word = {}
    # woorden met meer dan 7 verschillende letters

    return (better_words - curse_words)


def main():
    with open('woorden.txt', 'r') as w:
        data = w.readlines()
    with open ('scheldwoorden.txt', 'r') as s:
        scheldwoorden = set(s.readlines())
    good_words_set = filter(data, scheldwoorden)
    possible_words_set, letters_on_display = possible_words(good_words_set, {'s', 'h', 'c', 'i', 'r', 'f', 't'})
    pangrams_sorted = pangrams_only(possible_words_set, letters_on_display)
    print (pangrams_sorted)

if __name__ == "__main__":
    main()
