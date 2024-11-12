# models/historial_venta.py
class HistorialVenta:
    def __init__(self, venta_id, fecha, producto_id, cantidad, total):
        self.venta_id = venta_id
        self.fecha = fecha
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.total = total

    @staticmethod
    def obtener_ventas_mensuales(mes, año):
        # Aquí harías la consulta a la base de datos para obtener las ventas del mes/año
        pass
