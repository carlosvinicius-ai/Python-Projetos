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

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo Mundo em Panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
demolidor.dar_like()
tmep.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)