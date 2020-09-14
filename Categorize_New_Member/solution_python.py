#!/usr/bin/env python

def open_or_senior(data):
    member_category = []
    for tuple in data:
        member_category.append("Senior" if tuple[0] >= 55 and int(tuple[1] > 7) else "Open")
    return member_category
