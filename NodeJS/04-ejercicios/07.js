let m1 = [1,2,3,4,5,6,7,8,9,10];
let m2 = [1,2,3,4,5,6,7,8,9,10];

let resultado = 0;

for (i of m1){
    console.log(`--- Tabla del ${i} ---`);
    for(j of m2){
        resultado = i * j;

        if ((resultado % 2) !=0){
            continue;   
        }

        console.log(i,"x",j,'=',resultado);

    }
}