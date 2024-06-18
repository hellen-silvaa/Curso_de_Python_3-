"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

#este valor é imutável
string = 'Maria'
outra_variavel = f'{string[:2]}ABC{string[3:]}'
print(outra_variavel)



#você não pode mudar o valor
# string[3] = 'ABC'
