function reverseWords(str) {
    const reversedString = str.split(/(' ')/).map(word => {
        return word.split('').reverse().join('')
    }).join('')
    console.log(reversedString.split(/(' ')/))
    return reversedString;
}

console.log('Expected: ', 'ehT kciuq nworb xof spmuj revo eht yzal .god')
console.log('Got: ', reverseWords('The quick brown fox jumps over the lazy dog.'))