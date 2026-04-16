class Serie:
    
    def __init__(self, nome, genero, episodios, nota):
        self.indice = len(catalogo)
        self.nome = nome
        self.genero = genero
        self.episodios = episodios
        self.nota = nota

        def like(self):
            self.nota += 0.2
            if self.nota>5:
                self.nota = 5
        def dislike(self):
            self.nota -= 0.2
            if self.nota<0:
                self.nota = 0

catalogo = [ ]
catalogo.append(Serie("The Last of Us", "terror", 16, 4.2))
catalogo.append(Serie("Game of  Throne", "fantasia", 74, 4.6))
catalogo.append(Serie("Breaking Bad", "drama", 62, 4.2))
catalogo.append(Serie("Stranger Things", "terror", 42, 3.9))
catalogo.append(Serie("Uma Mente Excepcional", "fantasia", 37, 3.8))


while(True):
    comando = input("""Digite a função:
    1 - Ver séries cadastradas
    2 - Procurar serie por genero
    3 - Mostrar séries favoritas
    4 - Dar like em uma serie
    5 - Cadastrar nova serie
    0 - Sair
    """)

    match comando:
        case "1":
            for serie in catalogo:
                print(f"#{serie.indice} Nome: {serie.nome} / Genero: {serie.genero} / n° de episodios: {serie.episodios} / Nota: {serie.nota}")
            print()

        case "2":
            print()
            opção = input("Qual gênero te interessa? ")
            for serie in catalogo:
                if (serie.genero == opção):
                    print(f"#{serie.indice} Nome: {serie.nome} / Genero: {serie.genero} / n° de episodios: {serie.episodios} / Nota: {serie.nota}")





        case "3":
            print("Mostrar series favoritas")
        case "4":
            print("Dar like")
        case "5":
            print("Cadastrar serie")
        case "0":
            print("Fim do programa")
            break
        case _:
            print("Valor inválido")