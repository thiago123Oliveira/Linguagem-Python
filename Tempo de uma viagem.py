__author__ = 'Aluno'

distancia=float(input('Digite a distância em KM: '))
velocidade=float(input('Digite a velocidade em KM/h: '))
tempo=(distancia/velocidade)
print('Tempo de viagem: %.2f '%tempo, 'h')
