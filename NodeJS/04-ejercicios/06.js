let meta = {
    precioTotal: 1899,
    ahorroActual: 300,
}


function pagoSemanal(pago){
    let semana=0;

    while(meta.ahorroActual<=meta.precioTotal){
        semana++;
        meta.ahorroActual+=pago;
        if (meta.ahorroActual>=meta.precioTotal)
            break
    }
    return {
        semanaFinal:semana,
        totalAhorrado:meta.ahorroActual,
    }
}

let semanal = pagoSemanal(300);

// La forma correcta de imprimir los resultados:
console.log("Me alcanza en la semana:", semanal.semanaFinal);
console.log("El saldo final es:", semanal.totalAhorrado);