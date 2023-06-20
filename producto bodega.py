#BODEGA TIENDA

from datetime import datetime
import os 
import msvcrt
import time

ListaProducto= []

def menuTienda():
    print("Bienvenido!")
    print("1)Registrar producto")
    print("2)Consultar datos")
    print("3)Listar productos")
    print("4)Salir del menú")
    opc=''
    while opc not in ['1','2','3','4']:
        opc= input("Por favor ingrese una opción:\n>")
    return opc

def registrarproducto():
    while True:
        id_producto= input("Por favor ingrese un ID (4 dígitos):\n>")
        print("ALO")
        if len(id_producto)==4 and id_producto.isalnum and productoregistrado(id_producto):
            print("Producto registrado con éxito.")
            break
        else: 
            print("Su id está usado o es incorrecto, por favor vuelva a intentar.")
            time.sleep(1)
    nombre_producto = input("Ingrese nombre producto:\n>")
    precio = int(input("Ingrese precio"))
    stock = int(input("Ingrese stock disponible inicial=\n>"))
    producto= [id_producto,nombre_producto,precio,stock]
    ListaProducto.append(producto)

def productoregistrado(id_producto):
    L=1
    while L==1:
        for producto in ListaProducto:
            for dato in producto:
                if id_producto==producto[0]:
                    L=0
                    return False
        else:
            L=0
            return True


def Consultar_datos(buscarid):
    print("=====BÚSQUEDA PRODUCTO=====")
    for producto in ListaProducto:
        if buscarid==producto[0]:
            print(f"|ID producto: {producto[0]}|\n|Nombre producto: {producto[1]}|\nPrecio: {producto[2]}|\n|Stock: {producto[3]}|")
            print("======================")
        else:
            print("Producto no se encuentra en sistema.")

def listar_productos():
    print("====PRODUCTOS DISPONIBLES===")
    print(f"================\n{ListaProducto}\n=============")

repmenu=False

while repmenu==False:
    opc=menuTienda()
    if opc=="1": registrarproducto()
    if opc=="2":
        buscarid= input("Ingrese id a buscar (largo 4 dígitos):\n>")
        if len(buscarid)==4 and buscarid.isalnum:
            Consultar_datos(buscarid)
        else:
            print("Ingrese id válido.")
    if opc=="3": listar_productos()
    if opc=="4": repmenu=True


now = datetime.now() 
print(f"{now}")
tiempo=datetime.now().time()
hora=tiempo.hour
min=tiempo.minute
sec=tiempo.second
if sec<10 and sec>0:
    print(f"Hora actual: {hora}:{min}:0{sec}")
else:
    print(f"Hora actual: {hora}:{min}:{sec}")


print("1")

