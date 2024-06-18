"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
input sempre retorna string
"""

#numero_str = input('Vou dobrar o número que você digitar: ')

#SEMPRE QUE O USUARIO MANDA ALGO VOCÊ PRECISA TRATAR ESSE DADO
#transformando string digitada para número flutuante

#isdigit -> verifica se usuario digitou APENAS NÚMEROS True or False
# print(numero_str.isdigit())

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')


numero_str = input('Vou dobrar o número que você digitar: ')

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# try tenta executar e se ocorrer um erro dentro do try ele pula pro except