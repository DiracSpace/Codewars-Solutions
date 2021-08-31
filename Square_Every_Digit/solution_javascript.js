function squareDigits(num) {
    let characters = Array.from(String(num), Number);
    let result = "";

    characters.forEach(character => {
        result += Math.pow(character, 2);
    });

    return Number(result);
}