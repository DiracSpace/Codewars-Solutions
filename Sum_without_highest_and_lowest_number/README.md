# [Sum without highest and lowest number](https://www.codewars.com/kata/576b93db1129fcf2200001e6)

# Explanation
Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!). (The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

If array is empty, null or None, or if only 1 Element exists, return 0.
Note:In C++ instead null an empty vector is used. In C there is no null. ;-)

-- There's no null in Haskell, therefore Maybe [Int] is used. Nothing represents null.

# Explicacion
Suma todos los números de la matriz (en F # y Haskell obtienes una lista) excepto el elemento más alto y el más bajo (¡el valor, no el índice!). (El elemento más alto / más bajo es, respectivamente, solo un elemento en cada borde, ¡incluso si hay más de uno con el mismo valor!)

Si la matriz está vacía, nula o Ninguno, o si solo existe 1 elemento, devuelve 0.
Nota: En C ++, en su lugar, se utiliza un vector vacío nulo. En C no hay nulo. ;-)

-- No hay nulo en Haskell, por lo tanto, se usa Maybe [Int]. Nada representa nulo.

# Examples - Ejemplos
`{ 6, 2, 1, 8, 10 } => 16`
`{ 1, 1, 11, 2, 3 } => 6`