# archivo_principal.py
import tkinter as tk
from tkinter import messagebox
from Controlador.controlador import Controlador
from Vista.formulario_Agregar import FormularioAgregarProducto

class CatalogoView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.controlador = Controlador()
        self.configure(bg="white")
        
        # Título
        self.title_label = tk.Label(self, text="Catálogo de Productos", font=("Arial", 18), bg="white", fg="#f73205")
        self.title_label.pack(pady=20)
        
        # Botón para agregar productos
        self.boton_agregar_producto = tk.Button(self, text="Agregar Producto", command=self.abrir_formulario_agregar, 
                                                font=("Arial", 12), bg="#00132e", fg="#ff9900")
        self.boton_agregar_producto.pack(pady=10)
        
        # Frame para los productos (lista de productos) con scroll
        self.canvas = tk.Canvas(self, bg="white")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame dentro del canvas para contener los productos
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Agregar el scrollbar y canvas al frame principal
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Crear una ventana en el canvas que contendrá los productos
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Llamar a cargar los productos dentro del scrollable frame
        self.productos_frame = self.scrollable_frame

        # Cargar productos
        self.cargar_productos()
#-
    def cargar_productos(self):
        """Carga los productos y los muestra en la vista"""
        for widget in self.productos_frame.winfo_children():
            widget.destroy()  # Limpiamos el frame antes de cargar los productos

        productos = self.controlador.obtener_todos_los_productos()
    
        print(f"Productos obtenidos: {productos}")  # Agrega esta línea para verificar
    
        if productos:
            for idx, producto in enumerate(productos):
                row = idx // 3  # Fila en la que irá el producto
                col = idx % 3   # Columna en la que irá el producto
                self.mostrar_producto_en_lista(producto, row, col)
        else:
            tk.Label(self.productos_frame, text="No hay productos disponibles.", font=("Arial", 12), bg="white", fg="#00132e").pack(pady=10)

#-
    ###
    def mostrar_producto_en_lista(self, producto, row, col):
        """Muestra un solo producto en una cuadrícula con 3 columnas"""
        producto_frame = tk.Frame(self.productos_frame, bg="white", bd=1, relief="solid", padx=10, pady=10)
        producto_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Nombre del producto
        producto_nombre = tk.Label(producto_frame, text=producto[1], font=("Arial", 14, "bold"), bg="white", fg="#f73205")
        producto_nombre.pack(pady=(0, 5))

        # Marco simulando la imagen
        imagen_frame = tk.Frame(producto_frame, bg="gray", width=150, height=150)
        imagen_frame.pack(pady=(0, 5))

        # Categoria y marca
        categoria_marca = f"Categoría: {producto[4]}  |  Marca: {producto[5]}"
        categoria_marca_label = tk.Label(producto_frame, text=categoria_marca, font=("Arial", 10), bg="white", fg="#00132e")
        categoria_marca_label.pack(pady=(0, 5))

        # Precio
        
        try:
            precio = float(producto[2])  # Convertir a float
            precio_label = tk.Label(producto_frame, text=f"Precio: ${precio:.2f}", font=("Arial", 12), bg="white", fg="#f73205")
        except ValueError:
            precio_label = tk.Label(producto_frame, text="Precio no válido", font=("Arial", 12), bg="white", fg="#f73205")
        precio_label.pack(pady=(0, 5))

        # Botón para ver detalles
        ver_button = tk.Button(producto_frame, text="Ver Producto", command=lambda p=producto: self.abrir_producto_individual(p),
                           font=("Arial", 12), bg="#00132e", fg="#ff9900")
        ver_button.pack(side="bottom", pady=(10, 0))


    ###

    
    def abrir_formulario_agregar(self):
        """Abre un formulario para agregar un producto"""
        FormularioAgregarProducto(self, self.controlador, self.cargar_productos)

    def abrir_producto_individual(self, producto):
        """Abre una ventana para editar un producto individual"""
        self.producto_individual_window = tk.Toplevel(self)
        self.producto_individual_window.title("Detalles del Producto")
        self.producto_individual_window.geometry("300x250")
        self.producto_individual_window.configure(bg="white")
        
        # Mostrar información del producto
        self.producto_id = tk.Label(self.producto_individual_window, text=f"ID: {producto[0]}", font=("Arial", 12), bg="white")
        self.producto_id.pack(pady=10)
        
        self.nombre_label = tk.Label(self.producto_individual_window, text=f"Nombre: {producto[1]}", font=("Arial", 12), bg="white")
        self.nombre_label.pack(pady=10)
        self.precio_label = tk.Label(self.producto_individual_window, text=f"Precio: {producto[2]}", font=("Arial", 12), bg="white")
        self.precio_label.pack(pady=10)
        
        # Botón para convertir a campo de texto editable
        self.editar_button = tk.Button(self.producto_individual_window, text="Editar", command=lambda: self.editar_producto(producto),
                                       font=("Arial", 12), bg="#00132e", fg="#ff9900")
        self.editar_button.pack(pady=10)

        # Tabla de cargamentos
        self.cargamento_button = tk.Button(self.producto_individual_window, text="Agregar Cargamento", command=self.agregar_cargamento, 
                                           font=("Arial", 12), bg="#00132e", fg="#ff9900")
        self.cargamento_button.pack(pady=10)

    def editar_producto(self, producto):
        """Edita un producto"""
        nombre_editado = self.nombre_label.cget("text").split(": ")[1]  # Obtenemos el nombre del producto
        self.controlador.editar_producto(producto[0], nombre_editado)  # Ejemplo de cómo podrías editar



    def crear_entry(self, texto):
        """Convierte un texto a un campo de texto editable"""
        entry = tk.Entry(self.producto_individual_window, font=("Arial", 12))
        entry.insert(0, texto)
        return entry
    
    def guardar_edicion(self, producto):
        """Guarda los cambios realizados en un producto"""
        nuevo_nombre = self.nombre_label.winfo_children()[0].get()
        nuevo_precio = self.precio_label.winfo_children()[0].get()
        
        if nuevo_nombre and nuevo_precio:
            try:
                nuevo_precio = float(nuevo_precio)
                self.controlador.actualizar_producto(producto[0], nuevo_nombre, nuevo_precio)
                self.producto_individual_window.destroy()
                self.cargar_productos()
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
    
    def agregar_cargamento(self):
        """Simula la acción de agregar un cargamento de productos"""
        # Aquí se puede abrir otro formulario para agregar cargamento masivo
        messagebox.showinfo("Cargamento", "Funcionalidad para agregar cargamento aún no implementada.")
