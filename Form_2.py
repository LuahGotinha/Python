print('Hello :D')
name = input('Please, enter your name: ')
age = int(input('Please, enter your age: '))
adress = input('Please, enter your adress: ')
born_date = input('please, enter your born date (do not separate the number): ')
born_date = born_date[:2] + '/' + born_date[2:4] + '/' + born_date[4:]

print(f'''
Name: {name}
Age: {age}
Adress: {adress}
Born date: {born_date}
    ''')
