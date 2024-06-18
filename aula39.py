"""
Integrando strings com while
"""
# #        01234567891011               indices positivos
# nome =  'Hellen Silva'  #Iteráveis
# #        11109876543210               indices negativos

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])            #buscando a letra do indice 3

#proximo exercicio unir as coisas
#nova_string += '*H*e*l*l*e*n**S*i*l*v*a*''

nome = 'Hellen Silva'

indice = 0
novo_nome = ''
while indice <len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
