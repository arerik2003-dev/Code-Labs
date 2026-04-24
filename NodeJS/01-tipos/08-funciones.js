function saludar(){
console.log("Hola Mundo");
}

saludar(); //llamamos a la función para que se ejecute, si no la llamamos, la función no se ejecutará y no veremos el mensaje en la consola

function sumar(a,b){
    resultado=a+b;
    return resultado; //return es una palabra reservada que se utiliza para devolver un valor desde una función, en este caso, devuelve el resultado de la suma de a y b
}

console.log(sumar(5,3)); //llamamos a la función sumar con los argumentos 5 y 3, el resultado de la suma se devuelve y se imprime en la consola, en este caso, el resultado es 8;
