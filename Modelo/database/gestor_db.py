# gestor_db.py
import sqlite3
import os

# Ruta de la base de datos
DB_PATH = "Modelo/database/productos.db"

def agregar_producto(id_producto, nombre, descripcion, precio, categoria, marca, imagen_path=None):
    """Agregar un producto a la base de datos con imagen (solo almacena la ruta de la imagen por ahora)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Validar que la imagen esté disponible, solo almacenar la ruta
    if imagen_path and os.path.isfile(imagen_path):
        imagen = imagen_path
    else:
        imagen = None  # Si no se proporciona imagen, asignamos None

    # Insertar producto en la base de datos
    cursor.execute("""
        INSERT INTO productos (id_producto, nombre, descripcion, precio, categoria, marca, imagen)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (id_producto, nombre, descripcion, precio, categoria, marca, imagen))

    conn.commit()
    conn.close()

def obtener_productos():
    """Obtiene todos los productos de la base de datos"""
    try:
        conn = sqlite3.connect(DB_PATH)  # Crear una nueva conexión
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")  # Asegúrate de que esta consulta sea válida
        productos = cursor.fetchall()
        conn.close()  # Cerrar la conexión
        return productos
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        return []

def obtener_producto_por_id(id_producto):
    """Obtener un producto por su ID, incluyendo la imagen"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
    producto = cursor.fetchone()

    conn.close()

    if producto:
        id_producto, nombre, descripcion, precio, categoria, marca, imagen = producto
        
        # Solo si la imagen existe, podemos devolver la ruta
        return producto  # Devuelve los datos del producto junto con la ruta de la imagen si existe
        
    else:
        return None

def actualizar_producto(id_producto, nombre, descripcion, precio, categoria, marca, imagen_path=None):
    """Actualizar un producto en la base de datos (solo actualiza la ruta de la imagen si se proporciona)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Si se proporciona una nueva imagen, validamos y actualizamos la ruta
    if imagen_path and os.path.isfile(imagen_path):
        imagen = imagen_path
    else:
        imagen = None  # Si no se proporciona imagen, dejamos el valor como None

    cursor.execute("UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, categoria = ?, marca = ?, imagen = ? WHERE id_producto = ?",
                   (nombre, descripcion, precio, categoria, marca, imagen, id_producto))

    conn.commit()
    conn.close()

def eliminar_producto(id_producto):
    """Eliminar un producto de la base de datos"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
    conn.commit()
    conn.close()

