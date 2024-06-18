"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#SOLUÇÃO 1
# entrada_str = input ('Digite um número: ')

# if entrada_str.isdigit():
#     entrada_int = int(entrada_str)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}!')

# else:
#     print(f'{entrada_int} não é um número inteiro')

#-----------------------------------------------------------------------

#SOLUÇÃO 2
# entrada = input('Digite um número: ')

# try:
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')

# except:
#     print('Você não digitou um número inteiro')




"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input('Digite que horas são: ')
# entrada_int = int(entrada)

# bom_dia = 1 <= entrada_int <= 11
# boa_tarde = 12<= entrada_int <=17

# if bom_dia:
#     print('Bom dia!')
# elif boa_tarde:
#     print('Boa tarde!')
# else:
#     print('Boa noite!')


#SOLUÇÃO 1

# entrada = input('Digite a hora: ')

# try:
#     hora = int(entrada)

#     if hora >=0 and hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Não reconheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# entrada = input ('Digite seu primeiro nome: ')

# nome = len(entrada)

# try:

#     if 1 <= nome <= 4:
#         print('Seu nome é curto')
#     elif 5 <= nome <= 6:
#         print('Seu nome é normal')
#     elif  nome >= 6:
#         print('Seu nome é muito grande')
#     else:
#         print('Não reconheço esse nome')
# except:
#      print('Por favor, digite seu nome corretamente')

entrada = input ('Digite seu primeiro nome: ')

nome = len(entrada)

try:

    if 1 <= nome <= 4:
        print('Seu nome é curto')
    elif 5 <= nome <= 6:
        print('Seu nome é normal')
    elif  nome >= 6:
        print('Seu nome é muito grande')
    else:
        print('Não reconheço esse nome')
except:
     print('Por favor, digite seu nome corretamente')