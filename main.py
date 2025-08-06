repartidor={}
def Ingreso():
    cantidad=int(input("Ingrese la cantidad de repartidores que participaron: "))
    for i in range(cantidad):
        nombre=input("Ingrese el nombre del repartidor: ")
        paquetes=