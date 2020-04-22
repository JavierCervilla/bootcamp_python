#!/usr/bin/env python3
import string

def text_analyzer(text = 'What is the text to analyse?\n'):
    text_analyzer.__doc__ = "this function counts the number of characters, \
the uppers one, the lowers, punctuation marks and spaces in a given text"
    def_text = 'What is the text to analyse?\n'
    if text[:1] == def_text[:1]:
        text = input(text)
    char = 0
    low_letter = 0
    upper_letter = 0
    punctuation_marks = 0
    spaces = 0
    for i in text:
        char += 1
        if i.isupper() == True:
            upper_letter+= 1
        if i.islower() == True:
            low_letter += 1
        if i in string.punctuation:
            punctuation_marks += 1
        if i.isspace() == True:
            spaces += 1
    print('The text contains ' + str(char) + ' characters:')
    print('- ' + str(upper_letter) + ' upper letters.')
    print('- ' + str(low_letter) + ' lower letters.')
    print('- ' + str(punctuation_marks) + ' punctuation marks.')
    print('- ' + str(spaces) + ' spaces.')
