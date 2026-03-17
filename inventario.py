Inventario = {}

def agregar_producto(nombre, precio, cantidad):
    Inventario[nombre] = { "precio": precio, "cantidad":cantidad }
    print("producto agregado")

def mostrar_productos():
    if Inventario:
        for  nombre, producto in Inventario.items():
            print(f"{nombre}: {producto['precio']} x {producto['cantidad']}")

def eliminar_producto(nombre):
    if nombre in Inventario:
        del Inventario[nombre]
        print('eliminado con exito')
    else:
        print('no hay producto en el inventario')

def actualizar_producto(nombre, precio=None, cantidad=None):
    if nombre in Inventario:
        if precio: 
            Inventario [nombre]['precio'] = precio
        if cantidad:
            Inventario [nombre]['cantidad'] = cantidad
        print('producto actualizado con exito')
    else:
        print('producto no encontrado')

def calcular_estaditica():
    if Inventario:
        total_productos = sum(producto['cantidad'] for producto in Inventario.values())
        valor_total = sum(producto['precio'] * producto['cantidad'] for producto in Inventario.values())
        print(f"total prodcutos: {total_productos}")
        print(f"valor total del inventario: ${valor_total:.2f}")
    else:
        print("no hay producto en el inventario") 

def main():
    while True:
        print("\nMenu principal ")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Eliminar producto")
        print("4. Actualizar producto")
        print("5. Calcular estadísticas")
        print("6. Salir")
        opt = int(input("escribe una opcion"))
        match opt:
            case 1:
                while True:
                    nombre = str(input("escribe el nombre del producto"))
                    if nombre.replace(" ", " ").isalpha():
                        break
                    else:
                        print("ingrese un nombre al producto (solo letras )")
                while True:
                    try:
                        precio = float(input("ingresa el precio del producto"))
                        if precio > 0:
                            break
                        else:
                            print("error")
                    except ValueError:
                        print("error")
                while True:
                    cantidad = int(input("ingrese la cantidad a comprar"))
                    try:
                        if cantidad > 0:
                            break
                        else: 
                            print("error")
                    except ValueError:
                        print('error')
                agregar_producto(nombre, precio, cantidad)
            case 2:
                mostrar_productos()  
            case 3:
                nombre = input("ingrese el nombre del producto que desea eliminar ")
                eliminar_producto(nombre)
            case 4:
                nombre = input("escribe el producto a actualizar")
                precio = input("ingrese el precio a actualizar (sino dejalo en blanco si va a mantenerse igual)")
                cantidad = input("ingrese la cantidad (si no cambia dejalo asi dejalo en blanco)")
                precio = float(precio) if precio else None
                cantidad = float(cantidad) if precio else None
                actualizar_producto(nombre, precio, cantidad)
            case 5:
                calcular_estaditica()
            case 6:
                print("hasta luego")
                break
            case _:
                print ("error 10101010101")
            
if __name__ == "__main__":
    main()