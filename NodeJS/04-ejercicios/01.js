function Mayor(a, b){
    if(a>b){
        resultado = a;
    }else if (b>a){
        resultado = b;
    }
    return resultado

    //return (a>b) ? a:b;
}

let mayor = Mayor (10,5);

console.log(mayor)
