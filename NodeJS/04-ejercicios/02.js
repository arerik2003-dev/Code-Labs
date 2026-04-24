/* Nombre ancho  x alto
8k  7680 x 4320
4k 3840 x 2160
WQHS 2560 X 1440
FHD 1920 X 1080
HD 1280 X 720

 */
function nombreResolucion(ancho, alto){

    switch (true){
        case (ancho<=1280 && alto<=720):
            return "HD";
        case (ancho<=1920 && alto <= 1080):
            return "FHD";
        case (ancho<=2560 && alto <= 1440):
            return "WQHS";
        case (ancho<=3840 && alto <= 2160):
            return "4K";
        case (ancho<=7680 && alto <= 4320):
            return "8K";
        default:
            console.log("Valor incorrecto");
    }

}
let nombre = nombreResolucion(1366,768);

console.log(nombre);
