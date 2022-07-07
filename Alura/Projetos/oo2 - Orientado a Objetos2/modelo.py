class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        
    def dar_like(self):
        self._likes += 1
    
    @property       #get
    def likes(self):
        return self._likes
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter    #set      
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):      # dunder methods - neste caso um metodo criado para representar o objeto da classe de forma textual
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes {self._likes}'

class Filme (Programa):         #para criar uma herança com a classe mãe
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao  
        
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} min - Likes {self._likes}'
        
class Serie (Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
        
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporada} - Likes {self._likes}'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)