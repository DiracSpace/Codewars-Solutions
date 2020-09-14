#!/usr/bin/env python

def wave(people):
    mexican_wave = []
    for index, char in enumerate(people):
        if char.isspace() is False:
            mexican_wave.append(people[:index] + char.upper() + people[index + 1:])
    return mexican_wave
