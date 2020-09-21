#!/usr/bin/env python

def count_bits(n):
    result = 0
    while n > 0:
        result += n & 1
        n >>= 1
    return result
