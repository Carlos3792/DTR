from Modelo.database.gestor_db import agregar_producto, obtener_productos, obtener_producto_por_id, actualizar_producto, eliminar_producto
import os
from tkinter import filedialog  # Importamos el filedialog para seleccionar un archivo

class Controlador:
    def __init__(self):
        pass

    def crear_producto(self, id_producto, nombre, descripcion, precio, categoria, marca, imagen_path=None):
        """Crear un nuevo producto en la base de datos, sin guardar la imagen por el momento"""
        # Verificar que los campos esenciales no estén vacíos
        if not nombre or not descripcion or not precio or not categoria or not marca:
            print("Error: Todos los campos son obligatorios.")
            return

        # Simular la selección de imagen (no la guardamos por el momento)
        if imagen_path:
            print(f"Imagen seleccionada: {imagen_path}")
        else:
            print("No se ha seleccionado una imagen.")

        # Llamar al gestor_db para agregar el producto (sin imagen por ahora)
        try:
            # Aquí no procesamos la imagen, solo guardamos los otros datos
            agregar_producto(id_producto, nombre, descripcion, precio, categoria, marca, None)
            print(f"Producto {nombre} agregado con éxito.")
        except Exception as e:
            print(f"Error al agregar producto: {e}")

    def obtener_todos_los_productos(self):
        """Obtener todos los productos"""
        productos = obtener_productos()
        if productos:
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
            return productos  # Devuelves la lista de productos aquí
        else:
            print("No hay productos en la base de datos.")
            return []  # Retornas una lista vacía si no hay productos


    def obtener_producto(self, id_producto):
        """Obtener un producto por su ID"""
        producto = obtener_producto_por_id(id_producto)
        if producto:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, nombre, precio):
        """Actualizar un producto en la base de datos"""
        actualizar_producto(id_producto, nombre, precio)
        print(f"Producto con ID {id_producto} actualizado con éxito.")

    def eliminar_producto(self, id_producto):
        """Eliminar un producto de la base de datos"""
        eliminar_producto(id_producto)
        print(f"Producto con ID {id_producto} eliminado con éxito.")

    def seleccionar_imagen(self):
        """Permite al usuario seleccionar una imagen sin procesarla"""
        imagen_path = filedialog.askopenfilename(title="Seleccionar una imagen", filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if imagen_path:
            print(f"Imagen seleccionada: {imagen_path}")
        else:
            print("No se seleccionó ninguna imagen.")
        return imagen_path
