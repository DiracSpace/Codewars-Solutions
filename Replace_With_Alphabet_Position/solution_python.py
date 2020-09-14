#!/usr/bin/env python

def alphabet_position(text):
    string = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for index in range(0, len(text)):
        if text[index].lower() in alphabet:
            string += str(alphabet.index(text[index].lower()) + 1) + " "
    return string.strip()
