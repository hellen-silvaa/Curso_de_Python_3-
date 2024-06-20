#pega item por item do range e faz alguma coisa
for i in range(10):
  if i == 2: #quando i for 2 print e volta no começo do laço
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break#quebra esse laço e pula pra fora do bloco

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')