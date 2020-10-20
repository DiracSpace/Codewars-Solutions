#!/usr/bin/env python

def find_short(s):
    list = []
    for index, word in enumerate(s.split()):
        list.append(len(word))
    return min(list)
