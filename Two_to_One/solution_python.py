#!/usr/bin/python3

def longest(a1: str, a2: str) -> str:
    return "".join(list(dict.fromkeys(sorted([c for c in (a1 + a2)]))))
