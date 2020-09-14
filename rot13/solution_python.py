#!/usr/bin/env python

# this code works but doesnt detect characters that arent in the list
def rot13(message):
    string = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    translation = {
        'a':'n',    'd':'q',    'g':'t',    'j':'w',
        'b':'o',    'e':'r',    'h':'u',    'k':'x',
        'c':'p',    'f':'s',    'i':'v',    'l':'y',    'm':'z'
    }

    if message is None:
        return ''
    else:
        # we iterate the string without spaces
        for index, letter in enumerate(message.replace(" ", "")):
            # determine which numbers are keys
            if alphabet.index(letter.lower()) >= 13 and letter.casefold() in alphabet:
                # backwards search for keys in dictionary
                for key, value in translation.items():
                    if letter.casefold() == value.casefold():
                        if letter.isupper():
                            # return the uppercase result
                            string += key.upper()
                        else:
                            # return the result
                            string += key
            else:
                # search for values using letter as key
                if letter.isupper():
                    # return the uppercase result of search
                    lowercase_letter = translation.get(letter.lower())
                    string += lowercase_letter.upper()
                else:
                    # return the result
                    string += translation.get(letter)
        return string
