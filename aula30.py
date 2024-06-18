"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
    simples é melhor do que complexo

"""

velocidade = 61 #velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #A distância onde o radar pega

#criar variavel do que esta repetindo para deixar o código limpo
velocidade_carro_passou_RADAR_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro<= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_RADAR_1
if velocidade_carro_passou_RADAR_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

#saber se foi ou não multado
if carro_multado_radar_1:
    print('Carro multado em radar 1')











