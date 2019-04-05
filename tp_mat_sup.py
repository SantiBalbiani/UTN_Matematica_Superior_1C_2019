# -*- coding: utf-8 -*-
from cmath import *
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nota = tk.Label(self)
        self.nota["text"] = "ingrese los complejos en forma *Binómica* y presione Sumar"
        self.nota.pack(side="top")
        self.ingresoCampo1 = tk.Entry(self)
        self.ingresoCampo1["text"] = "campo1"
        self.ingresoCampo1.pack(side="top")
        self.ingresoCampo2 = tk.Entry(self)
        self.ingresoCampo2["text"] = "campo2"
        self.ingresoCampo2.pack(side="top")
        self.suma = tk.Button(self)
        self.suma["text"] = "Sumar"
        self.suma["command"] = self.sumar
        self.suma.pack(side="top")
        self.quit = tk.Button(self, text="Salir", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def sumar(self):
        suma =  complex(self.ingresoCampo1.get()) + complex(self.ingresoCampo2.get())
        print(suma)
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
