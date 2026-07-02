import tkinter as tk

janela = tk.Tk()

titulo = tk.Label(text="Tabela", padx=20, pady=20, bd=2, relief="solid")
posicao10 = tk.Label(text="A", padx=20, pady=20, bd=2, relief="solid")
posicao11 = tk.Label(text="B", padx=20, pady=20, bd=2, relief="solid")
posicao12 = tk.Label(text="C", padx=20, pady=20, bd=2, relief="solid")
posicao22 = tk.Label(text="D", padx=20, pady=20, bd=2, relief="solid")

titulo.grid(row=0, column=0, columnspan=3)
posicao10.grid(row=1, column=0, rowspan=2)
posicao11.grid(row=1, column=1)
posicao12.grid(row=1, column=2)
posicao22.grid(row=2, column=2, columnspan=2)

janela.mainloop()