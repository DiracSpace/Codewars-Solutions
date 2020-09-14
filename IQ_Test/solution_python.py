#!/usr/bin/env python

def iq_test(numbers):
    odd = []
    even = []
    # find all odd or even numbers
    for index, char in enumerate(numbers.split(), start=1):
        if int(char) % 2 == 0:
            odd.append(index)
        if int(char) % 2 != 0:
            even.append(index)
    if len(odd) > len(even):
        return even[0]
    else:
        return odd[0]
