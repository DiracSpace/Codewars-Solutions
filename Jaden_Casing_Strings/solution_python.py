#!/usr/bin/env python

def to_jaden_case(string):
    quote = ''
    for word in string.split():
        quote += word[:1].upper() + word[1:] + " "
    return quote.strip()
