import servicios
import archivos

inventario = []

while True:
    print("\nMenú principal")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            servicios.agregar_producto(inventario, nombre, precio, cantidad)
        case "2":
            servicios.mostrar_inventario(inventario)
        case "3":
            nombre = input("Ingrese el nombre del producto: ")
            producto = servicios.buscar_producto(inventario, nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado")
        case "4":
            nombre = input("Ingrese el nombre del producto: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            servicios.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
        case "5":
            nombre = input("Ingrese el nombre del producto: ")
            servicios.eliminar_producto(inventario, nombre)
        case "6":
            estadisticas = servicios.calcular_estadisticas(inventario)
            print(estadisticas)
        case "7":
            ruta = input("Ingrese la ruta del archivo CSV: ")
            archivos.guardar_csv(inventario, ruta)
        case "8":
            ruta = input("Ingrese la ruta del archivo CSV: ")
            inventario = archivos.cargar_csv(ruta)
        case "9":
            break
        case _:
            print("Opción inválida")