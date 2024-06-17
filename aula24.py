# Operadores in e not in
# Strings são iteráveis (navega item por item)
#  0 1 2 3 4 5
#  H e l l e n
# -6-5-4-3-2-1
# in -> entre (esta entre)
# not in -> não entre (não esta entre)
# para acesar o indice usamos [ ]

# nome = 'Hellen'
# print(nome [1])
# print(nome [-5])
# print('e' in nome)
# print('zero' in nome)
# print(10* '-')
# print('e' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
        print(f'{encontrar} não está em {nome}')