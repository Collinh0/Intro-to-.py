//Q1. camelCase
function camelCase(str) {
    return str
        .toLowerCase()
        .split(' ')
        .map((word, index) => {
            if (index === 0) {
                return word;
            }
            return word.charAt(0).toUpperCase() + word.slice(1);
        })
        .join('');
}

console.log(camelCase("we are group one"));
console.log(camelCase("FOOTBALL KENYA FEDERATION"));

