class Serie:
    
    def __init__(self, nome, genero, episodios, nota):
        self.indice = len(catalogo)
        self.nome = nome
        self.genero = genero
        self.episodios = episodios
        self.nota = nota

        def like(self):
            self.nota += 0.2
            if self.nota > 5:
                self.nota = 5
        def dislike(self):
            self.nota -= 0.2
            if self.nota < 0:
                self.nota = 0

catalogo = [ ]
catalogo.append(Serie("The Last of Us", "terror", 16, 4.2))
catalogo.append(Serie("Game of  Throne", "fantasia", 74, 4.6))
catalogo.append(Serie("Breaking Bad", "drama", 62, 4.2))
catalogo.append(Serie("Stranger Things", "terror", 42, 3.9))
catalogo.append(Serie("Uma Mente Excepcional", "fantasia", 37, 3.8))


while(True):
    comando = input("""Digite a função:
    1 - Ver series cadastradas
    2 - Procurar serie por genero
    3 - Mostrar series favoritas
    4 - Dar like em uma serie
    5 - Cadastrar nova serie
    0 - Sair
    """)
    
    match comando:
        case "1":
            print()
            for serie in catalogo:
                print(f"#{serie.indice} Nome: {serie.nome} / Genero: {serie.genero} / n° de episodios: {serie.episodios} / Nota: {serie.nota}")
            print()

        case "2":
            print()
            opção = input("Qual gênero te interessa? ")
            for serie in catalogo:
                if (serie.genero == opção):
                    print(f"#{serie.indice} Nome: {serie.nome} / Genero: {serie.genero} / n° de episodios: {serie.episodios} / Nota: {serie.nota}")
            print()

        case "3":
            print()
            for serie in catalogo:
                if (serie.nota > 4.0):
                    print(f"#{serie.indice} Nome: {serie.nome} / Genero: {serie.genero} / n° de episodios: {serie.episodios} / Nota: {serie.nota}")
            print()

        case "4":
            print()
            indice = int(input("Qual série você gostaria de avaliar? Digite o índice: "))
            avaliacao = str(input("like ou dislike? "))
                
            for serie in catalogo:
                if avaliacao == "like":
                    serie.like()
                    print(f"Você deu like em {serie.nome}! Nova nota: {serie.nota}")

                elif avaliacao == "dislike":
                    serie.dislike()
                    print(f"Você deu dislike em {serie.nome}! Nova nota: {serie.nota}")
                
            print("Obrigada pela sua avaliação!")
            print()

            

        case "5":
            novo_indice = len(catalogo)
            print()
            nome = input("Nome da série: ")
            genero = input("Gênero: ")
            episodios = int(input("Número de episódios: "))
            nota = float(input("Nota (0 a 5): "))
            print()
            
            nova_serie = Serie(nome, genero, episodios, nota)
            catalogo.append(nova_serie)

            print(f"Série {nome} cadastrada com sucesso!")
            print()
            for serie in catalogo:
                print(f"#{serie.indice} Nome: {serie.nome} / Genero: {serie.genero} / n° de episodios: {serie.episodios} / Nota: {serie.nota}")
            print()

        case "0":
            print("Fim do programa")
            break
        case _:
            print("Valor inválido")