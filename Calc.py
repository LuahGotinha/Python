import os
from math import sqrt

os.system('cls')

try:
    print('Que tipo de conta você quer?')
    answer = int(input('1. Regra de três\n2. Raiz\n3. Potência\n\n--->'))
    if answer == 1:
        os.system('cls')
        answer = input('Você quer com porcentagem? S | N\n')
        if answer.upper == 'S' or answer.upper == 'SIM':
            print('''
Exemplo: 1 número ---- 2 número
         3 número ----     X
            ''')
            number = float(input('\nO primeiro número: '))
            number2 = float(input('O segundo: '))
            number3 = float(input('O terceiro: '))
            print('O X é: ', number3*number2/number, '%')
        elif answer.upper == 'N' or answer.upper == 'NAO' or answer.upper == 'NÃO':
            os.system('cls')
            print('''
Exemplo: 1 número ---- 2 número
         3 número ----     X
            ''')
            number = float(input('\nO primeiro número: '))
            number2 = float(input('O segundo: '))
            number3 = float(input('O terceiro: '))
            print('O X é: ', number3*number2/number)
        else:
            print('Resposta errada!')

    elif answer == 2:
        os.system('cls')
        index = int(input('Indique o índice: '))
        rooting = float(input('Digite o radicando: '))
        print('A raiz é:', rooting ** (1/index))
        
    else:
        os.system('cls')
        number1 = int(input('Indique o expoênte: '))
        base = int(input('Indique a base: '))
        print('O resultado é:', base ** number1)

except ValueError:
    print('Valor errado!')