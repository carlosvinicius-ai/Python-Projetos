class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
        
    @property
    def ano(self):
        return self.__ano
    
    @property
    def duracao(self):
        return self.__duracao
        
    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1
        
class Serie:
    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporada = temporada
        self.__likes = 0
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
        
    @property
    def ano(self):
        return self.__ano
    
    @property
    def temporada(self):
        return self.__temporada
        
    @property
    def likes(self):
        return self.__likes
        
    def dar_like(self):
        self.likes += 1



vingadores = Filme("vingadores - guerra infinita", 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}m - Likes: {vingadores.likes}')

atlanta = Serie("atlanta", 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporada} - Likes {atlanta.likes}')
