import tkinter as tk
from tkinter import messagebox

def atualizar_listas():
    lista_pizza_pendentes.delete(0, tk.END)
    lista_pizza_concluidas.delete(0, tk.END)
    for pizza in pizza_pendentes:
        lista_pizza_pendentes.insert(tk.END, pizza)
    for pizza in pizza_concluidas:
        lista_pizza_concluidas.insert(tk.END, pizza)

def manipular_tarefa(acao):
    pizza = entrada_pizza.get().strip()

    try:
        pizza_selecionada = lista_pizza_pendentes.curselection()
        pizza = lista_pizza_pendentes.get(pizza_selecionada) if pizza == "" and pizza_selecionada else pizza
    except IndexError:
        pizza_selecionada = None

    if acao == "adicionar" and pizza:
        pizza_pendentes.append(pizza)
    elif acao == "excluir" and pizza_selecionada:
        pizza_pendentes.remove(pizza)
    elif acao == "concluir" and pizza_selecionada:
        pizza_pendentes.remove(pizza)
        pizza_concluidas.append(pizza)

    entrada_pizza.delete(0, tk.END)
    atualizar_listas()


janela = tk.Tk()
janela.title("Lista de Pizza Diárias")

pizza_pendentes, pizza_concluidas = [], []

entrada_pizza = tk.Entry(janela, width=40)
entrada_pizza.grid(row=0, column=0, padx=10, pady=10)


tk.Button(janela, text="Adicionar pizza", width=15, command=lambda: manipular_tarefa("adicionar")).grid(row=0, column=1, padx=6, pady=10)


lista_pizza_pendentes = tk.Listbox(janela, height=10, width=50)
lista_pizza_pendentes.grid(row=1, column=1, padx=10, pady=10)


lista_pizza_concluidas = tk.Listbox(janela, height=10, width=50)
lista_pizza_concluidas.grid(row=1, column=2, padx=10, pady=10)


tk.Button(janela, text="Excluir pizza", width=20, command=lambda: manipular_tarefa("excluir")).grid(row=2, column=0, padx=10, pady=10)


tk.Button(janela, text="Concluir pizza", width=20, command=lambda: manipular_tarefa("concluir")).grid(row=2, column=1, padx=10, pady=10)


atualizar_listas()

janela.mainloop()
