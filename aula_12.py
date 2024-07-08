nome = 'Hellen'
altura = 1.57
peso = 58
imc = peso / altura * altura
#imc = ... #Ellipsis (...) não gera erro 
print (f'{nome} tem {altura} altura \n pesa {peso} quilos \n e seu IMC é de {imc}')


# Hellen tem 1.57 de altura,
#pesa 58 quilos e seu IMC é 
# 
#o calcúlo do imc divide o peso em kg pela altura ao quadrado em metros
#IMC = peso / (altura x altura)


#Resolução Professor:
nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2
print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu imc é', )
print(imc)
