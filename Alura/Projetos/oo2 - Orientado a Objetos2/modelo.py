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


class Filme (Programa):         #para criar uma herança com a classe mãe
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao  
        
class Serie (Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}m - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporada} - Likes {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada     #hasattr é utilizado para saber se possui o atributo selecionado
    print(f'Nome: {programa.nome} - Ano: {programa.ano} - Temporadas/Duração: {detalhes} - Likes {programa.likes}')