archivo_compras= "compras.txt"
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


class Compra:
    def __init__(self, dni, fecha, nombre_producto, cantidad, precio, descuento):
        self.dni = dni
        self.fecha = fecha
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.precio = precio
        self.descuento = descuento

def añadir_compra():
    dni = input("Ingrese el DNI del cliente: ")
    fecha = input("Ingrese la fecha en la que realizó la compra (YYYY-MM-DD): ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad de productos de ese tipo que lleva: "))
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el descuento que tiene, en caso de que no tenga marque 0: "))
    return Compra(dni, fecha, nombre, cantidad, precio, descuento)

def mostrar_compras_por_producto(compras, producto):
    contador = 0
    for compra in compras:
        if compra.nombre_producto == producto:
            contador += 1
    if contador == 0:
        print(f"Ningún cliente ha comprado el producto '{producto}'.")
    else:
        print(f"{contador} clientes han comprado el producto '{producto}'.")

def eliminar_producto(compras, dni, fecha, producto):
    for compra in compras:
        if compra.dni == dni and compra.fecha == fecha and compra.nombre_producto == producto:
            compras.remove(compra)
            print("Producto eliminado correctamente.")
            return
    print("No se encontró la compra especificada.")

def listar_productos(compras):
    productos = set()
    for compra in compras:
        productos.add(compra.nombre_producto)
    print("Productos comprados:")
    for producto in productos:
        print(producto)

def listar_compras_por_cliente_fecha(compras, dni, fecha):
    total = 0
    for compra in compras:
        if compra.dni == dni and compra.fecha == fecha:
            total += (compra.precio * compra.cantidad * (1 - compra.descuento / 100))
            print(f"Producto: {compra.nombre_producto}, Precio: {compra.precio}, Importe con descuento: {compra.precio * (1 - compra.descuento / 100)}")
    print(f"Importe total de las compras realizadas por el cliente {dni} en la fecha {fecha}: {total}")

