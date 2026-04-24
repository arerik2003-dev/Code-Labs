//AND, OR, NOT 

//AND (&&) - Devuelve true si ambos operandos son verdaderos
console.log(true && true); // true
console.log(true && false); // false
console.log(false && true); // false
console.log(false && false); // false

//OR (||) - Devuelve true si al menos uno de los operandos es verdadero
console.log(true || true); // true
console.log(true || false); // true
console.log(false || true); // true
console.log(false || false); // false

//NOT (!) - Devuelve el valor opuesto del operando
console.log(!true); // false
console.log(!false); // true

let mayor = true;
let suscrito = true;

console.log('operador AND', mayor && suscrito); // true
console.log('operador OR', mayor || suscrito);

//NOT !

console.log('OPerador NOT', !mayor); // false

let catalogoinfantil = !mayor; // false

