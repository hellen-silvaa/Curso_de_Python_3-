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
    print(total)
    #passando args para lista
    # args = list(args)
    # print(args, type(args))


soma(1, 2, 3, 4, 5, 6)