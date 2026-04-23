class Funcionario:
    def __init__(self, indice, cargo, nome, login, salario):
        self.indice = indice
        self.cargo = cargo
        self.nome = nome
        self.login = login
        self.salario = salario

    def info(self):
        return (f"#{self.indice} - Cargo: {self.cargo} - Nome: {self.nome} - Email: {self.login}@empresa.com - Salário: {self.salario}")


class Estagiario(Funcionario):
    def __init__(self, indice, nome, login, ano_matricula):
        super().__init__(indice, "Estagiario", nome, login, 1200)
        self.ano_matricula = ano_matricula

    def info(self):
        return super().info() + f" - Ano de matrícula: {self.ano_matricula}"


class Tecnico(Funcionario):
    def __init__(self, indice, nome, login, salario, nivel=1):
        super().__init__(indice, "Tecnico" , nome, login, salario)
        self.nivel = nivel

    def info(self):
        return super().info() + f" - Nível de acesso: n{self.nivel}"

    def diminui_nivel(self):
        if(self.nivel > 1):
            self.nivel = self.nivel - 1
            return f"Sucesso! Usuário agora é n{self.indice}"
        else:
            return f"Fracasso! Usuário já é n1"

    def aumenta_nivel(self):
        if(self.nivel < 3):
            self.nivel = self.nivel + 1
            return f"Sucesso! Usuário agora é n{self.indice}"
        else:
            return f"Fracasso! Usuário já é n3"

class Vendedor(Funcionario):
    def __init__(self, indice, nome, login, quantidade_vendas=1):
        super().__init__(indice, "Vendedor", nome, login, 2000)
        self.quantidade_vendas = quantidade_vendas

    def info(self):
        return super().info() + f" - Quantidade de vendas: {self.quantidade_vendas}"

    def aumenta_venda(self):
        self.quantidade_vendas = quantidade_vendas + 1

funcionarios =  [ ]

funcionarios.append(Funcionario(0, "Gerente", "Bruno", "bruno.dantes", 2500))
funcionarios.append(Estagiario(1, "Lucas", "lusca.renan", 2026))
funcionarios.append(Tecnico(2, "Manu", "manu.ramos", 4000))
funcionarios.append(Tecnico(3, "Isabella", "isabella.correa", 5000, 2))
funcionarios.append(Vendedor(4, "Vitor", "vitor.rodrigues", 15))

print()
for f in funcionarios:
    print(f.info())