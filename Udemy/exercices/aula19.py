# crie um programa que verifique entre 2 valores qual é o maior

first = input('Insert the first value: ')
second = input('Insert the second value: ')

try:
    first =  int(first)
    second = int(second)

    if first > second:
        print(f'{first=} greater than {second=}')
    else:
        print(f'{second=} greater than {first=}')

except ValueError as e:
    print("enter an integer value")