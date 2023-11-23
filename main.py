import psutil
import tkinter as tk
from tkinter import messagebox

def obtener_top_procesos(n):
    # Obtener procesos y sus usos de memoria
    procesos = [(proc.pid, proc.name(), proc.memory_info().rss) for proc in psutil.process_iter(['pid', 'name', 'memory_info'])]
    # Ordenar por uso de memoria
    procesos.sort(key=lambda proc: proc[2], reverse=True)
    return procesos[:n]

def mostrar_ventana(procesos):
    ventana = tk.Tk()
    ventana.withdraw()  # Esconde la ventana principal
    mensaje = "\n".join([f"{pid} - {nombre}: {memoria / (1024 * 1024):.2f} MB" for pid, nombre, memoria in procesos])
    messagebox.showinfo("Top 5 procesos por uso de memoria", mensaje)
    ventana.destroy()

def main():
    top_procesos = obtener_top_procesos(10)
    mostrar_ventana(top_procesos)

if __name__ == "__main__":
    main()
