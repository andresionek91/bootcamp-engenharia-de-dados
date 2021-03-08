
class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.sobrenome = sobrenome
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos"


class Cachorro:
    def __init__(self, nome, raca, idade):
        self.raca = raca
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} é da raça {self.raca} e tem {self.idade} anos"

    def is_cachorro(self):
        return True


andre = Pessoa(nome='Andre', sobrenome='Sionek', idade=30)
belisco = Cachorro(nome='Belisco', raca='Lhasa', idade=1.5)

print(andre)
print(belisco)
print(belisco.is_cachorro())


class EngenheiroDeDados(Pessoa):
    def __init__(self, nome, sobrenome, idade, experiencia):
        super().__init__(nome, sobrenome, idade)
        self.experiencia = experiencia

    def __str__(self):
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos, " \
               f"é Engenheiro de Dados e tem {self.experiencia} anos de experiencia"


andre = EngenheiroDeDados(nome='Andre', sobrenome='Sionek', idade=30, experiencia=4)
print(andre)


class CatiorinhoFiaDaPuta(Cachorro):
    def is_fiadaputa(self):
        return True


belisco = CatiorinhoFiaDaPuta(nome='Belisco', raca='Lhasa', idade=1.5)
print(belisco.is_cachorro())
print(belisco.is_fiadaputa())
