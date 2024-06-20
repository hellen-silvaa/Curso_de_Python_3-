"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativa = 0

while True:

    letra_digitada = input ('Digite uma letra: ')
    numero_tentativa += 1

    if len(letra_digitada)>1:
        print('Digite apenas uma letra.')
        continue

        #saber se a letra que digitou esta na palavra secreta:
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada #concatenação

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        #se a letra secreta estiver em letras acertadas exiba a letra 
        if letra_secreta in letras_acertadas:
             palavra_formada += letra_secreta
            #se a letra naõ estiver vai exibir o *
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        #limpa a tela e volta no começo
        os.system('cls')
        print('VOCÊ GANHOU, PARABÉNS!!!! ')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativa)
        #volta pro começo do jogo zerado
        letras_acertadas = ''
        numero_tentativa = 0


