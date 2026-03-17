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

