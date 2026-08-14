import tkinter as tk

def clica():
    selecionado = lista1.curselection()[0]
    if selecionado == 0:
        lista2.delete(0,"end")
        lista2.insert(0, "Metro ==> Pés")
        lista2.insert(1, "Centímetro ==> Polegada")
        lista2.insert(2, "Kilometro ==> Milha")

    if selecionado == 1:
        lista2.delete(0,"end")
        lista2.insert(0, "Kilograma ==> Libras")
        lista2.insert(1, "Grama ==> Onça")

    if selecionado == 2:
        lista2.delete(0,"end")
        lista2.insert(0, "Litro ==> Galão")
        lista2.insert(1, "Mililitro ==> Onça")

def calcular():
    escolhido = lista2.curselection()[0]
    aaa=lista2.get(escolhido)
    valorCampo = float(campo.get())
    
    if aaa == "Metro ==> Pés":
        resultado.delete(0, "end")
        resultado.insert(0, valorCampo * 3.281)
    
    if aaa == "Centímetro ==> Polegada":
        resultado.delete(0, "end")
        resultado.insert(0, valorCampo / 2.54)

    if aaa == "Kilometro ==> Milha":
        resultado.delete(0, "end")
        resultado.insert(0, valorCampo / 1.609)

    if aaa == "Kilograma ==> Libras":
        resultado.delete(0, "end")
        resultado.insert(0, valorCampo * 2.205)

    if aaa == "Grama ==> Onça":
        resultado.delete(0, "end")
        resultado.insert(0, valorCampo / 28.35)

    if aaa == "Litro ==> Galão":
        resultado.delete(0, "end")
        resultado.insert(0, valorCampo / 3.785)

    if aaa == "Mililitro ==> Onça":
        resultado.delete(0, "end")
        resultado.insert(0, valorCampo / 29.574)


janela = tk.Tk()
janela.title("Conversor de Medidas")
janela.geometry("600x600")

lista1 = tk.Listbox(janela, selectmode="single",)
lista1.grid(row=0, column=0)

lista1.insert(0,"Distância")
lista1.insert(1,"Massa")
lista1.insert(2,"Volume")

selecionaBt = tk.Button(janela,text="Seleciona", command=clica)
selecionaBt.grid(row=0, column=2)

lista2 = tk.Listbox(janela)
lista2.grid(row=1, column=0)

quadro = tk.Frame(janela)
quadro.grid(row=1, column=2)

campo = tk.Entry(quadro)
campo.grid()

calculaBt = tk.Button(quadro,text="Calcula", command=calcular)
calculaBt.grid()

resultado = tk.Entry(quadro)
resultado.grid()

janela.mainloop()