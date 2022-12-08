segundos = int(input('Digite os números de segundos que deseja converter: '))

horas = segundos // 3600
segs_restantes = segundos % 3600
minutos = segs_restantes // 60
final = segs_restantes % 60

print('O tempo é: ', horas, 'horas e', minutos, 'minutos e', final, 'segundos')