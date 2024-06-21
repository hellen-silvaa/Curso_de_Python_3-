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
# string = 'ABCDE'  # 5 caracteres (len)
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


#------------------------------------------------------------------------------------------------------------------

#ALTERAR OS VALORES DA LISTA

#indice   0    1      2       3    4
#indice  -5    -4    -3      -2    -1
# lista = [123, True, 'Hellen', 1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))
#aqui alteramos o indice que continha o valor 'hellen' para o valor 'maria'

#------------------------------------------------------------------------------------------------------------------

#indice   0    1      2       3    4
#indice  -5    -4    -3      -2    -1
#lista = [1,2,3,4]
#pegando o valor do indice 2 e mostrando na tela, dado mutavel
# numero = lista[2]
# print(numero)
"""
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#SE EU ALTERAR A LISTA  LUGAR QUE EU REFERENCIAR A LISTA TAMBÉM VAI ALTERAR
# lista = [10,20,30,40] #CRIAR  Create
# lista[2] = 300 #ALTERAR       Update
# del lista[2]#DELETAR          Delete
# print(lista)

# #apagando o 30 o 40 passa a ser o indice 2, ele move todos indices da frente
# print(lista[2])

# lista.append(50) # adicionando item no final da lista
# lista.append(60)
# #lista.pop() #remove o último indice da lista

# lista.append(70)
# ultimo_valor = lista.pop()
# print(lista, 'Removido,', ultimo_valor)

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# #        0   1   2   3
# lista = [10, 20, 30, 40]
# lista.append('Hellen')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1] #-1 sempre será o ultimo inserido na lista
# #lista.clear() -> limpa lista
# lista.insert(0, 5) #adicioanr um item no indice 0 o valor 5
# print(lista)

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)

 #tipos de dados mutáveis - list e copy

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Hellen', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
