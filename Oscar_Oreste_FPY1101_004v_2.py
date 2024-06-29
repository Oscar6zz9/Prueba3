import json
import datetime
hora = datetime.datetime.now()
fecha = hora.strftime("%Y/%m/%d %H:%M:%S")

#Lista para almacenar ventas
ventas = []

#Información de las izzas
precios = {
    "cuatroquesos": {"pequeña": 6000, "mediana": 9000, "familiar": 12000},
    "hawaiana": {"pequeña": 6000, "mediana": 9000, "familiar": 12000},
    "napolitana": {"pequeña": 5500, "mediana": 8500, "familiar": 11000},
    "pepperoni": {"pequeña": 7000, "mediana":10000, "familiar": 13000}
}

#Menú interactivo
def menu():
    print('\n--- Pizzas Duoc UC ---')
    print('1. Registrar una venta')
    print('2. Mostrar todas las ventas.')
    print('3. Buscar ventas por cliente')
    print('4. Guardar ventas en un archivo.')
    print('5. Cargar las ventas desde un archivo')
    print('6. Generar boleta.')
    print("7. Anular venta")
    print('8. Salir del programa')

#Registrar una venta
def registrar_una_venta():
    nombre= input("Nombre de cliente: ").lower()
    saborpizza= input("Ingresar tipo de pizza: cuatroquesos/hawaiana/napolitana/pepperoni: ").lower()
    tamañopizza= input("Ingresar tamaño de pizza: pequeña/mediana/familiar: ").lower()
    cantidad= int(input("Ingresar cantidad: "))
    tipocliente= input("Ingresar tipo de cliente: diurno/vespertino/administrativo: ").lower()

    if saborpizza not in precios or tamañopizza not in precios[saborpizza]:
        print("producto no existe")
        return
    
    preciounitario= precios[saborpizza][tamañopizza]

    descuento=0
    if tipocliente == "diurno":
        descuento=0.12
    elif tipocliente == "vespertino":
        descuento=0.14
    elif tipocliente == "Administrativo":
        descuento = 0.10

    preciototal= preciounitario * cantidad
    preciofinal= preciototal * (1 - descuento)

    venta = {
        "Cliente": nombre,
        "Variedad": saborpizza,
        "Tamaño": tamañopizza,
        "Cantidad": cantidad,
        "Tipo cliente": tipocliente,
        "Descuento":descuento,
        "Total_a_pagar": preciofinal   
    }
    ventas.append(venta)
    print("VENTA REGISTRADA...")

#Mostrar todas las ventas
def mostrar_ventas():
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for venta in ventas:
            print(venta)

#Buscar por cliente
def buscar_ventas():
    nombre_cliente= input("Ingrese nombre de cliente: ")
    ventas_cliente= [venta for venta in ventas if venta["Cliente"]== nombre_cliente]

    if not ventas_cliente:
        print(f"{nombre_cliente} no registra ventas.")
    else:
        for venta in ventas_cliente:
            print(venta)

#Guardar las ventas en un archivo
def guardar_ventas():
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file, indent=4)
    print("Ventas guardadas.")
    
#Cargar las vents en un archivo
def cargar_ventas():
    try:
        with open("ventas.json", "r") as file:
            ventas= json.load(file)
        print("Venta cargada desde 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo.")

#Generar boleta
def generar_boleta():
    cliente= input("Ingrese nombre del cliente: ")
    ventas_cliente= [venta for venta in ventas if venta['Cliente']== cliente]
    if ventas_cliente:
        total= sum(venta['Total_a_pagar'] for venta in ventas_cliente)
        print("\nBoleta")
        print("------------------------------")
        print("Pizzeria Duoc UC")
        print(f"fecha: {fecha}")
        print(f"Cliente: {cliente}")
        for venta in ventas_cliente:
            print(f"{venta['Variedad']} - {venta['Tamaño']} - ${venta['Total_a_pagar']}")
            print(f"Descuento: {venta['Descuento'] * 100}%")
            print(f'Total a pagar: ${total}\n')
            print("¡gracias por su compra!")
            print("------------------------------")
            
    else:
        print('no se encontraron ventas para ese cliente.')

#Anular venta
def anular_venta():
    cliente= input("Ingrese nombre del cliente: ")
    ventas_cliente= [venta for venta in ventas if venta["Cliente"]== cliente]
    if ventas_cliente:
        for venta in ventas_cliente:
            print(f"Venta anulada: {venta}")
            ventas.remove(venta)
    else:
        print('no se encontraron ventas para ese cliente.')



while True:
    menu()
    op=input("Seleccione una opción: ")

    if op == "1":
        registrar_una_venta()
    elif op == "2" :
        mostrar_ventas()
    elif op == "3" :
        buscar_ventas()
    elif op == "4" :
        guardar_ventas()
    elif op == "5" :
        cargar_ventas()
    elif op == "6" :
        generar_boleta()
    elif op == "7" :
        anular_venta()
    elif op == "8" :
        print("Saliendo del Programa")
        break
    else:
        print("opcion no valida")