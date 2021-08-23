#!/usr/bin/python3

n = int(input("Ingrese un numero: "))

primes = [True for i in range(n + 1)]
total_primes = 0
prime = 2

while (prime * prime <= n):
    if (primes[prime] == True):
        for i in range(prime * prime, n + 1, prime):
            primes[i] = False
    prime += 1

for p in range(2, n + 1):
    if primes[p]:
        total_primes += 1

print (f"0 to {n} is {total_primes}")