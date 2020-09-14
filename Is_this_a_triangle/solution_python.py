#!/usr/bin/env python

def is_triangle(a, b, c):
    # Triangle inequality theorem
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        return False
