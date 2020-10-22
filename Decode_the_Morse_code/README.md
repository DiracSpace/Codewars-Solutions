# [Deocde the Morse Code](https://www.codewars.com/kata/54b724efac3d5402db00065e)

# Explanation
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications
around the world. The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−.
The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used
to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic),
that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

# Explicacion
En este kata tienes que escribir un decodificador de código Morse simple. Si bien el código Morse ahora es reemplazado principalmente por canales de comunicación de voz y datos digitales, todavía se
usa en algunas aplicaciones alrededor del mundo. El código Morse codifica cada carácter como una secuencia de "puntos" y "guiones". Por ejemplo, la letra A se codifica como · -, la letra Q se codifica
como −− · - y el dígito 1 se codifica como · −−−−. El código Morse no distingue entre mayúsculas y minúsculas, tradicionalmente se utilizan letras mayúsculas. Cuando el mensaje está escrito en código Morse,
se usa un solo espacio para separar los códigos de caracteres y se usan 3 espacios para separar palabras. Por ejemplo, el mensaje HEY JUDE en código Morse es ···· · - · −− · −−− ·· - - ·· ·.

NOTA: Los espacios adicionales antes o después del código no tienen significado y deben ignorarse.

Además de letras, dígitos y algunos signos de puntuación, existen algunos códigos de servicio especiales, el más notorio de ellos es la señal de socorro internacional SOS
(que fue emitida por primera vez por Titanic), que está codificado como ··· −−− ···. Estos códigos especiales se tratan como caracteres especiales únicos y, por lo general, se transmiten como palabras
independientes.

Su tarea es implementar una función que tome el código morse como entrada y devuelva una cadena decodificada legible por humanos.


# Examples - Ejemplos
`decodeMorse('.... . -.--   .--- ..- -.. .') -> return "HEY JUDE"`