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
    if len(lista)<=1:
        return lista
    else:
        pivote=lista[0][1]
        menor=[x for x in lista[1:] if x[1]<pivote]
        igual=[x for x in lista if x[1]==pivote]
        mayor=[x for x in lista[1:] if x[1]>pivote]
        return quick_sort(menor)+igual+quick_sort(mayor)

def MostrarOrdenRepartidores():
    if not repartidor:
        print("No hay repartidores")
        return
    lista=[(nombre,dato["nombre"]) for nombre, dato in repartidor.items()]
    lista_orden=quick_sort(lista)
    print("\n Orden de repartidores por cantidad de paquetes")
    for nombre,_ in lista_orden:
        dato=repartidor[nombre]
        print(f"\n El nombre del repartidor es: {nombre}")
        print(f"\n Paquetes entregados son: {dato['paquetes']}")
        print(f"\n Zona designada es : {dato['zona']}")


def busqueda(lista, objetivo):
    if not repartidor:
        print("El repartidor no se encuentra en este sistema")
        return
    nombre_buscado = input("Ingrese el nombre del repartidor que esta buscando: ")
    for nombre in repartidor:
        if nombre.lower() == nombre_buscado.lower():
            datos = repartidor[nombre]
            print("\n Repartidor encontrado ")
            print(f"Nombre: {nombre}")
            print(f"Paquetes entregados: {datos['paquetes']}")
            print(f"Zona designada: {datos['zona']}")
            return
    print("Repardidor no encontrado")

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

while True:
    print("==Menu==")
    print("1. Ingresar Repartidores")
    print("2. Orden por cantida de paquetes entregados")
    print("3. Buscar repartidores")
    print("4. Estadistica de Repartidores")
    print("5. Salir")
    opcion=input("Seleccione una opcion: ")
    match=opcion
    match 1:

