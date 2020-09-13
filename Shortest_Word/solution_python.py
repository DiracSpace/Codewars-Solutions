#!/usr/bin/env python

"""
URL - https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

Simple, dada una cadena de palabras, devuelve la longitud de las palabras más cortas.
La cadena nunca estará vacía y no es necesario tener en cuenta los diferentes tipos de datos.
"""

def find_short(s):
    list = []
    for index, word in enumerate(s.split()):
        list.append(len(word))
    return min(list)
