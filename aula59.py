# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Hellen', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Ruan', 'João', 'Eduarda', (0,10,20,30,40)],  # 2
]

#*_ = resto
#p, b, *_, ap,  u = lista
#print(p, u, ap)

#for nome in lista:
 #   print(nome, end=' ')

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')