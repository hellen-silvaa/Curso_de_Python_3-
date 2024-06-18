"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal

(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
#10 caracteres na esquerda
print(f'{variavel: >10}')
#10 caracteres na direita
print(f'{variavel: <10}.')
#10 caracteres no centro
print(f'{variavel: ^10}')
print(f'{variavel:$^10}')
print(f'{1000.6562565:,.1f}')
print(f'{-1000.6562565:-,.1f}')
print(f'{1000.6562565:0=+10,.1f}')

print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
