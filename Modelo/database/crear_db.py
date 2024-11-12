import sqlite3

DB_PATH = "productos.db"

def crear_base_de_datos():
    # Conectar a la base de datos
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Eliminar la tabla si existe
    cursor.execute("DROP TABLE IF EXISTS productos")

    # Crear tabla de productos con todas las columnas necesarias
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            categoria TEXT,
            marca TEXT,
            imagen TEXT
        )
    """)

    # Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()

# Llamar a la función para crear la base de datos
crear_base_de_datos()
