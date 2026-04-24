/* Nombre ancho  x alto
8k  7680 x 4320
4k 3840 x 2160
WQHS 2560 X 1440
FHD 1920 X 1080
HD 1280 X 720

 */

let obj = [ 
    {pantallas: {
        ancho : x,
        alto : y,
    }
}];    


obj.push({pantalla: 'Samsung', ancho : 1366,alto: 724});



// 1. Definimos el arreglo de objetos de forma limpia
let pantallas = [ 
    { marca: 'Dell', ancho: 1280, alto: 720 },
    { marca: 'Samsung', ancho: 1366, alto: 768 },
    { marca: 'Asus', ancho: 2560, alto: 1440 },
    { marca: 'LG', ancho: 3840, alto: 2160 }
];    

// 2. Recorremos el arreglo
for (let pantalla of pantallas) {
    let resolucion = ""; // Variable para guardar el nombre temporalmente

    switch (true) {
        case (pantalla.ancho <= 1280 && pantalla.alto <= 720):
            resolucion = "HD";
            break;
        case (pantalla.ancho <= 1920 && pantalla.alto <= 1080):
            resolucion = "FHD";
            break;
        case (pantalla.ancho <= 2560 && pantalla.alto <= 1440):
            resolucion = "WQHD";
            break;
        case (pantalla.ancho <= 3840 && pantalla.alto <= 2160):
            resolucion = "4K";
            break;
        case (pantalla.ancho <= 7680 && pantalla.alto <= 4320):
            resolucion = "8K";
            break;
        default:
            resolucion = "Valor inválido";
    }

    // Imprimimos el resultado formateado
    console.log(`La pantalla ${pantalla.marca} de ${pantalla.ancho}x${pantalla.alto} es de tipo: ${resolucion}`);
}


