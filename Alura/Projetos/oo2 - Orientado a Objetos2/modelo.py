class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
        
    @property
    def ano(self):
        return self._ano
        
    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1


class Filme (Programa):         #para criar uma herança com a classe mãe
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self._ano = ano
        self._duracao = duracao
        self._likes = 0
        
    @property
    def duracao(self):
        return self._duracao
        
class Serie (Programa):
    def __init__(self, nome, ano, temporada):
        self._nome = nome.title()
        self._ano = ano
        self._temporada = temporada
        self._likes = 0
        
    @property
    def temporada(self):
        return self._temporada



vingadores = Filme("vingadores - guerra infinita", 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}m - Likes: {vingadores.likes}')

atlanta = Serie("atlanta", 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporada} - Likes {atlanta.likes}')
