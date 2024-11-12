# producto_info.py

from Modelo.producto import Producto  # Importa la clase Producto desde el archivo producto.py

class ProductoInfo:
    def __init__(self, producto, cantidad, fecha_ingreso, fecha_fabricacion, fecha_vencimiento):
        self.producto = producto
        self.cantidad = cantidad
        self.fecha_ingreso = fecha_ingreso
        self.fecha_fabricacion = fecha_fabricacion
        self.fecha_vencimiento = fecha_vencimiento
        self.stock_minimo = 10

    def actualizar_stock(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
        else:
            raise ValueError("No hay suficiente cantidad en stock para realizar la venta.")

    def reponer_stock(self, cantidad_reponida):
        self.cantidad += cantidad_reponida

    def esta_vencido(self):
        from datetime import datetime
        fecha_actual = datetime.now().date()
        return self.fecha_vencimiento < fecha_actual

    def es_disponible(self):
        return self.cantidad > 0 and not self.esta_vencido()

    def __str__(self):
        return (f"{self.producto.nombre} - Stock: {self.cantidad}, Fecha de ingreso: {self.fecha_ingreso}, "
                f"Fecha de fabricación: {self.fecha_fabricacion}, Fecha de vencimiento: {self.fecha_vencimiento}")

