# formulario_agregar.py
import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
import os

class FormularioAgregarProducto(tk.Toplevel):
    def __init__(self, master, controlador, callback_producto_agregado):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.callback_producto_agregado = callback_producto_agregado
        self.title("Agregar Producto")
        self.geometry("400x500")
        self.configure(bg="white")

        # Crear un canvas con scrollbar
        canvas = tk.Canvas(self, bg="white")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Campos para agregar cada atributo del producto
        fields = {
            "Nombre del Producto": "nombre_entry",
            "Descripción del Producto": "descripcion_entry",
            "Precio del Producto": "precio_entry",
            "Categoría del Producto": "categoria_entry",
            "Marca del Producto": "marca_entry",
            "Imagen del Producto": "imagen_path"  # Ruta de imagen
        }

        self.entries = {}
        for label, var_name in fields.items():
            tk.Label(scrollable_frame, text=label, font=("Arial", 12), bg="white").pack(pady=5)
            entry = tk.Entry(scrollable_frame, font=("Arial", 12))
            entry.pack(pady=5)
            self.entries[var_name] = entry

        # Previsualización de imagen
        self.image_label = tk.Label(scrollable_frame, bg="white")
        self.image_label.pack(pady=10)

        # Botón para seleccionar imagen
        tk.Button(scrollable_frame, text="Seleccionar Imagen", command=self.seleccionar_imagen,
                  font=("Arial", 12), bg="#00132e", fg="#ff9900").pack(pady=10)

        # Botón para agregar el producto
        boton_agregar = tk.Button(scrollable_frame, text="Agregar", command=self.agregar_producto,
                                  font=("Arial", 12), bg="#00132e", fg="#ff9900")
        boton_agregar.pack(pady=10)

    def seleccionar_imagen(self):
        """Permite seleccionar una imagen y guardar una copia en la carpeta DTR/Modelo/database"""
        filepath = filedialog.askopenfilename(
            title="Seleccionar Imagen",
            filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if filepath:
            try:
                # Redimensionar la imagen para mostrarla en la interfaz
                photo = tk.PhotoImage(file=filepath)
                photo = photo.subsample(int(photo.width() / 100), int(photo.height() / 100))  # Redimensiona a 100x100
                self.image_label.configure(image=photo)
                self.image_label.image = photo  # Mantener referencia para evitar que se pierda la imagen

                # Guardar una copia de la imagen en la carpeta DTR/Modelo/database
                destination_dir = "DTR/Modelo/database"
                os.makedirs(destination_dir, exist_ok=True)
                destination_path = os.path.join(destination_dir, os.path.basename(filepath))

                # Copiar el archivo de imagen a la carpeta destino
                shutil.copy(filepath, destination_path)

                # Actualizar la entrada con la nueva ruta
                self.entries["imagen_path"].delete(0, tk.END)
                self.entries["imagen_path"].insert(0, destination_path)

                messagebox.showinfo("Éxito", f"Imagen guardada exitosamente en {destination_path}")

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    def agregar_producto(self):
        """Agregar producto usando el controlador"""
        nombre = self.entries["nombre_entry"].get()
        descripcion = self.entries["descripcion_entry"].get()
        precio = self.entries["precio_entry"].get()
        categoria = self.entries["categoria_entry"].get()
        marca = self.entries["marca_entry"].get()
        imagen = self.entries["imagen_path"].get()

        if all([nombre, descripcion, precio, categoria, marca, imagen]):
            try:
                precio = float(precio)
                self.controlador.crear_producto(None, nombre, descripcion, precio, categoria, marca, imagen)
                messagebox.showinfo("Éxito", "Producto agregado exitosamente")
                self.callback_producto_agregado()  # Llamar a la función de callback para recargar productos
                self.destroy()
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
