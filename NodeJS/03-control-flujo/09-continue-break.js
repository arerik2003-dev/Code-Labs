let i = o;

while (i<6){
    
    i++;
    if (i ===2){
        continue;//sera ignorado, y pasa a la siguiente iteracion
    }
    if (i ===4){
        break;//se detiene la ejecucion del loop, y ademas se puede aplicar a todas las sentencias condicionales
    }
    console.log(i);
}

