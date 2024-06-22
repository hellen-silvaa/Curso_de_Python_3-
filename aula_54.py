"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []
#dar opçoes para usuário
while True:
    print('Selecione uma opção')
    opcao =input('[i]nserir [a]pagar [l]istar: ')

#
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input ('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l')










# #                     0       1        2         3
# lista_de_compra = ['maça', 'leite', 'arroz', 'macarrão']

# #inserir
# lista_de_compra.append('suco de maracujá') #passa a ser o indice 4 e ao apagar o leite ele passa a ser o 3

# #apagar
# del lista_de_compra [1] #vamos apagar o leite da nossa lista

# #listar valores da lista
# print(lista_de_compra)