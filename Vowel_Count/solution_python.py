#!/usr/bin/env python

def get_count(input_str):
    if input_str == '':
        return 0
    else:
        sum = 0
        vowels = ["a", "e", "i", "o", "u"]
        for char in input_str:
            if char in vowels:
                sum += 1
        return sum
