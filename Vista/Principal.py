# principal.py
import tkinter as tk
from Vista.catalogo_view import CatalogoView  # Asegúrate de importar la vista del catálogo

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DTR - Domicilios, Tiendas y Recetas")
        self.geometry("800x500")
        
        # Colores personalizados
        azul_oscuro = "#00132e"
        amarillo = "#ff9900"
        naranja = "#f73205"
        
        # Configuración del fondo de la ventana principal
        self.configure(bg="white")
        
        # Panel lateral
        panel_lateral = tk.Frame(self, bg=azul_oscuro, width=200)
        panel_lateral.pack(side="left", fill="y")
        
        # Título en el panel lateral
        tk.Label(panel_lateral, text="Menú", font=("Arial", 16), fg=amarillo, bg=azul_oscuro).pack(pady=20)

        # Botones del panel lateral
        tk.Button(panel_lateral, text="Historial de Ventas Mensual", command=self.abrir_historial, 
                  bg=azul_oscuro, fg=amarillo, font=("Arial", 12), relief="flat", activebackground=amarillo).pack(pady=10, fill="x")
        tk.Button(panel_lateral, text="Recomendación de Recetas", command=self.abrir_recetas, 
                  bg=azul_oscuro, fg=amarillo, font=("Arial", 12), relief="flat", activebackground=amarillo).pack(pady=10, fill="x")
        tk.Button(panel_lateral, text="Catálogo de Productos", command=self.abrir_catalogo, 
                  bg=azul_oscuro, fg=amarillo, font=("Arial", 12), relief="flat", activebackground=amarillo).pack(pady=10, fill="x")
        tk.Button(panel_lateral, text="Atención al Cliente", command=self.abrir_atencion_cliente, 
                  bg=azul_oscuro, fg=amarillo, font=("Arial", 12), relief="flat", activebackground=amarillo).pack(pady=10, fill="x")

        # Contenedor para el contenido principal
        self.contenedor = tk.Frame(self, bg="white")
        self.contenedor.pack(side="right", expand=True, fill="both")
        
        # Aquí se inicializa el frame vacío para cada vista
        self.catalogo_frame = None

    def abrir_historial(self):
        # Aquí iría el código para abrir el historial de ventas
        pass
    
    def abrir_recetas(self):
        # Aquí iría el código para abrir las recomendaciones de recetas
        pass
    
    def abrir_catalogo(self):
    # Si ya hay un frame del catálogo abierto, lo destruimos para reemplazarlo
        if self.catalogo_frame:
            self.catalogo_frame.destroy()
    
    # Creamos y mostramos la vista del catálogo
        self.catalogo_frame = CatalogoView(self.contenedor)
        self.catalogo_frame.pack(fill="both", expand=True)  # Empaquetar el frame para que se muestre


    def abrir_atencion_cliente(self):
        # Aquí iría el código para abrir la atención al cliente
        pass

# Ejecución de la aplicación
if __name__ == "__main__":
    app = Principal()  # Aquí debes usar Principal, no DTRApp
    app.mainloop()
