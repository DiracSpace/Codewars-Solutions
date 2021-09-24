// original solution with relative clean code conventions
function toCamelCase(str) {
    if (str.length == 0) return '';

    const splitted = (str.includes("-")) ? str.split("-") : str.split("_");

    const capitalizedLettersArray = splitted.map((s, i) => {
        if (i === 0) {
            return s[0] + s.slice(1);
        } else {
            return s[0].toUpperCase() + s.slice(1);
        }
    });

    return capitalizedLettersArray.join("");
}

// Reduced variables solution
function toCamelCase(str) {
    if (str.length === 0) return '';

    return ((str.includes("-"))
        ? str.split("-")
        : str.split("_")).map((s, i) => {
            if (i === 0) {
                return s[0] + s.slice(1);
            } else {
                return s[0].toUpperCase() + s.slice(1);
            }
        }).join("");
}