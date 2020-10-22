# [Maximum Subarray Sum](https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c)

# Explanation
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# Explicacion
El problema del subarreglo de suma máxima consiste en encontrar la suma máxima de una subsecuencia contigua en un arreglo o lista de enteros:

El caso fácil es cuando la lista se compone solo de números positivos y la suma máxima es la suma de toda la matriz. Si la lista está formada solo por números negativos, devuelve 0 en su lugar.

Se considera que la lista vacía tiene cero suma máxima. Tenga en cuenta que la lista o matriz vacía también es una sublista / subarreglo válido.

# Examples - Ejemplos

[Kadane's Algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)

`max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6: [4, -1, 2, 1]`