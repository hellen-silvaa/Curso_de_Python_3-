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
#upper -> maiusculas
#posso colocar uma lista dentro de outra
# indice   0    1      2       3    4
# indice  -5    -4    -3      -2    -1
# lista = [123, True, 'Hellen', 1.2, []]
# print(lista[2].upper(), type(lista[-4]))




#ALTERAR OS VALORES DA LISTA

#indice   0    1      2       3    4
#indice  -5    -4    -3      -2    -1
lista = [123, True, 'Hellen', 1.2, []]
lista[-3] = 'Maria'
print(lista[2], type(lista[2]))
#aqui alteramos o indice que continha o valor 'hellen' para o valor 'maria'


