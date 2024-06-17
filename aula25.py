"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Hellen'
preco = 1000.85661235
variavel = '%s, o preço é R$%.2f' % (nome, preco) 
print(variavel)

print('O hexadecimal de %d é %04x' % (15,15))
#%04 preenche as casas que faltar com 0

print('O hexadecimal de %d é %08X' % (1500, 1500))