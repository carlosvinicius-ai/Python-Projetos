class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        
class Serie:
    def __init__(self, nome, ano, temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada

vingadores = Filme("Vingadores", 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}m')

atlanta = Serie("atlanta", 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporada}')
