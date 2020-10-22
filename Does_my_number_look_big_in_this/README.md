# [Does my number look big in this?](https://www.codewars.com/kata/5287e858c6b5a9678200083c)

# Explanation 
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

The Challenge:
Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

# Explicación
Un número narcisista es un número positivo que es la suma de sus propios dígitos, cada uno elevado a la potencia del número de dígitos en una base determinada. En este Kata, nos restringiremos al decimal (base 10).

El reto:
Su código debe devolver verdadero o falso dependiendo de si el número dado es un número narcisista en base 10.

No se requiere la verificación de errores para cadenas de texto u otras entradas no válidas, solo se pasarán a la función números enteros positivos distintos de cero válidos.

# Examples - Ejemplos
153 (3 digits):
`1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`

1634 (4 digits):
`1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634`