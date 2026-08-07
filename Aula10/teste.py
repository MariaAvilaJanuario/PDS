import tkinter as tk

def adicionar():
    conteudo = campo.get()
    lista.insert('end', conteudo)

def remover():
    selecionados = lista.curselection()
    lista.delete(selecionados)

janela = tk.Tk()
janela.title("Exercícios")
janela.geometry("300x300")

textoCampo = tk.StringVar()
campo = tk.Entry(janela, textvariable=textoCampo)
campo.grid(row=0, column=0)

btAdicionar = tk.Button(janela, text="Adicionar", command=adicionar)
btAdicionar.grid(row=0, column=1)

lista = tk.Listbox(janela, selectmode="multiple")
lista.grid(row=1, column=0)

btRemover = tk.Button(janela, text="Remover", command=remover)
btRemover.grid(row=1, column=1)

lista.insert(0,"Maria")
lista.insert(1,"Manu")
lista.insert(3,"Fulano")

janela.mainloop()