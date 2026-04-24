""""
def calculadora_descuento (precio_base):
    if precio_base >100:
        descuento = precio_base * 0.80
    elif precio_base <=100:
        descuento = precio_base 
    return descuento

Precio_base = float(input("Ingresa el costo del producto: "))
pago_total = calculadora_descuento(Precio_base)

print("EL precio FInal es:", pago_total)
 

def validar_acceso(nombre, edad):
    if edad >= 18:
        print(f"bienvenido {nombre}, tienes acceso al sitio web.")
    else:
        print(f"LO siento {nombre}. no tienes acceso al sitio web.")
    return (nombre, edad)


Nombre = input("Ingresa tu nombre: ")
Edad = int(input("Ingresa tu edad: "))
           
acceso = validar_acceso(Nombre, Edad)

print({acceso})

def calcular_pago(x, y, z):
    sueldo_bruto = y * z
    if sueldo_bruto>2000:
        pago = sueldo_bruto * 0.90
    elif sueldo_bruto <=2000:
        pago = sueldo_bruto
    return pago

Nombre = input("IIngresa tu nombre: ")
Horas_trabajadas = float(input("Ingresa el numero de horas trabajadas: "))
Pago_hora = float(input("INgresa el pago por hora: "))

pago_total = calcular_pago(Nombre, Horas_trabajadas, Pago_hora)

print("EL pago total es:", pago_total)



# --- FUNCION 1: Hace la matemática ---
def calcular_pago(nombre, horas, pago_h):
    sueldo_bruto = horas * pago_h
    if sueldo_bruto > 2000:
        pago_final = sueldo_bruto * 0.80
    else:
        pago_final = sueldo_bruto
    return pago_final

# --- FUNCION 2: Imprime el reporte final ---
def mostrar_resumen(lista_resultados):
    print("\n--- RESUMEN DE NÓMINA ---")
    for linea in lista_resultados: 
        print(f"-> {linea}")
    print("-------------------------")

resultados = []
continuar = "SI"

while continuar.upper() == "SI":
    Nombre =input("Ingresa nombre de empleado: ")
    hrs = float(input("Ingresa Horas Trabajadas: "))
    pag = float(input("INgresa Pago por Hora:  "))
    pago_total = calcular_pago(Nombre, hrs, pag)

    resultados.append(f"{Nombre} cobrará: ${pago_total:.2f}")
    continuar = input("¿Deseas ingresar otro empleado? (SI/NO): ")

mostrar_resumen(resultados)


""


carrito = []

carrito.append("leche")
carrito.append("pan")
carrito.append("huevos")
carrito.append("queso")
continuar = "SI"
print("Carrito de compras:  \n")

for item in carrito:
    print(f"->{item}\n")

print("-------------------------")
    

while continuar.upper() == "SI": 
    continuar = input("¿Deseas agregar otro producto? (SI/NO): ")
    producto = input("INgresa un producvto para agregar al carrito: ")
    carrito.append(producto)
    if continuar.upper() == "NO":
        break

for item in carrito:
    print(f"->{item}\n")

print("-------------------------")
    
Libros = [Titulo, Autor, float(precio)]  # lista donde se guardarán los usuarios
Empleado = [Nombre, numero_empleado]  # lista donde se guardarán los empleados
carrito = []
print("--------------------Bienvenido a la libreria *Despues del Té*----------------")

print("1. Acceso empleado \n 2. Acceso cliente \n 3. Salir")
opcion = int(input("Selecciona una opcion: "))

def menu(opcion):
    if opcion == 1:
        print("Acceso empleado")
    elif opcion == 2:
        print("Acceso cliente")
    elif opcion == 3:
        print("Salir")
    else:
        print("Opcion no valida")


def acceso_empleado():
    print("Acceso empleado")
    
    #LOGICA
    print("1. Agregar libro \n 2. Ver libros \n 3. Registrar nuevo empleado \n 4. volver al menu principal")
    opcion_empleado = int(input("Selecciona una opcion: "))
    if opcion_empleado == 1:
        titulo = input("Ingresa el título del libro: ")
        Libros.append(titulo)
        autor = input("Ingresa el autor del libro: ")
        Libros.append(autor)
        precio = float(input("Ingresa el precio del libro: "))
        Libros.append(precio)
        print("Libro agregado exitosamente.")
    elif opcion_empleado == 2:
        print("Libros disponibles: ")
        #TODO Agregar logica para mostrar inventario
    elif opcion_empleado == 3:
        print("Para registrar un nuevo empleado ingrese")
        nombre = input("\n Nombre: ")
        num_empleado = int(input("Ingresa el numero de empleado: "))
        
    elif opcion_empleado == 4:
        #TODO agregar break o  funcion similar para volver al menu inicial 
        print("Hola")

def acceso_cliente():
    print("BIenvenido a tu carrito: \n ¿Deseas agregar un producto? (SI/NO)")
    continuar = "SI"

    while continuar.upper() == "SI":
        nuevo_producto = input("¿Que producto deseas agregar? ")
        carrito.append (nuevo_producto)
    continuar = input("¿Deseas agregar otro producto? (SI/NO)")
    if continuar != "SI":
        total = 
        print("Total a pagar: ",total)


# Listas globales para que todas las funciones las vean
libros = []  # Estructura: [["Libro A", "Autor", 100.0], ["Libro B", "Autor", 150.0]]
empleados = []
carrito = []

def ver_inventario_y_empleados():
    print("\n--- REPORTE DE INVENTARIO ---")
    if not libros:
        print("No hay libros en el sistema.")
    else:
        for i, libro in enumerate(libros):
            print(f"{i+1}. Título: {libro[0]} | Autor: {libro[1]} | Precio: ${libro[2]}")
    
    print("\n--- LISTA DE EMPLEADOS ---")
    if not empleados:
        print("No hay empleados registrados.")
    else:
        for emp in empleados:
            print(f"Nombre: {emp[0]} | ID: {emp[1]}")

def acceso_empleado():
    print("\n--- MENÚ EMPLEADO ---")
    print("1. Agregar libro\n2. Ver Inventario y Empleados\n3. Registrar empleado\n4. Volver")
    op = input("Selecciona: ")
    
    if op == "1":
        t = input("Título: ")
        a = input("Autor: ")
        p = float(input("Precio: "))
        libros.append([t, a, p])
        print("¡Libro guardado!")
    elif op == "2":
        ver_inventario_y_empleados()
    elif op == "3":
        n = input("Nombre: ")
        id_e = input("ID: ")
        empleados.append([n, id_e])
    elif op == "4":
        return

def acceso_cliente():
    print("\n--- BIENVENIDO A LA TIENDA ---")
    if not libros:
        print("Lo sentimos, no hay libros disponibles para comprar hoy.")
        return

    total_pagar = 0
    continuar = "SI"
    
    while continuar.upper() == "SI":
        print("\nLibros en existencia:")
        for i, libro in enumerate(libros):
            print(f"{i}. {libro[0]} (${libro[2]})")
        
        try:
            seleccion = int(input("\nIngresa el NÚMERO del libro que deseas: "))
            
            # Verificamos si el número existe en la lista de libros
            if 0 <= seleccion < len(libros):
                libro_elegido = libros[seleccion]
                carrito.append(libro_elegido[0])
                total_pagar += libro_elegido[2] # Sumamos el precio (está en la posición 2)
                print(f"Añadido: {libro_elegido[0]}")
            else:
                print("Ese número de libro no existe.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

        continuar = input("¿Deseas agregar otro producto? (SI/NO): ")

    print(f"\n--- TICKET DE COMPRA ---")
    print(f"Productos: {carrito}")
    print(f"TOTAL A PAGAR: ${total_pagar}")
    carrito.clear() # Limpiamos el carrito para el siguiente cliente

# Bucle principal
while True:
    print("\n--- LIBRERÍA 'DESPUÉS DEL TÉ' ---")
    print("1. Empleado\n2. Cliente\n3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        acceso_empleado()
    elif opcion == "2":
        acceso_cliente()
    elif opcion == "3":
        print("Cerrando sistema...")
        break






print("Calculadora")
def calculadora_descuento (precio_base):
    if precio_base >100:
        descuento = precio_base * 0.80
    elif precio_base <=100:
        descuento = precio_base 
    return descuento

Precio_base = float(input("Ingresa el costo del producto: "))
pago_total = calculadora_descuento(Precio_base)

print("EL precio FInal es:", pago_total)


"""
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
