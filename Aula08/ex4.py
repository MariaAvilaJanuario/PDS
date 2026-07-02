import tkinter as tk

janela = tk.Tk()
janela.geometry("530x300")

bolo = tk.PhotoImage(file="bolo.png")
cookie = tk.PhotoImage(file="cookie.png")
maca = tk.PhotoImage(file="maçã.png")

titulo = tk.Label(janela, 
                 text="Imagens!",
                 fg="black",
                 font=["Arial", 15, "bold"])

imagem1 = tk.Label(image=bolo,
                   text="Bolo",
                   compound="bottom",
                   padx=10,
                   pady=10)

imagem2 = tk.Label(image=cookie,
                   text="Cookie",
                   compound="top",
                   padx=10,
                   pady=10)

imagem3 = tk.Label(image=maca,
                   text="Maça",
                   compound="center",
                   padx=10,
                   pady=10)

titulo.grid(row=0, column=0, columnspan=3)
imagem1.grid(row=1, column=0)
imagem2.grid(row=1, column=1)
imagem3.grid(row=1, column=2)

janela.mainloop()