repartidor={}
def Ingreso():
    cantidad=int(input("Ingrese la cantidad de repartidores que participaron: "))
    for i in range(cantidad):
        nombre=input("Ingrese el nombre del repartidor: ")
        paquetes=int(input("Ingrese la cantidad de paquetes que envio: "))
        if paquetes<0:
                print("La cantidad de paquetes no puede ser negativa")
        else:
            print("Dato guardado correcatamente")
        zona=input("Ingrese la zona donde se le asigno repartir dichos paquetes: ")
        repartidor[nombre]={
            "paquetes": paquetes,
            "zona":zona
        }

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0][1]
        menor = [x for x in lista[1:] if x[1] < pivote]
        igual = [x for x in lista if x[1] == pivote]
        mayor = [x for x in lista[1:] if x[1] > pivote]
        return quick_sort(mayor) + igual + quick_sort(menor)

def MostrarOrdenRepartidores():
    if not repartidor:
        print("No hay repartidores")
        return
    lista = [(nombre, dato["paquetes"]) for nombre, dato in repartidor.items()]
    lista_orden = quick_sort(lista)
    print("\n Orden de repartidores por cantidad de paquetes (mayor a menor):")
    for nombre, _ in lista_orden:
        dato = repartidor[nombre]
        print(f"\n Repartidor: {nombre}")
        print(f" Paquetes entregados: {dato['paquetes']}")
        print(f" Zona: {dato['zona']}")

def busqueda():
    if not repartidor:
        print("El repartidor no se encuentra en este sistema")
        return
    nombre_buscado = input("Ingrese el nombre del repartidor que está buscando: ")
    for nombre in repartidor:
        if nombre.lower() == nombre_buscado.lower():
            datos = repartidor[nombre]
            print("\n Repartidor encontrado:")
            print(f"   Nombre: {nombre}")
            print(f"   Paquetes entregados: {datos['paquetes']}")
            print(f"   Zona designada: {datos['zona']}")
            return
    print(" Repartidor no encontrado")

def Estadistica():
    if not repartidor:
        print("No hay repartidores registrados")
        return
    total=0
    contador=0
    max=None
    min=None
    max_repartidores=[]
    min_repartidores=[]
    for nombre,dato in repartidor.items():
        paquetes=dato['paquetes']
        total+=paquetes
        contador+=1
        if max is None or paquetes>max:
            max=paquetes
            max_repartidores=['nombre']
        elif paquetes==max:
            max_repartidores.append(nombre)
        if min is None or paquetes<min:
            min=paquetes
            min_repartidores=['nombre']
        elif paquetes==min:
            min_repartidores.append(nombre)
    promedio=total/contador
    print("\n Estadistica general de los repartidores")
    print(f"\n Total de paquetes entregados: {total}")
    print(f"Promedio de paquetes entregados: {promedio:.2f}")
    print(f"\n El repartidor(es) con mas entregas es: ({max} paquetes):")
    for nombre in max_repartidores:
        print(f"  -{nombre}")
    print(f"\nRepartidor(es) con menos entregas ({min} paquetes):")
    for nombre in min_repartidores:
        print(f"   - {nombre}")

while True:
    print("\n== Menú ==")
    print("1. Ingresar repartidores")
    print("2. Orden por cantidad de paquetes entregados")
    print("3. Buscar repartidor por nombre")
    print("4. Estadísticas de repartidores")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            Ingreso()
        case "2":
            MostrarOrdenRepartidores()
        case "3":
            busqueda()
        case "4":
            Estadistica()
        case "5":
            print(" Programa finalizado.")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")


