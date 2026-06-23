def validar_producto(producto):
    return producto.strip() != ""

def validar_stock(stock):
    try:
        return int(stock) >= 0
    except:
        return False

def validar_precio(precio):
    try:
        return float(precio) > 0
    except:
        return False
    
def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción(1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opción entre 1 y 6.")
        except:
            print("Debe ingresar un número válido.")
                        
def agregar_producto(lista):
    nombre = input("Ingrese el nombre del producto: ")

    if not validar_producto(nombre):
        print("El nombre no puede estar vacío ni ser solo espacios en blanco")
        return

    stock_input = input("Ingrese stock: ")
    if not validar_stock(stock_input):
        print("El stock debe ser un número entero mayor o igual que cero.")
        return

    precio_input = input("Ingrese precio: ")
    if not validar_precio(precio_input):
        print("El precio debe ser un número decimal mayor que cero.")
        return
    
    producto = {
        "nombre": nombre,
        "stock": int(stock_input),
        "precio": float(precio_input),
        "disponible": False 
    }

    lista.append(producto)
    print("Producto registrado correctamente.")

def buscar_producto(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre.lower(): 
            return -1

def actualizar_estado(lista):
    for producto in lista:
        if producto["stock"] > 0: 
            producto["disponible"] = True
        else:
            producto["disponible"] = False
            
def mostrar_productos(lista):
    actualizar_estado(lista) 

    if len(lista) == 0:
        print("No existen productos registrados.")
        return

    print("\n=== LISTA DE PRODUCTOS ===")

    for producto in lista:
        print(f"Nombre: {producto['nombre']}")
        print(f"Stock: {producto['stock']}")
        print(f"Precio: {producto['precio']}")
        
        if producto["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN STOCK")

        print("*" * 45)

productos = []

while True:
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        agregar_producto(productos)
        
    elif opcion == 2:
        nombre = input("Ingresa el nombre del producto a buscar: ")
        posicion = buscar_producto(productos, nombre) 
        if posicion != -1: 
            print("\nProducto encontrado!!")
            print(f"Posición en la lista: {posicion}")
            print(productos[posicion])
        else:
            print(f"El producto '{nombre}' no se encuentra registrado.")
            
    elif opcion == 3:
        nombre = input("Ingresa el nombre del producto a eliminar: ")
        posicion = buscar_producto(productos, nombre)
        
        if posicion != -1:
            productos.pop(posicion)
            print("Producto eliminado correctamente")
        else:
            print(f"El producto '{nombre}' no se encuentra registrado")
            
    elif opcion == 4:
        actualizar_estado(productos)
        print("Productos actualizados según el stock.")
        
    elif opcion == 5:
        mostrar_productos(productos)
        
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break