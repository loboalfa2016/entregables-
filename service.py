def agregar_producto(inventario, nombre, precio, cantidad):
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' agregado exitosamente.")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"producto '{nombre}' no encontrado.")
        return
    else: 
        inventario.remove(producto)
        print(f"producto {nombre} eliminado exitositamente.")

def actualizar_producto(inventario, nombre, precio=None, cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"producto {nombre} no encontardo.")
        return
    if precio:
        producto["precio"] = precio
        print(f"precio del producto {nombre} actualizado exitosamente.")
    if cantidad:
        producto["cantidad"] = cantidad
        print(f"cantidad del producto {nombre} actaulizado exitosamente.")

def calcular_estadistica(inventario):
    if not inventario:
        print("el inventario esta vacio.")
        return None
    unidades_totales = sum(producto["cantidad"] for producto in inventario)
    valor_total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)
    producto_mas_caro = max(inventario, key=lambda x: x["precio"])
    producto_mayor_stock = max(inventario, key=lambda x: x["cantidad"])
    return {
        "unidades_totales": unidades_totales,
        "valor_totales": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
        
