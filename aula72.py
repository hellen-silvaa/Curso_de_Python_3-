# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao (*args):
    total = 0
    for numero in args:
        total *= numero
        print(total)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
