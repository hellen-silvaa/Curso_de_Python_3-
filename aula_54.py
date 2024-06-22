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



import os

# Inicializa uma lista vazia que será usada para armazenar os valores inseridos pelo usuário.
lista = []

# Loop infinito que permite ao usuário interagir com o programa continuamente até decidir parar.
while True:
    # Exibe um menu de opções para o usuário.
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    # Se a opção escolhida for 'i', insere um novo valor na lista.
    if opcao == 'i':
        # Limpa a tela (no Windows)
        os.system('cls')
        # Solicita um valor ao usuário e adiciona esse valor à lista.
        valor = input('Valor: ')
        lista.append(valor)

    # Se a opção escolhida for 'a', apaga um valor da lista com base no índice fornecido pelo usuário.
    elif opcao == 'a':
        # Solicita ao usuário o índice do valor que deseja apagar.
        indice_str = input('Escolha o índice para apagar: ')

        try:
            # Converte a string do índice para um inteiro.
            indice = int(indice_str)
            # Apaga o valor da lista no índice especificado.
            del lista[indice]
        except ValueError:
            # Trata o erro caso o valor inserido pelo usuário não seja um número inteiro.
            print('Por favor digite um número inteiro.')
        except IndexError:
            # Trata o erro caso o índice inserido pelo usuário não exista na lista.
            print('Índice não existe na lista.')
        except Exception:
            # Trata qualquer outro tipo de erro que possa ocorrer.
            print('Erro desconhecido.')

    # Se a opção escolhida for 'l', lista todos os valores presentes na lista.
    elif opcao == 'l':
        # Limpa a tela (no Windows). No Linux/MacOS, use 'clear' no lugar de 'cls'.
        os.system('cls')

        # Verifica se a lista está vazia e informa ao usuário caso não haja nada para listar.
        if len(lista) == 0:
            print('Nada para listar')

        # Itera sobre a lista e imprime cada índice e valor.
        for i, valor in enumerate(lista):
            print(i, valor)

    # Caso o usuário insira uma opção inválida, exibe uma mensagem de erro.
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