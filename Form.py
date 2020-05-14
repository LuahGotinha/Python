print('Olá, bem-vindo(a)')

name = input('Coloque seu nome: ')
age = int(input('Coloque sua idade: '))
adress = input('Colque seu endereço: ')
date = input('Está namorando/casado: ')
born_date = 2020 - age

print(f'''
Nome: {name}
Idade: {age}
Endereço: {adress}
Namorando: {date}
Ano de nascimento: {born_date}
    ''')
