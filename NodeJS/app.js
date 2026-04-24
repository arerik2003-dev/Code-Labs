const http = require('http');

const hostname = "127.0.0.1";
const port = 3000;
const server = http.createServer((req, res) => { //esto es un callback, es una función que se ejecuta cuando el servidor recibe una petición
    res.statusCode = 200; //status code es el código de estado de la respuesta, 200 significa que la petición fue exitosa
    res.setHeader('Content-Type', 'text/plain'); //setHeader es un método que se utiliza para establecer el encabezado de la respuesta, en este caso se establece el tipo de contenido como texto plano
    res.end('Hola Mundo\n'); //end es un método que se utiliza para finalizar la respuesta, en este caso se envía el mensaje "Hola Mundo" al cliente
}) 

server.listen(port, hostname,() => { //listen es un método que se utiliza para iniciar el servidor, en este caso se inicia en el puerto 3000 y en la dirección IP
    console.log(`Servidor corriendo en http://${hostname}:${port}/`); //cuando el servidor esté corriendo, se imprimirá un mensaje en la consola indicando la dirección del servidor
});

