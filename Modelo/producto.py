class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, categoria, marca, imagen):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre            # Nombre del producto
        self.descripcion = descripcion  # Descripción del producto
        self.precio = precio            # Precio del producto
        self.categoria = categoria      # Categoría del producto
        self.marca = marca              # Marca del producto
        self.imagen = imagen            # Ruta de la imagen (archivo local)

    def __str__(self):
        """Representación en formato de texto de la información básica del producto"""
        return f"Producto {self.nombre} ({self.id_producto}): {self.descripcion}, Precio: ${self.precio}, Marca: {self.marca}, Categoría: {self.categoria}"

