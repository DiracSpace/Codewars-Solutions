# [Two to One](https://www.codewars.com/kata/5656b6906de340bd1b0000ac)

# Explanation

Take 2 strings `s1` and `s2` including only letters from `a` to `z`. Return a new sorted string, the longest possible, containing distinct letters 
- each taken only once 
- coming from s1 or s2.

# Explicacion
Tome 2 cadenas `s1` y` s2` que incluyan solo letras de la `a` a la` z`. Devuelve una nueva cadena ordenada, la más larga posible, que contenga letras distintas
- cada uno tomado solo una vez
- procedente de s1 o s2.

# Examples - Ejemplos
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"