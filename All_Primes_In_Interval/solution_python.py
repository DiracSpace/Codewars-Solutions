#!/usr/bin/python3

def is_prime(n: int):
    isPrime = False

    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                isPrime = True
                break
    return isPrime

def find_primes(n: int):
    total_primes = 0
    for i in range(0, n):
        if is_prime(i):
            total_primes += 1
    return total_primes

n = int(input("Input a number: "))
print (find_primes(n))