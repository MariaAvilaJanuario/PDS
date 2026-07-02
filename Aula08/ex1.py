import tkinter as tk

janela = tk.Tk()
janela.geometry("450x350")

A = tk.Label(janela, text="A")
A.place(x=100, y=60)

B = tk.Label(janela, text="B")
B.place(x=360, y=10)

C = tk.Label(janela, text="C")
C.place(x=15, y=250)

D = tk.Label(janela, text="D")
D.place(x=360, y=280)

E = tk.Label(janela, text="E")
E.place(x=200, y=175)

janela.mainloop()