//Personaje de tv

let nombre ="Tanjirou Kamado";
let anime = "DEmon Slayer";
let edad = 16;


let personaje = {
    nombre:"Tanjirou Kamado",  //par llave-valor, el nombre es la llave y Tanjirou Kamado es el valor, las llaves se utilizan para agrupar datos relacionados, en este caso, los datos de un personaje de anime   
    anime: "Demon Slayer",
    edad: 16,

};


console.log(personaje);

console.log(personaje.nombre);

console.log(personaje['anime']); //también se puede acceder a las propiedades de un objeto utilizando corchetes, en este caso se accede a la propiedad anime del objeto personaje, esta forma es útil cuando el nombre de la propiedad es dinámico o no es un identificador válido


personaje.edad = 13; //también se pueden modificar las propiedades de un objeto, en este caso se modifica la propiedad edad del objeto personaje, ahora la edad es 13
personaje['edad'] = 15; //también se puede modificar las propiedades de un objeto utilizando corchetes, en este caso se modifica la propiedad edad del objeto personaje, ahora la edad es 15

console.log(personaje);

let llave = edad;
console.log(personaje[llave]); //también se puede acceder a las propiedades de un objeto utilizando una variable como llave, en este caso se accede a la propiedad edad del objeto personaje utilizando la variable llave, esta forma es útil cuando el nombre de la propiedad es dinámico o no es un identificador válido


delete personaje.anime;

console.log(personaje); //también se pueden eliminar las propiedades de un objeto utilizando el operador delete, en este caso se elimina la propiedad anime del objeto personaje, ahora el objeto personaje ya no tiene la propiedad anime