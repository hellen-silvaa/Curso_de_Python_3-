"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
#Lembre-te de desempacotamento
x,y, *resto = 1, 2, 3, 4
print(x,y, resto)


# def soma(x,y):
#     return x + y

def soma (*args):
    total = 0
    for numero in args:
        print('Total', total,'+', numero)
        total += numero
        print('Total', total)
    return total
    #passando args para lista
    # args = list(args)
    # print(args, type(args))


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(1, 2, 3, 4, 5, 6)
print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) #*numeros -> desempacotando
print(outra_soma)

#sum realiza a soma
print(sum((numeros)))

# print(*numeros)