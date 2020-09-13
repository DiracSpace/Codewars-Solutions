#!/usr/bin/env python

def sum_array(arr):
    if arr is None or int(len(arr)) < 3 or not arr:
        return 0
    else:
        arr.remove(min(arr))
        arr.remove(max(arr))
        return sum(arr)
