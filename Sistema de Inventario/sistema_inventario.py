import tkinter as tk
from tkinter import messagebox

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}'

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad, precio):
        nuevo_producto = Producto(nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        return f'Producto "{nombre}" agregado con éxito.'

    def mostrar_productos(self):
        if not self.productos:
            return "No hay productos en el inventario."
        else:
            return '\n'.join([str(producto) for producto in self.productos])

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def actualizar_cantidad(self, nombre, cantidad):
        producto = self.buscar_producto(nombre)
        if producto:
            producto.cantidad = cantidad
            return f'Cantidad del producto "{nombre}" actualizada a {cantidad}.'
        else:
            return f'Producto "{nombre}" no encontrado.'

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            return f'Producto "{nombre}" eliminado del inventario.'
        else:
            return f'Producto "{nombre}" no encontrado.'

class InventarioApp:
    def __init__(self, root):
        self.inventario = Inventario()
        self.root = root
        self.root.title("Sistema de Inventario")

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame, text="Sistema de Inventario", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_button = tk.Button(self.frame, text="Agregar Producto", command=self.agregar_producto)
        self.add_button.grid(row=1, column=0, pady=5)

        self.show_button = tk.Button(self.frame, text="Mostrar Productos", command=self.mostrar_productos)
        self.show_button.grid(row=1, column=1, pady=5)

        self.search_button = tk.Button(self.frame, text="Buscar Producto", command=self.buscar_producto)
        self.search_button.grid(row=2, column=0, pady=5)

        self.update_button = tk.Button(self.frame, text="Actualizar Cantidad", command=self.actualizar_cantidad)
        self.update_button.grid(row=2, column=1, pady=5)

        self.delete_button = tk.Button(self.frame, text="Eliminar Producto", command=self.eliminar_producto)
        self.delete_button.grid(row=3, column=0, pady=5)

        self.exit_button = tk.Button(self.frame, text="Salir", command=self.root.quit)
        self.exit_button.grid(row=3, column=1, pady=5)

    def agregar_producto(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Agregar Producto")

        tk.Label(self.new_window, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.new_window, text="Cantidad:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.new_window, text="Precio:").grid(row=2, column=0, padx=10, pady=5)

        self.nombre_entry = tk.Entry(self.new_window)
        self.cantidad_entry = tk.Entry(self.new_window)
        self.precio_entry = tk.Entry(self.new_window)

        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)
        self.cantidad_entry.grid(row=1, column=1, padx=10, pady=5)
        self.precio_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.new_window, text="Agregar", command=self.save_producto).grid(row=3, column=0, columnspan=2, pady=10)

    def save_producto(self):
        nombre = self.nombre_entry.get()
        try:
            cantidad = int(self.cantidad_entry.get())
            precio = float(self.precio_entry.get())
            mensaje = self.inventario.agregar_producto(nombre, cantidad, precio)
            messagebox.showinfo("Info", mensaje)
            self.new_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Cantidad y Precio deben ser números válidos.")

    def mostrar_productos(self):
        productos = self.inventario.mostrar_productos()
        messagebox.showinfo("Productos en Inventario", productos)

    def buscar_producto(self):
        self.search_window = tk.Toplevel(self.root)
        self.search_window.title("Buscar Producto")

        tk.Label(self.search_window, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.search_entry = tk.Entry(self.search_window)
        self.search_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.search_window, text="Buscar", command=self.show_producto).grid(row=1, column=0, columnspan=2, pady=10)

    def show_producto(self):
        nombre = self.search_entry.get()
        producto = self.inventario.buscar_producto(nombre)
        if producto:
            messagebox.showinfo("Producto Encontrado", str(producto))
        else:
            messagebox.showerror("Error", f'Producto "{nombre}" no encontrado.')
        self.search_window.destroy()

    def actualizar_cantidad(self):
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Actualizar Cantidad")

        tk.Label(self.update_window, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.update_window, text="Nueva Cantidad:").grid(row=1, column=0, padx=10, pady=5)

        self.update_nombre_entry = tk.Entry(self.update_window)
        self.update_cantidad_entry = tk.Entry(self.update_window)

        self.update_nombre_entry.grid(row=0, column=1, padx=10, pady=5)
        self.update_cantidad_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.update_window, text="Actualizar", command=self.save_update).grid(row=2, column=0, columnspan=2, pady=10)

    def save_update(self):
        nombre = self.update_nombre_entry.get()
        try:
            cantidad = int(self.update_cantidad_entry.get())
            mensaje = self.inventario.actualizar_cantidad(nombre, cantidad)
            messagebox.showinfo("Info", mensaje)
            self.update_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número válido.")

    def eliminar_producto(self):
        self.delete_window = tk.Toplevel(self.root)
        self.delete_window.title("Eliminar Producto")

        tk.Label(self.delete_window, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.delete_entry = tk.Entry(self.delete_window)
        self.delete_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.delete_window, text="Eliminar", command=self.confirm_delete).grid(row=1, column=0, columnspan=2, pady=10)

    def confirm_delete(self):
        nombre = self.delete_entry.get()
        mensaje = self.inventario.eliminar_producto(nombre)
        messagebox.showinfo("Info", mensaje)
        self.delete_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
