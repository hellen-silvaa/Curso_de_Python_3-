# if /    elif   / else
#se  / se não se / se não
#pass ou ... -> passa aquele trecho de código que não foi escrito no momento
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True
# se condicao 1 for verdadeira execute este trecho de código
if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
# se não se
elif condicao2:
    print('Código para condição 2')
#Ao encontrar a condicao 3 como verdadeira ele executa e sai do blobo
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
# se não
else:
    print('Nenhuma condição foi satisfeita')

#fora do bloco
if 10 ==10:
        print('Outro if')

print('Fora do if')

#verifica a verdadeira e sai, ele não verifica os outros elif


