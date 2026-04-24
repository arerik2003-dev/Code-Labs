

"""
print("Bienvenido a esta calculadora de Python")
print("Elige 1 opcion\n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = int(input("¿Que operacion realizar?"))
#if opcion == 1:
  #  num1 = int(input("INgresa el primer numero:"))
   
    # num2 = int(input("INgresa el segundo numero:"))
    #resultado =num1 + num2 
    #print("EL resu8ltado es:", resultado)
#elif opcion == 2:
 #   num1=
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if opcion == 1:
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == 2:
    resultado = num1 - num2
    print("EL resultadop es:", resultado)
elif opcion == 3:
    resultado = num1 * num2
    print("EL resultado es:", resultado)
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
    else: 
        print("Error: No se puede dividir por cero.")
else:
    print("Opcion no valida")

    
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 
kilometers_to_miles = ###

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


    """
temps = [22, 28, 18,31, 25, 27, 30]

for i in range(len(temps)-1):
    if temps[i]>temps[i+1]:
        temps[i], temps[i+1] = temps[i+1], temps[i]

print(temps[-1])

collatz = int(input("Ingresa un numero: "))
while collatz != 1:
    print(collatz, end=" ")
    if collatz % 2 == 0:
        collatz = collatz // 2
    else:
        collatz = 3 * collatz + 1
print(collatz)