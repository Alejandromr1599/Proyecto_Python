import os
archivo_compras = "compras.txt"
def cargar_compras():
    compras = {}
    try:
        archivo = open("compras.txt")
        for linea in archivo:
                dni, fecha, producto, cantidad, precio, descuento = linea.strip().split(',')
                if dni not in compras:
                    compras[dni] = []
                compras[dni].append({
                    'fecha': fecha,
                    'producto': producto,
                    'cantidad': int(cantidad),
                    'precio': float(precio),
                    'descuento': float(descuento)
                })
    except FileNotFoundError:
        print(f"El archivo no existe. Se creará uno nuevo al finalizar el programa.")
    except Exception as e:
        print(f"Error al cargar compras desde el archivo: {e}")
    
    return compras

def guardar_compras(compras):
    try:
        with open(archivo_compras, 'w') as archivo:
            for dni, lista_compras in compras.items():
                for compra in lista_compras:
                    archivo.write(f"{dni},{compra['fecha']},{compra['producto']},"
                                  f"{compra['cantidad']},{compra['precio']},{compra['descuento']}\n")
    except Exception as e:
        print(f"Error al guardar compras en el archivo: {e}")

def main():

    clientes = cargar_compras()

    def contar_clientes_producto():
        producto = input("Ingrese el nombre del producto: ")
    
        total_clientes = sum(1 for compras in clientes.values() for compra in compras if compra['producto'] == producto)

        if total_clientes > 0:
            print(f"{total_clientes} clientes han comprado el producto {producto}.")
        else:
            print("Error: El producto no ha sido comprado por ningún cliente.")


    def eliminar_producto_compra():
        dni = input("Ingrese DNI del cliente: ")
        fecha = input("Ingrese la fecha de compra: ")
        producto = input("Ingrese el nombre del producto a eliminar: ")

        if dni in clientes and any(compra['producto'] == producto for compra in clientes[dni]):
            clientes[dni] = [compra for compra in clientes[dni] if compra['producto'] != producto]
            print(f"Producto {producto} eliminado correctamente.")
        else:
            print("Error: El producto no existe en la compra especificada.")


    def listar_nombres_productos():
        productos = set(compra['producto'] for compras in clientes.values() for compra in compras)
        print("Nombres de productos comprados:")
        for producto in productos:
            print(producto)


    def listar_compras_cliente_fecha():
        dni = input("Ingrese DNI del cliente: ")
        fecha = input("Ingrese la fecha de compra: ")

        if dni in clientes:
            compras_cliente_fecha = [compra for compra in clientes[dni] if compra['fecha'] == fecha]

            if compras_cliente_fecha:
                total_importe = 0

                for compra in compras_cliente_fecha:
                    importe_con_descuento = compra['cantidad'] * (compra['precio'] - compra['descuento'])
                    total_importe += importe_con_descuento

                    print(f"Producto: {compra['producto']}, Precio: {compra['precio']}, "
                      f"Importe con Descuento: {importe_con_descuento}")

                print(f"\nImporte Total de las Compras en {fecha} por el Cliente {dni}: {total_importe}")
            else:
                print("No hay compras registradas para el cliente en la fecha especificada.")
        else:
            print("Error: Cliente no encontrado.")


    while True:
        print("\nMenú:")
        print("1. Cargar información desde el archivo")
        print("2. Contar clientes que han comprado un producto")
        print("3. Eliminar producto de una compra")
        print("4. Listar nombres de productos comprados")
        print("5. Listar compras de un cliente en una fecha")
        print("6. Guardar información en el archivo")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            clientes = cargar_compras()
            print("Información cargada correctamente desde el archivo.")
        elif opcion == '2':
            contar_clientes_producto()
            pass
        elif opcion == '3':
            eliminar_producto_compra()
            pass
        elif opcion == '4':
            listar_nombres_productos()
            pass
        elif opcion == '5':
            listar_compras_cliente_fecha()
            pass
        elif opcion == '6':
            guardar_compras(clientes)
            print("Información guardada correctamente en el archivo.")
        elif opcion == '7':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 7.")

if __name__ == "__main__":
    main()

