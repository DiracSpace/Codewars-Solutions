#!/usr/bin/env python

def max_sequence(arr):
    # count positive numbers
    positive = lambda x: [number for number in arr if number > 0]
    negative = lambda x: [number for number in arr if number < 0]
    # taking into account empty arrays
    if len(arr) == 0 or int(len(negative(arr))) == int(len(arr)):
        return 0
    else:
        if int(len(positive(arr))) == len(arr):
            # all positive numbers
            return sum(arr)
        else:
            # kadane algorithm
            max_now = 0
            max_total = 0
            for number in range(0, int(len(arr))):
                max_now = max_now + arr[number]
                if max_now < 0:
                    max_now = 0
                if max_now > max_total:
                    max_total =  max(max_total, max_now)
            return max_total
