import csv

def guardar_cvs(inventario, ruta):
    if not inventario:
        print("el inventario esta vacio.")
        return
    confirmacion = input(f"desea sobreescribir el archivo {ruta} ? (s/n)")
    if confirmacion.upper() != "S":
        print("operacion cancelada.")
        return
    try:
        with open(ruta, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "precio", "cantidad"])
            for producto in inventario:
                writer.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
            print(f"inventario guardado exitosamente en {ruta}.")
    except Exception as e:
        print(f"error al guatdar en el inventarion: {e}")

def cargar_csv(ruta):
    try:
        with open(ruta, "r") as file:
            reader = csv.DictReader(file)
            inventario = []
            next(reader)
            for row in reader:
                nombre, precio, cantidad = row["nombre"], float(row["precio"]), int(row["cantidad"])
                inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            print(f"inventario cargado exitosamente desde {ruta}.")
            return inventario
    except Exception as e:
        print(f"error al cargar el inventario: {e}")
        return []
    