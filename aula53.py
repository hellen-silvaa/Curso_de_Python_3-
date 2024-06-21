"""
enumerate - enumera iteráveis (índices)

enumerate para enumerar valores de iteráveis (pegar índices)


[(0, 'Hellen'), (1, 'Helena'), (2, 'Maria'), (3, 'João')]
"""

lista = ['Hellen', 'Helena', 'Maria']
lista.append('João')

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)


for item in enumerate(lista):
    indice, nome = item 
    print(indice, nome)

#esse é a mesma coisa do de cima,porém bemm mais simplificado
#código limpo    
for indice, nome in enumerate(lista):
    print(indice, nome)