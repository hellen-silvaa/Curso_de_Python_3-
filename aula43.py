# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python'

novo_texto = ''

#'para cada letra em texto exiba a letra na tela'
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')