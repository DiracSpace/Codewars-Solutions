# [Persistent Bugger](https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec)

# Explanation
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# Explicación
Escribe una función, persistencia, que tome un parámetro positivo num y devuelva su persistencia multiplicativa, que es la cantidad de veces que debes multiplicar los dígitos en num hasta llegar a un solo dígito.

# Examples - Ejemplos
`persistence(39) === 3 // 3 * 9 = 27, 2 * 7 = 14, 1 * 4 = 4, 4 = 1`
`persistence(999) === 4 // 9 * 9 * 9 = 729, 7 * 2 * 9 = 126, 1 * 2 * 6 = 12, 1*2 = 2, 2 = 1`
`persistence(4) === 0 // 4 = 1`