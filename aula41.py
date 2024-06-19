"""while/ellse"""
#i -> variavel i para representar o indice e contar indice 
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else: 
    print('Não encontrei um espaço na string')
print('Fora do while')
#break encontrado já pula fora do while sem executar else
#se não tem break executa while