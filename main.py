repartidor={}
def Ingreso():
    cantidad=int(input("Ingrese la cantidad de repartidores que participaron: "))
    for i in range(cantidad):
        nombre=input("Ingrese el nombre del repartidor: ")
        paquetes=int(input("Ingrese la cantidad de paquetes que envio: "))
        if 0<=paquetes:
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
        pivote=lista[0]
        menor=[x for x in lista[1:] if x<pivote]
        igual=[x for x in lista if x==pivote]
        mayor=[x for x in lista[1:] if x>pivote]
        return quick_sort(menor)+igual+quick_sort(mayor)

def MostrarOrdenRepartidores():
    if not repartidor:
        print("\n El repartidor no se encuentra en este sistema ")
        return
    paquetes=list(repartidor.keys())
    paquetesOrdenados=quick_sort(paquetes)
    print("\n El orden de los repartidores de mayor a menor cantidad de paquetes entregados")
