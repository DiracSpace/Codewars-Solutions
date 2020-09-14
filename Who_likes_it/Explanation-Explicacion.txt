URL - https://www.codewars.com/kata/5266876b8f4bf2da9b000362

Explanation:
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

Example Input/Output:
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in and 2 others simply increases.

Explicacion:
Probablemente conozca el sistema "Me gusta" de Facebook y otras páginas. Las personas pueden "dar me gusta" a publicaciones de blogs,imágenes u otros elementos.
Queremos crear el texto que debería mostrarse junto a dicho elemento. Implemente una función como :: [String] -> String, que debe incluir una matriz de entrada,
que contiene los nombres de las personas a las que les gusta un elemento. Debe devolver el texto de la pantalla como se muestra en los ejemplos:

Ejemplo Entrada/Salida:
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

Para 4 o más nombres, el número en y otros 2 simplemente aumenta.
