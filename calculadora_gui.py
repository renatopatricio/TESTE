import tkinter as tk
from tkinter import messagebox

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Erro: divisão por zero!'
    return a / b

def calcular(operacao):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if operacao == 'soma':
            resultado = soma(a, b)
        elif operacao == 'subtrai':
            resultado = subtrai(a, b)
        elif operacao == 'multiplica':
            resultado = multiplica(a, b)
        elif operacao == 'divide':
            resultado = divide(a, b)
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

root = tk.Tk()
root.title("Calculadora Simples")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label_a = tk.Label(frame, text="Primeiro número:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(frame)
entry_a.grid(row=0, column=1)

label_b = tk.Label(frame, text="Segundo número:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(frame)
entry_b.grid(row=1, column=1)

btn_soma = tk.Button(frame, text="Soma", width=10, command=lambda: calcular('soma'))
btn_soma.grid(row=2, column=0)
btn_subtrai = tk.Button(frame, text="Subtração", width=10, command=lambda: calcular('subtrai'))
btn_subtrai.grid(row=2, column=1)
btn_multiplica = tk.Button(frame, text="Multiplicação", width=10, command=lambda: calcular('multiplica'))
btn_multiplica.grid(row=3, column=0)
btn_divide = tk.Button(frame, text="Divisão", width=10, command=lambda: calcular('divide'))
btn_divide.grid(row=3, column=1)

label_resultado = tk.Label(frame, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop() 
