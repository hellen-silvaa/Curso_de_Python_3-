"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
len -> verifica qtd de caractere
"""
#listas conseguimos acessar elementos por elementos
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))
#lista = [] lista vazia type = list
#lsiats são mutaveis, conseguimos acessar o indice e mudar ele

#posso colocar uma lista dentro de outra
#indice   0    1      2       3    4
#indice  -1    -2     -3      -4   -5
lista = [123, True, 'Hellen', 1.2, []]
print(lista[2], type(lista[-1]))


