"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip -> corta espaços no começo e no fim
"""

frase = '     Olá só que           ,     coisa interessante           '
lista_palavras = frase.split()

#divida na virgula
lista_frases_cruas = frase.split(', ')


lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases)
print(lista_palavras)
print(lista_frases_cruas)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)