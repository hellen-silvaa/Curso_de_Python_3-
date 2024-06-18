"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# com id o python busca a identidade do valor na memoria
# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

#declarar a variavel fora do bloco para usar ela dentro do bloco
condicao = False

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
   print('Não faça algo')

print(passou_no_if)
