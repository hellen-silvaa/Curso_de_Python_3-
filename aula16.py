# if /    elif   / else
#se  / se não se / se não

entrada = input('Você quer "Entrar" ou "Sair"?.')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print('Bem vindo ao sistema')
    
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')


print('FORA DOS BLOCOS')