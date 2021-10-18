# [Tribonacci Sequence](https://www.codewars.com/kata/556deca17c58da83c00002db)

# Explanation

Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

```
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
```

But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

```
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
```

Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]

# Explicación

Bien conocido con el hermano mayor de Fibonacci, también conocido como Tribonacci.

Como el nombre ya puede revelar, funciona básicamente como un Fibonacci, pero sumando los últimos 3 (en lugar de 2) números de la secuencia para generar el siguiente. Y, lo que es peor, lamentablemente no podré escuchar a hablantes de italiano no nativos tratando de pronunciarlo :(

Entonces, si vamos a comenzar nuestra secuencia de Tribonacci con [1, 1, 1] como entrada inicial (también conocida como firma), tenemos esta secuencia:

```
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
```

Pero, ¿y si comenzamos con [0, 0, 1] como firma? Como comenzar con [0, 1] en lugar de [1, 1] básicamente desplaza la secuencia de Fibonacci común en un lugar, es posible que tenga la tentación de pensar que obtendríamos la misma secuencia desplazada en 2 lugares, pero ese no es el caso y obtendríamos:

```
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
```

Bueno, puede que ya lo hayas adivinado, pero para que quede claro: necesitas crear una función de fibonacci que, dada una matriz / lista de firmas, devuelva los primeros n elementos, firma incluida de la secuencia inicial.

La firma siempre contendrá 3 números; n siempre será un número no negativo; si n == 0, devuelve una matriz vacía (excepto en C, devuelve NULL) y prepárate para cualquier otra cosa que no esté claramente especificada;)

Si disfrutaste de este kata, puedes encontrar una versión más avanzada y generalizada en el kata de Xbonacci

[Agradecimiento personal al profesor Jim Fowler en Coursera por sus increíbles clases que realmente recomiendo a cualquier entusiasta de las matemáticas y por mostrarme esta curiosidad matemática también con su habitual pasión contagiosa :)]