let animales =['chanchito', 'caballo'];

console.log(animales);

console.log(animales[0]); //acceder al primer elemento del array, los arrays son estructuras de datos que permiten almacenar múltiples valores en una sola variable, los elementos del array se acceden mediante su índice, que comienza en 0

animales.push('perro'); //agregar un elemento al final del array, el método push se utiliza para agregar un elemento al final del array, en este caso se agrega el elemento 'perro' al array animales
animales.unshift('gato'); //agregar un elemento al principio del array, el método unshift se utiliza para agregar un elemento al principio del array, en este caso se agrega el elemento 'gato' al array animales

console.log(animales);

animales.pop(); //eliminar el último elemento del array, el método pop se utiliza para eliminar el último elemento del array, en este caso se elimina el elemento 'perro' del array animales
animales.shift(); //eliminar el primer elemento del array, el método shift se utiliza para eliminar el primer elemento del array, en este caso se elimina el elemento 'gato' del array animales

console.log(animales);

animales[1] = 'vaca'; //modificar un elemento del array, los elementos del array se pueden modificar asignando un nuevo valor a su índice, en este caso se modifica el elemento en el índice 1 del array animales, ahora el elemento en el índice 1 es 'vaca'

console.log(animales);

console.log(animales.length); //obtener la longitud del array, la propiedad length se utiliza para obtener la longitud del array, en este caso se obtiene la longitud del array animales, que es 2      

animales.splice(3, 0, 'oveja'); //agregar un elemento en una posición específica del array, el método splice se utiliza para agregar o eliminar elementos en una posición específica del array, en este caso se agrega el elemento 'oveja' en la posición 3 del array animales, el segundo argumento es 0 porque no se va a eliminar ningún elemento

console.log(animales);