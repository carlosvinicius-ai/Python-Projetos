"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hours = input('WHat time is it? ')

try:
    hours = int(hours)
    if hours >=0 and hours <= 11:
        print('Good Morning')
    
    elif hours >= 12 and hours <= 17:
        print('Good Afternoon')
    
    elif hours >= 18 and hours <= 23:
        print('Good Night')
    
    else:
        print("This hours don't exists")

except:
    print('Please, enter a valid value')
