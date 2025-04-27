import tkinter as tk
from tkinter import ttk, messagebox


class Boleto:
    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio:.1f}"

    @property
    def precio(self):
        raise NotImplementedError("Método precio debe ser implementado por subclases")


class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)

    @property
    def precio(self):
        return 100.0


class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion

    @property
    def precio(self):
        return 50.0 if self.dias_anticipacion >= 10 else 60.0


class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion

    @property
    def precio(self):
        precio_platea = 50.0 if self.dias_anticipacion >= 10 else 60.0
        return precio_platea * 0.5


class TeatroMunicipalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")
        self.root.geometry("400x350")
        self.boletos = []

        self.crear_interfaz()

    def crear_interfaz(self):
        ttk.Label(self.root, text="Teatro Municipal", font=('Helvetica', 16, 'bold')).pack(pady=10)

        datos_frame = ttk.LabelFrame(self.root, text="Datos del Boleto", padding=10)
        datos_frame.pack(padx=10, pady=5, fill=tk.X)

        self.tipo_boleto = tk.StringVar(value="Palco")
        ttk.Radiobutton(datos_frame, text="Palco", variable=self.tipo_boleto, value="Palco",
                        command=self.actualizar_campos).grid(row=0, column=0, sticky="w")
        ttk.Radiobutton(datos_frame, text="Platea", variable=self.tipo_boleto, value="Platea",
                        command=self.actualizar_campos).grid(row=0, column=1, sticky="w")
        ttk.Radiobutton(datos_frame, text="Galeria", variable=self.tipo_boleto, value="Galeria",
                        command=self.actualizar_campos).grid(row=0, column=2, sticky="w")

        ttk.Label(datos_frame, text="Número:").grid(row=3, column=0, sticky="w", pady=(10, 0))
        self.numero_entry = ttk.Entry(datos_frame, width=10)
        self.numero_entry.grid(row=3, column=1, sticky="w", pady=(10, 0))

        ttk.Label(datos_frame, text="Cant. Dias para el Evento:").grid(row=4, column=0, sticky="w", pady=(5, 0))
        self.dias_entry = ttk.Entry(datos_frame, width=10)
        self.dias_entry.grid(row=4, column=1, sticky="w", pady=(5, 0))

        self.actualizar_campos()

        botones_frame = ttk.Frame(self.root)
        botones_frame.pack(pady=10)

        ttk.Button(botones_frame, text="Vender", command=self.vender_boleto).grid(row=0, column=0, padx=5)
        ttk.Button(botones_frame, text="Salir", command=self.root.quit).grid(row=0, column=1, padx=5)

        ttk.Separator(self.root, orient='horizontal').pack(fill=tk.X, padx=10, pady=5)

        info_frame = ttk.LabelFrame(self.root, text="Información", padding=10)
        info_frame.pack(padx=10, pady=5, fill=tk.X)

        self.info_label = ttk.Label(info_frame, text="", font=('Helvetica', 10))
        self.info_label.pack()

    def actualizar_campos(self):
        tipo = self.tipo_boleto.get()
        if tipo == "Palco":
            self.dias_entry.config(state='disabled')
            self.dias_entry.delete(0, tk.END)
        else:
            self.dias_entry.config(state='normal')

    def vender_boleto(self):
        try:
            numero = int(self.numero_entry.get())
            tipo = self.tipo_boleto.get()

            if tipo == "Palco":
                boleto = Palco(numero)
            else:
                dias_texto = self.dias_entry.get()
                if not dias_texto:
                    raise ValueError("Debe ingresar los días de anticipación")

                dias = int(dias_texto)
                if dias < 0:
                    raise ValueError("Los días no pueden ser negativos")

                if tipo == "Platea":
                    boleto = Platea(numero, dias)
                else:  # Galeria
                    boleto = Galeria(numero, dias)

            self.boletos.append(boleto)
            self.mostrar_info(boleto)

            self.numero_entry.delete(0, tk.END)
            if tipo != "Palco":
                self.dias_entry.delete(0, tk.END)
                self.dias_entry.config(state='normal')

            messagebox.showinfo("Éxito", "Boleto vendido correctamente")

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")

    def mostrar_info(self, boleto):
        self.info_label.config(text=str(boleto))


if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroMunicipalApp(root)
    root.mainloop()