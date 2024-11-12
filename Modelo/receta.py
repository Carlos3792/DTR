# models/receta.py
class Receta:
    def __init__(self, receta_id, nombre, productos):
        self.receta_id = receta_id
        self.nombre = nombre
        self.productos = productos

    @staticmethod
    def obtener_recetas_relacionadas(productos_comprados):
        # Algoritmo para recomendar recetas basadas en productos comprados
        pass
