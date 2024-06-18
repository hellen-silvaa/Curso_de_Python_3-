"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
#Loop infinito
# condicao = True
# while condicao:
#     print(1)
#     print(2)
#     print(3)


condicao = True
 
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
#break busca o laço mais proximo dele e sai do laço while 