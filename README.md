# 🛒 SuperPyMarket – Sistema de Gestión de Compras para Supermercados

> Aplicación de consola desarrollada en Python para gestionar y consultar compras realizadas por clientes, a partir de un archivo de texto estructurado.

---

## 📌 Descripción

**SuperPyMarket** es un sistema sencillo pero funcional, orientado a la gestión de compras en un entorno de supermercado. Al ejecutarse, carga automáticamente la información del archivo `compras.txt`, donde se almacenan los datos de compras históricas realizadas por los clientes.

Mediante un menú interactivo, el usuario puede consultar, filtrar, eliminar y guardar información relacionada con productos, clientes y fechas específicas.

---

## 📂 Estructura del archivo `compras.txt`

Cada línea representa una compra con el siguiente formato:

DNI,Fecha,Producto,Cantidad,Precio,Descuento
**Ejemplo:**
12345678A|2025-05-15|Pan|2|1.20|0.10
98765432B|2025-05-15|Leche|1|0.99|0.00
## 🧠 Funcionalidades disponibles

- 📥 **Carga de datos desde el archivo `compras.txt`**
- 👥 **Contar cuántos clientes han comprado un producto específico**
- 🗑️ **Eliminar un producto de una compra por DNI y fecha**
- 🧾 **Listar todos los nombres de productos comprados**
- 📅 **Consultar compras de un cliente en una fecha concreta**, con cálculo del importe total aplicando descuentos
- 💾 **Guardar los cambios en el archivo de texto**
- 🚪 **Salir del programa**

---

### Requisitos
- Python 3.7 o superior

### Cómo usar

1. Asegúrate de tener el archivo `compras.txt` en la misma carpeta que el script.
2. Ejecuta el archivo:

🛠 Tecnologías y conceptos aplicados
-📁 Lectura y escritura de archivos de texto
-🔁 Bucles y condicionales
-🗃️ Diccionarios y listas en Python
-📅 Gestión de fechas (formato string)
-🧠 Organización modular del código con funciones
-🎯 Validaciones básicas y control de errores

## 👨‍💻 Autor

Desarrollado por **Alejandro Medina Rmirez**  
Técnico en Sistemas Microinformáticos y Redes  
Estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM)

---

## 📜 Licencia

Este proyecto se distribuye bajo la **Licencia MIT**.  
Uso libre para fines educativos y personales.



